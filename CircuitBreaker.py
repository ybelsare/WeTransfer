import functools
import http
import logging
from datetime import datetime
import requests
import flask

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s,%(msecs)d %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)


class StateChoices:
    OPEN = "open"
    CLOSED = "closed"
    HALF_OPEN = "half_open"


class CircuitBreaker:
    def __init__(self, http_client, threshold, delay):
        self.threshold = threshold
        self.delay = delay
        self.state = StateChoices.CLOSED
        self.last_attempt_timestamp = None
        self._failed_attempt_count = 0

    def update_last_attempt_timestamp(self):
        self.last_attempt_timestamp = datetime.utcnow().timestamp()

    def set_state(self, state):
        prev_state = self.state
        self.state = state
        logging.debug(f"Changed state from {prev_state} to {self.state}")

    def handle_closed_state(self, url):
        response = requests.get(url)
        if response.status_code == http.HTTPStatus.OK:
            self.update_last_attempt_timestamp()
            self.set_state(StateChoices.CLOSED)
            return 0
        if 500 <= response.status_code < 600:
            self.update_last_attempt_timestamp()
            self._failed_attempt_count += 1
            if self._failed_attempt_count >= self.threshold:
                self.set_state(StateChoices.OPEN)

    def handle_open_state(self, url):
        current_timestamp = datetime.utcnow().timestamp()
        if self.last_attempt_timestamp + self.delay >= current_timestamp:
            logging.info("Retry after some time")

            return 0
        else:
            self.set_state(StateChoices.CLOSED)
            self._failed_attempt_count = 0
            self.update_last_attempt_timestamp()
            response = requests.get(url)
            if response.status_code == http.HTTPStatus.OK:
                self.update_last_attempt_timestamp()
                self.set_state(StateChoices.CLOSED)
                return 0
            if 500 <= response.status_code < 600:
                self.update_last_attempt_timestamp()
                self._failed_attempt_count += 1
                if self._failed_attempt_count >= self.threshold:
                    self.set_state(StateChoices.OPEN)

    def do_request(self, url: str) -> int:
        if self.state == StateChoices.CLOSED:
            return self.handle_closed_state(url)
        if self.state == StateChoices.OPEN:
            return self.handle_open_state(url)
        return 0

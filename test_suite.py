import pytest
from CircuitBreaker import CircuitBreaker
from CircuitBreaker import StateChoices
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,%(msecs)d %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)

faulty_endpoint = "http://localhost:5000/failure"
success_endpoint = "http://localhost:5000/success"
random_status_endpoint = "http://localhost:5000/random"


# Threshold = 2 and delay = 60 seconds

def test_all_success():
    _circuit_breaker = CircuitBreaker(None, 2, 60)
    for _ in range(5):
        _circuit_breaker.do_request(success_endpoint)
    assert (_circuit_breaker.state == StateChoices.CLOSED)


# Three Failures -> Sleep -> Success
# Circuit should open after first two failed request and then close after a delay
# After delay the successful entries should go through
def test_failures_success_scenario1():
    _circuit_breaker = CircuitBreaker(None, 2, 60)
    for _ in range(3):
        _circuit_breaker.do_request(faulty_endpoint)
    assert (_circuit_breaker.state == StateChoices.OPEN)
    time.sleep(65)
    for _ in range(2):
        _circuit_breaker.do_request(success_endpoint)
    assert (_circuit_breaker.state == StateChoices.CLOSED)


def test_all_failures():
    _circuit_breaker = CircuitBreaker(None, 2, 60)
    for _ in range(3):
        _circuit_breaker.do_request(faulty_endpoint)
    assert (_circuit_breaker.state == StateChoices.OPEN)
    time.sleep(65)
    for _ in range(3):
        _circuit_breaker.do_request(faulty_endpoint)
    assert (_circuit_breaker.state == StateChoices.OPEN)


def test_mix():
    _circuit_breaker = CircuitBreaker(None, 2, 60)
    for _ in range(3):
        _circuit_breaker.do_request(faulty_endpoint)
    assert (_circuit_breaker.state == StateChoices.OPEN)
    time.sleep(65)
    for _ in range(3):
        _circuit_breaker.do_request(faulty_endpoint)
    assert (_circuit_breaker.state == StateChoices.OPEN)
    time.sleep(65)
    for _ in range(5):
        _circuit_breaker.do_request(success_endpoint)
    assert (_circuit_breaker.state == StateChoices.CLOSED)


def test_delay():
    _circuit_breaker = CircuitBreaker(None, 2, 60)
    for _ in range(3):
        _circuit_breaker.do_request(faulty_endpoint)
    assert (_circuit_breaker.state == StateChoices.OPEN)
    time.sleep(65)
    _circuit_breaker.do_request(success_endpoint)
    assert (_circuit_breaker.state == StateChoices.CLOSED)

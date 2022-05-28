from CircuitBreaker import CircuitBreaker
import http
import requests
import logging
import time

faulty_endpoint = "http://localhost:5000/failure"
success_endpoint = "http://localhost:5000/success"
random_status_endpoint = "http://localhost:5000/random"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,%(msecs)d %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)

if  __name__ == '__main__':
    _circuit_breaker = CircuitBreaker(None,2,60)
    _circuit_breaker.do_request(faulty_endpoint)
    _circuit_breaker.do_request(faulty_endpoint)
    _circuit_breaker.do_request(faulty_endpoint)
    time.sleep(100)
    _circuit_breaker.do_request(faulty_endpoint)




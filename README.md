# WeTransfer
    Circuit Breaker Implementation

# Project Structure
    CircuitBreaker.py - Contains the circuit breaker implemenetation
    service.py - Contains the server with 3 endpoints 1) Success 2) Failure 3 ) Random 
    main.py - shows how to use the circuit breaker
    test_suite.py - pytest test file
    requirements.txt - use pip install -r requirements.txt to install dependencies

# Instructions
    1) Download the code from the repository
    2) run python service.py to start the server 
    3) run pytest test_suite.py to run the unit tests 

# Sample output  of circuit breaker
    _circuit_breaker = CircuitBreaker(None, 2, 60)
    The threshold is 2 requests and delay is 60 secs

    _circuit_breaker.do_request(faulty_endpoint)
    _circuit_breaker.do_request(faulty_endpoint)
    # At this Point the Circuit is OPENED
    _circuit_breaker.do_request(faulty_endpoint) - This will send a message to retry after sometime
    _circuit_breaker.do_request(success_endpoint)- This will send a message to retry after sometime
    time.sleep(100) - Delay
    _circuit_breaker.do_request(success_endpoint) - This will succeed
    _circuit_breaker.do_request(success_endpoint) - This will succeed
    _circuit_breaker.do_request(faulty_endpoint)  
    _circuit_breaker.do_request(faulty_endpoint)
    _circuit_breaker.do_request(success_endpoint) - This will send a message to retry 

     C:\Users\446891\AppData\Local\Programs\Python\Python39\python.exe C:/Users/446891/PycharmProjects/WeTransfer/main.py
    20:46:32,85 DEBUG: in handle_closed_state ..
    20:46:32,155 DEBUG: Starting new HTTP connection (1): localhost:5000
    20:46:34,187 DEBUG: http://localhost:5000 "GET /failure HTTP/1.1" 500 20
    20:46:34,187 DEBUG: url request failed .. 
    20:46:34,187 DEBUG: in handle_closed_state ..
    20:46:34,187 DEBUG: Starting new HTTP connection (1): localhost:5000
    20:46:36,237 DEBUG: http://localhost:5000 "GET /failure HTTP/1.1" 500 20
    20:46:36,237 DEBUG: url request failed .. 
    20:46:36,237 ERROR: threshold has been breached
    20:46:36,237 ERROR: Circuit Breaker triggered .. OPEN
    20:46:36,237 DEBUG: Changed state from closed to open
    20:46:36,237 ERROR: Circuit Breaker is Open .. Retry after some time
    20:46:36,237 ERROR: Circuit Breaker is Open .. Retry after some time
    20:48:16,244 DEBUG: Sufficient Delay ...
    20:48:16,244 DEBUG: Circuit Breaker has been CLOSED
    20:48:16,244 DEBUG: Changed state from open to closed
    20:48:16,261 DEBUG: Starting new HTTP connection (1): localhost:5000
    20:48:18,302 DEBUG: http://localhost:5000 "GET /success HTTP/1.1" 200 20
    20:48:18,302 DEBUG: Changed state from closed to closed
    20:48:18,302 DEBUG: in handle_closed_state ..
    20:48:18,310 DEBUG: Starting new HTTP connection (1): localhost:5000
    20:48:20,336 DEBUG: http://localhost:5000 "GET /success HTTP/1.1" 200 20
    20:48:20,336 DEBUG: Changed state from closed to closed
    20:48:20,336 DEBUG: in handle_closed_state ..
    20:48:20,336 DEBUG: Starting new HTTP connection (1): localhost:5000
    20:48:22,378 DEBUG: http://localhost:5000 "GET /failure HTTP/1.1" 500 20
    20:48:22,378 DEBUG: url request failed .. 
    20:48:22,378 DEBUG: in handle_closed_state ..
    20:48:22,391 DEBUG: Starting new HTTP connection (1): localhost:5000
    20:48:26,457 DEBUG: http://localhost:5000 "GET /failure HTTP/1.1" 500 20
    20:48:26,457 DEBUG: url request failed .. 
    20:48:26,457 ERROR: threshold has been breached
    20:48:26,457 ERROR: Circuit Breaker triggered .. OPEN
    20:48:26,457 DEBUG: Changed state from closed to open
    20:48:26,457 ERROR: Circuit Breaker is Open .. Retry after some time

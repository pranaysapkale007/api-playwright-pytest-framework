import time

def retry_request(func, retries=3, delay=2):
    """
    Retry wrapper for API requests
    Retries the function call if response status >= 500 (server errors)
    """
    for attempt in range(retries):
        response = func()
        if response.status < 500:
            return response
        time.sleep(delay)
    return response
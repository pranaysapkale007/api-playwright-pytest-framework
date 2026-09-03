"""
Validators.py
Reusable validation functions for API responses.
Keep test cases clean by moving common checks here.
"""
def assert_status_code(response, expected_status):
    actual_status = response.status
    assert actual_status == expected_status, (f"Expected Status {expected_status}, but got {actual_status}")

def assert_key_in_response(response_json, key):
    assert key in response_json, f"Key '{key}' not found in response JSON"

def assert_list_not_empty(response_json, key):
    assert len(response_json[key]) > 0, f"List '{key}' is empty in response JSON"

def assert_header(response, header_name, expected_value=None):
    headers = response.headers
    assert header_name in headers, f"Header '{header_name}' not found"
    if expected_value:
        assert headers[header_name] == expected_value, (
            f"Expected header '{header_name}' value '{expected_value}', "
            f"but got '{headers[header_name]}'"
        )
import pytest
from playwright.sync_api import sync_playwright
from utils.validators import *

def test_get_users(api_client):
    """
    Test to fetch users from ReqRes API.
    Demonstrates GET request + basic assertions
    """
    response = api_client.get("/api/users?page=2")
    data = response.json()

    # Assertion 1: Status code check
    assert_status_code(response, 200)

    # Assertion 2: Response body contains 'data'
    assert_key_in_response(data, "data")

    # ASsertion 3: At least one user exists
    assert_list_not_empty(data, "data")

    # Assertion 4: Response header contains 'Content-Type'
    assert_header(response, "content-type", "application/json; charset=utf-8")
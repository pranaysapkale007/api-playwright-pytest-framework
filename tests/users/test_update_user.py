from utils.validators import assert_status_code, assert_key_in_response

def test_update_user(api_client, test_data):
    """
    Test to update an existing user using PUT request.
    Demonstrates PUT + response validation.
    """
    payload = test_data["update_user"]
    response = api_client.put("/api/users/2", payload)

    # ✅ Assertion 1: Status code check
    assert_status_code(response, 200)

    # ✅ Assertion 2: Response contains updated fields
    data = response.json()
    assert_key_in_response(data, "name")
    assert_key_in_response(data, "job")
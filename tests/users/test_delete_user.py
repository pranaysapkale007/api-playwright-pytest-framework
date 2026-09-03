from utils.validators import assert_status_code

def test_delete_user(api_client):
    """
    Test to delete an existing user using DELETE request.
    Demonstrates DELETE + response validation.
    """
    response = api_client.delete("/api/users/2")

    # ✅ Assertion: Status code should be 204 (No Content)
    assert_status_code(response, 204)

import pytest
from utils.validators import assert_status_code

@pytest.mark.parametrize("email, password", [
    ("eve.holt@reqres.in", "cityslicka"),
    ("wrong@example.com", "badpassword")
])
def test_login(api_client, email, password):
    payload = {"email": email, "password": password}
    response = api_client.post("/api/login", payload)

    if email == "eve.holt@reqres.in":
        assert_status_code(response, 200)
    else:
        assert_status_code(response, 400)
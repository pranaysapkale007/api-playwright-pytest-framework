from utils.retry import retry_request


def test_get_users_with_retry(api_client):
    response = retry_request(lambda: api_client.get("/api/users?page=2"))
    assert response.status == 200
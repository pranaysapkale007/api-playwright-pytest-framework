from utils.logger import get_logger

logger = get_logger()

def test_create_user(api_client, test_data):
    """
    Test to create a new user using POST request
    """
    payload = test_data["create_user"]
    
    logger.info(f"Creating user with payload: {payload}")

    response = api_client.post("/api/users", payload)
    data = response.json()
    
    logger.info(f"Response JSON: {data}")

    # Assertion 1: Status Code check
    assert response.status == 201

    # Assertion 2: Response contains 'id' and 'createdAt'
    data = response.json()
    assert "id" in data
    assert "createdAt" in data
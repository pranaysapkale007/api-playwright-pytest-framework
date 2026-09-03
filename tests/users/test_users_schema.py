from utils.schema_validator import validate_schema

user_list_schema = {
    "type": "object",
    "properties": {
        "page": {"type": "integer"},
        "data": {"type": "array"}
    },
    "required": ["page", "data"]
}

def test_get_users_schema(api_client):
    response = api_client.get("/api/users?page=2")
    data = response.json()
    validate_schema(data, user_list_schema)
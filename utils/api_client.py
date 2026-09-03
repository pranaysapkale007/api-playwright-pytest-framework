"""
api_client.py
Reusable API client using Playwright's APIRequestContext
This file acts like a toolbox with helper methods for GET, POST, PUT, DELETE.
"""
import json

class APIClient:
    def __init__(self, request_context):
        """
        Initialize with Playwright request context.
        request_context comes from our pytest fixture file conftest.py.
        """
        self.request_context = request_context

    def get(self, endpoint):
        """
        Perform a GET request.
        Example: client.get("/api/users?page=2")
        """
        return self.request_context.get(endpoint)

    def post(self, endpoint, payload):
        """
        Perform a POST request with JSON payload.
        """
        return self.request_context.post(endpoint, data=json.dumps(payload))

    def put(self, endpoint, payload):
        return self.request_context.put(endpoint, data=json.dumps(payload))

    def delete(self, endpoint):
        return self.request_context.delete(endpoint)
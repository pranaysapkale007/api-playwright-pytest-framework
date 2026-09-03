import json
import pytest
from playwright.sync_api import sync_playwright
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def config():
    """
    Fixture to load configuration details from config.json.
    Scope=session -> runs once per test session..
    """
    with open("config/config.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def api_client(config):
    """
    Create APIClient instance with Playwright request context
    This fixture gives us a ready-to-use client in all test.
    """
    playwright = sync_playwright().start()
    request_context = playwright.request.new_context(
        base_url=config["base_url"],
        extra_http_headers=config["headers"]
    )
    client = APIClient(request_context)
    yield client
    # Cleanup after tests finish
    request_context.dispose()
    playwright.stop()

@pytest.fixture(scope="session")
def test_data():
    with open("config/test_data.json") as f:
        return json.load(f)
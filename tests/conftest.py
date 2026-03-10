import pytest
from fastapi.testclient import TestClient
from src.app import app
import src.app as app_module


@pytest.fixture
def mock_activities():
    """Provide mock activities data for testing"""
    return {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": []
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        }
    }


@pytest.fixture
def client(mock_activities, monkeypatch):
    """Provide a test client with mock activities"""
    # Replace the global activities dictionary with mock data
    monkeypatch.setattr(app_module, "activities", mock_activities)
    return TestClient(app)

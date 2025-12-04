import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi_app import app
from backend.database import Base, get_db
from backend import models


TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function", autouse=True)
def setup_database(monkeypatch):
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    os.environ["ADMIN_TOKEN"] = "test-token"

    yield
    Base.metadata.drop_all(bind=engine)
    app.dependency_overrides = {}


def auth_headers():
    return {"X-Admin-Token": "test-token"}


def test_create_expert(client):
    response = client.post(
        "/api/experts",
        json={
            "name": "Test Expert",
            "title": "AI Lead",
            "summary": "Testing expert creation.",
            "linked_in_url": "https://www.linkedin.com/in/test-expert/",
            "location": "Abu Dhabi",
            "expertise": "Automation",
            "tools": "RPA",
        },
        headers=auth_headers(),
    )
    assert response.status_code == 201
    body = response.json()
    assert body["name"] == "Test Expert"
    assert body["vetted_status"] == "approved"


@pytest.fixture
def client():
    return TestClient(app)


def seed_experts(session):
    expert_1 = models.Expert(
        name="Alice AI",
        title="AI Engineer",
        summary="Building AI solutions",
        linked_in_url="https://example.com/alice",
        location="Dubai",
        expertise="NLP",
        tools="Transformers",
        vetted_status="approved",
    )
    expert_2 = models.Expert(
        name="Bob Builder",
        title="ML Architect",
        summary="Designs ML platforms",
        linked_in_url="https://example.com/bob",
        location="Abu Dhabi",
        expertise="Computer Vision",
        tools="CNNs",
        vetted_status="pending",
    )
    expert_3 = models.Expert(
        name="Carla Creator",
        title="AI Product Manager",
        summary="Launches AI products",
        linked_in_url="https://example.com/carla",
        location="Dubai",
        expertise="Product",
        tools="Roadmaps",
        vetted_status="approved",
    )
    session.add_all([expert_1, expert_2, expert_3])
    session.commit()
    return expert_1, expert_2, expert_3


def test_list_experts_default_filter(client):
    session = TestingSessionLocal()
    seed_experts(session)
    session.close()

    response = client.get("/api/experts")
    assert response.status_code == 200
    body = response.json()
    assert len(body) == 2  # Only approved


def test_list_experts_search_query(client):
    session = TestingSessionLocal()
    seed_experts(session)
    session.close()

    response = client.get("/api/experts", params={"q": "builder"})
    assert response.status_code == 200
    body = response.json()
    assert len(body) == 1
    assert body[0]["name"] == "Bob Builder"


def test_filter_by_expertise_and_location(client):
    session = TestingSessionLocal()
    seed_experts(session)
    session.close()

    response = client.get(
        "/api/experts", params={"expertise": "Product", "location": "Dubai"}
    )
    assert response.status_code == 200
    body = response.json()
    assert len(body) == 1
    assert body[0]["name"] == "Carla Creator"


def test_pending_not_included_without_filter(client):
    session = TestingSessionLocal()
    seed_experts(session)
    session.close()

    response = client.get("/api/experts")
    assert response.status_code == 200
    names = [item["name"] for item in response.json()]
    assert "Bob Builder" not in names

    response_all = client.get("/api/experts", params={"vetted_status": "pending"})
    assert response_all.status_code == 200
    names = [item["name"] for item in response_all.json()]
    assert "Bob Builder" in names

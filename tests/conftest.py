"""Pytest fixtures for the music resolver API tests."""

import pytest
from fastapi.testclient import TestClient

from app.main import app, limiter


@pytest.fixture()
def client():
    limiter.reset()
    with TestClient(app) as c:
        yield c

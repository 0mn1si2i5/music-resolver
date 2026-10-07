"""HTTP surface of the resolver service."""

from fastapi.testclient import TestClient


def test_health(client: TestClient):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_platforms_lists_four_platforms(client: TestClient):
    resp = client.get("/api/platforms")
    assert resp.status_code == 200
    assert [p["id"] for p in resp.json()["platforms"]] == ["Spotify", "AppleMusic", "Netease", "QQMusic"]


def test_resolve_requires_raw_link(client: TestClient):
    resp = client.post("/api/resolve", json={})
    assert resp.status_code == 400
    assert resp.json()["detail"] == "rawLink is required"


def test_resolve_rejects_invalid_json(client: TestClient):
    resp = client.post("/api/resolve", content="not json", headers={"Content-Type": "application/json"})
    assert resp.status_code == 400


def test_no_cors_headers_without_configured_origins(client: TestClient):
    resp = client.get("/health", headers={"Origin": "http://evil.example"})
    assert "access-control-allow-origin" not in resp.headers

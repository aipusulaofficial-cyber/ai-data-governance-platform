from fastapi.testclient import TestClient

from service import app


def test_http_contract_and_domain():
    c = TestClient(app)
    assert c.get("/health/live").status_code == 200
    r = c.post(
        "/v1/governance",
        json={
            "key": "integration",
            "payload": {
                "owner": "alice",
                "actor": "alice",
                "classification": "public",
                "required_classification": "public",
            },
        },
    )
    assert r.status_code == 200, r.text

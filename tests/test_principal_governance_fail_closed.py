import pytest

from governance_domain import Asset, evaluate
from policy_store import PolicyStore


@pytest.mark.parametrize(
    "asset_classification,requested",
    [("unknown", "restricted"), ("confidential", "unknown"), ("unknown", "unknown")],
)
def test_unrecognized_classifications_fail_closed(asset_classification, requested):
    decision = evaluate(
        Asset("asset-1", "alice", asset_classification),
        requested,
        "alice",
    )
    assert not decision.allowed
    assert "unknown_classification" in decision.reasons


def test_valid_classification_still_works():
    assert evaluate(Asset("asset-1", "alice", "public"), "internal", "alice").allowed


def test_stale_policy_write_is_rejected_without_overwriting(tmp_path):
    store = PolicyStore(str(tmp_path / "policies.db"))
    store.put("access", 1, "first")
    store.put("access", 2, "second")
    with pytest.raises(ValueError, match="strictly increase"):
        store.put("access", 1, "stale")
    assert store.get("access") == ("access", 2, "second")


@pytest.mark.parametrize("version", [True, 0, "1"])
def test_invalid_policy_version_is_rejected(tmp_path, version):
    store = PolicyStore(str(tmp_path / "policies.db"))
    with pytest.raises(ValueError, match="invalid policy"):
        store.put("access", version, "document")

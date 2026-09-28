from governance_domain import Asset, evaluate


def test_policy_allows_owner_within_classification():
    decision = evaluate(Asset("a1", "alice", "internal"), "confidential", "alice")
    assert decision.allowed is True
    assert decision.reasons == ()


def test_policy_rejects_owner_or_classification_violation():
    decision = evaluate(Asset("a1", "alice", "restricted"), "internal", "bob")
    assert decision.allowed is False
    assert set(decision.reasons) == {"owner_mismatch", "classification_exceeds_request"}

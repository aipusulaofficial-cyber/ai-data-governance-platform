from governance_domain import Asset, evaluate


def test_unknown_classification_fails_closed():
    asset = Asset("a1", "owner", "mystery")
    decision = evaluate(asset, "mystery", "owner")
    assert not decision.allowed
    assert "unknown_classification" in decision.reasons


def test_known_classification_owner_allowed():
    asset = Asset("a1", "owner", "internal")
    assert evaluate(asset, "confidential", "owner").allowed

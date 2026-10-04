import pytest

from governance_domain import Asset, evaluate
from service import _validated_tags


def test_unknown_classification_fails_closed():
    asset = Asset("a1", "owner", "mystery")
    decision = evaluate(asset, "mystery", "owner")
    assert not decision.allowed
    assert "unknown_classification" in decision.reasons


def test_known_classification_owner_allowed():
    asset = Asset("a1", "owner", "internal")
    assert evaluate(asset, "confidential", "owner").allowed


def test_malformed_tags_are_rejected_before_policy_evaluation():
    with pytest.raises(ValueError):
        _validated_tags({"tags": "admin"})
    with pytest.raises(ValueError):
        _validated_tags({"tags": ["ok", 7]})

from governance_domain import Asset, evaluate


def test_policy():
    a = Asset("1", "alice", "confidential")
    assert evaluate(a, "restricted", "alice").allowed
    assert not evaluate(a, "public", "bob").allowed

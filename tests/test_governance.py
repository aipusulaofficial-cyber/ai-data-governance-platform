from governance import *

import pytest



def test_lineage():
    c = Catalog()
    [c.register(Asset(x, "team", "internal")) for x in "abc"]
    c.link("a", "b")
    c.link("b", "c")
    assert c.lineage("a") == {"a", "b", "c"}



def test_owner():
    with pytest.raises(GovernanceError):
        Catalog().register(Asset("a", "", "public"))



def test_policy():
    with pytest.raises(GovernanceError):
        Policy().check(Asset("a", "t", "restricted"), {"public"})

from dataclasses import dataclass, field


@dataclass
class Asset:
    id: str
    owner: str
    classification: str
    tags: set[str] = field(default_factory=set)


@dataclass(frozen=True)
class PolicyDecision:
    allowed: bool
    reasons: tuple[str, ...]


def evaluate(asset: Asset, required_classification: str, actor: str) -> PolicyDecision:
    reasons = []
    if not asset.owner or actor != asset.owner:
        reasons.append("owner_mismatch")
    order = {"public": 0, "internal": 1, "confidential": 2, "restricted": 3}
    if asset.classification not in order or required_classification not in order:
        reasons.append("unknown_classification")
    elif order[asset.classification] > order[required_classification]:
        reasons.append("classification_exceeds_request")
    return PolicyDecision(not reasons, tuple(reasons))

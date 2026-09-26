# AI Data Governance Platform

A governance service for defining, validating and auditing how AI workloads access and use data.

## What this project does
The platform places governance decisions at explicit boundaries: incoming data is validated, policy is evaluated, lineage-oriented metadata is retained, and access decisions remain auditable.

## Architecture
```text
Data / access request
        |
        v
Contract + validation
        |
        v
Governance policy
     /       \
  allow      deny
    |          |
adapter      audit
    |
result + lineage metadata
```

Domain policy is separated from infrastructure adapters so storage or provider changes do not redefine governance rules.

## Contracts & auditability
Contracts define accepted data and access-request shapes. Validation rejects invalid input before policy evaluation. Decisions retain context needed to explain authorization outcomes and associated lineage.

## Reliability & security
Failure paths are explicit, external dependencies are isolated in tests, and security controls are validated in CI. Operational failures are distinguishable from legitimate governance denials.

## Delivery evidence
CI, production tests and security/SBOM checks are executable gates. Architecture and trade-offs are documented in [ARCHITECTURE.md](ARCHITECTURE.md) and [ADRs](ADRs/).

## Engineering standard
**Code → Contract → Test → Security → Runtime → Observability → Deployment → Evidence**.
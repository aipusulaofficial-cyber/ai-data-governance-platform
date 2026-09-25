# ADR-0002: Production hardening
The governance API uses FastAPI and OpenTelemetry at the edge. Kubernetes probes/resources and Helm define runtime packaging; Terraform owns infrastructure inputs. Trivy and CycloneDX enforce supply-chain checks; contract/property tests protect API boundaries; Locust supplies load validation.
State and lineage remain domain concerns; production externalizes durable storage, secrets and telemetry.

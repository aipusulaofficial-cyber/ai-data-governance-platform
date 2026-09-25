from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from opentelemetry import trace
from governance_domain import *
try:
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
    p = TracerProvider(
        resource=Resource.create({"service.name": "ai-data-governance-platform"})
    )
    p.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
    trace.set_tracer_provider(p)
except Exception:
    pass
app = FastAPI(title="ai-data-governance-platform", version="1.0.0")
tracer = trace.get_tracer("ai-data-governance-platform")


class Request(BaseModel):
    key: str
    payload: dict = {}


@app.get("/health/live")


def live():
    return {"status": "ok"}


@app.get("/health/ready")


def ready():
    return {"status": "ready"}


@app.post("/v1/governance")


def handle(r: Request):
    with tracer.start_as_current_span("ai-data-governance-platform.domain"):
        try:
            a = Asset(
                r.key,
                r.payload.get("owner", ""),
                r.payload.get("classification", "internal"),
                set(r.payload.get("tags", [])),
            )
            d = evaluate(
                a,
                r.payload.get("required_classification", "internal"),
                r.payload.get("actor", ""),
            )
            return {"allowed": d.allowed, "reasons": d.reasons}
        except (ValueError, KeyError, RuntimeError) as e:
            raise HTTPException(status_code=400, detail=str(e)) from e

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MOCK_ALERTS = [
    {
        "alert_id": "ALT-001",
        "severity": "critical",
        "description": "Brute-force login attempt detected on admin account.",
        "timestamp": "2026-02-23T04:12:00Z",
        "status": "open",
    },
    {
        "alert_id": "ALT-002",
        "severity": "high",
        "description": "Unusual outbound traffic spike to unknown IP range.",
        "timestamp": "2026-02-23T06:45:00Z",
        "status": "investigating",
    },
    {
        "alert_id": "ALT-003",
        "severity": "medium",
        "description": "Expired TLS certificate on api.internal.example.com.",
        "timestamp": "2026-02-22T18:30:00Z",
        "status": "open",
    },
    {
        "alert_id": "ALT-004",
        "severity": "low",
        "description": "User account locked after 5 consecutive failed login attempts.",
        "timestamp": "2026-02-22T14:20:00Z",
        "status": "resolved",
    },
    {
        "alert_id": "ALT-005",
        "severity": "critical",
        "description": "SQL injection pattern detected in POST /api/search request body.",
        "timestamp": "2026-02-23T09:01:00Z",
        "status": "open",
    },
]


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get("/api/alerts")
def get_alerts():
    return MOCK_ALERTS

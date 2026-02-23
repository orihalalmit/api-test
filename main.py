import random
from datetime import datetime, timedelta
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

SEVERITIES = ["critical", "high", "medium", "low"]
STATUSES = ["open", "investigating", "resolved"]
DESCRIPTIONS = [
    "Brute-force login attempt detected on admin account.",
    "Unusual outbound traffic spike to unknown IP range.",
    "Expired TLS certificate on api.internal.example.com.",
    "User account locked after 5 consecutive failed login attempts.",
    "SQL injection pattern detected in POST /api/search request body.",
    "Privilege escalation attempt by non-admin user detected.",
    "Malware signature matched in uploaded file on storage service.",
    "Unauthorized API key usage from unrecognized geographic region.",
    "DDoS traffic pattern detected on public-facing load balancer.",
    "Suspicious cron job added to production server.",
    "Unencrypted PII found in application log output.",
    "SSH login from blacklisted IP address blocked.",
    "Failed multi-factor authentication attempts exceeded threshold.",
    "Configuration drift detected on firewall ruleset.",
    "Outbound connection to known C2 server IP blocked.",
]


def random_timestamp() -> str:
    offset = timedelta(hours=random.randint(0, 72))
    ts = datetime.utcnow() - offset
    return ts.strftime("%Y-%m-%dT%H:%M:%SZ")


def generate_alerts(count: int = 5) -> list:
    descriptions = random.sample(DESCRIPTIONS, count)
    return [
        {
            "alert_id": f"ALT-{str(i + 1).zfill(3)}",
            "severity": random.choice(SEVERITIES),
            "description": descriptions[i],
            "timestamp": random_timestamp(),
            "status": random.choice(STATUSES),
        }
        for i in range(count)
    ]


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get("/api/alerts")
def get_alerts():
    return generate_alerts()

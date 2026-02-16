from services.graph_service.circular_repository import CircularRepository

repo = CircularRepository()

circular_data = {
    "circular_id": "RBI/2025-26/120",
    "title": "Revised NBFC Liquidity Framework",
    "regulator": "RBI",
    "date": "2025-03-01",
    "department": "Department of Regulation",
    "regulation_type": "Amendment",
    "summary": "Revised liquidity norms for NBFCs.",
    "pdf_url": "https://rbi.org/sample3.pdf",
    "risk_score": 0,  # will calculate later
    "schema_version": "1.0"
}

repo.create_circular(circular_data)

repo.link_industries(
    circular_id="RBI/2025-26/120",
    industries=["NBFC"]
)

repo.link_deadline(
    circular_id="RBI/2025-26/120",
    deadline_data={
        "date": "2025-06-30",
        "description": "Compliance submission deadline",
        "urgency_score": 40
    }
)

repo.link_penalty(
    circular_id="RBI/2025-26/120",
    penalty_data={
        "severity_level": "High",
        "description": "Failure to comply may attract supervisory penalty",
        "penalty_weight": 50
    }
)

repo.link_amendment(
    new_id="RBI/2025-26/120",
    old_id="RBI/2025-26/99"
)

print("Full circular inserted with deadline and penalty.")

from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.mitre_technique import MitreTechnique


def seed():
    db: Session = SessionLocal()

    techniques = [
        {
            "technique_id": "T1059",
            "name": "Command and Scripting Interpreter",
            "tactic": "Execution",
            "description": "Command execution through interpreters.",
            "platform": "Linux",
        },
        {
            "technique_id": "T1078",
            "name": "Valid Accounts",
            "tactic": "Defense Evasion",
            "description": "Use of legitimate accounts.",
            "platform": "Windows",
        },
        {
            "technique_id": "T1021",
            "name": "Remote Services",
            "tactic": "Lateral Movement",
            "description": "Remote access between systems.",
            "platform": "Linux",
        },
        {
            "technique_id": "T1566",
            "name": "Phishing",
            "tactic": "Initial Access",
            "description": "Social engineering attacks.",
            "platform": "Windows",
        },
    ]

    for item in techniques:
        exists = (
            db.query(MitreTechnique)
            .filter(
                MitreTechnique.technique_id == item["technique_id"]
            )
            .first()
        )

        if not exists:
            db.add(MitreTechnique(**item))

    db.commit()

    print("MITRE ATT&CK techniques inserted.")


if __name__ == "__main__":
    seed()
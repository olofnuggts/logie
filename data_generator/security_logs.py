# security_logs.py

import json
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker()


def generate_security_log():
    now = datetime.now()
    event_types = [
        "Login Attempt",
        "Firewall Breach",
        "Unauthorized Access",
        "Data Exfiltration",
    ]
    event_type = random.choice(event_types)
    status_choices = {
        "Login Attempt": ["Successful", "Failed"],
        "Firewall Breach": ["Detected", "Blocked"],
        "Unauthorized Access": ["Detected", "Thwarted"],
        "Data Exfiltration": ["Attempted", "Executed"],
    }
    status = random.choice(status_choices[event_type])

    log = {
        "timestamp": (now - timedelta(seconds=random.randint(0, 300))).strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "log_type": "Security",
        "event_type": event_type,
        "source": fake.ipv4() if event_type != "Login Attempt" else fake.user_name(),
        "status": status,
        "description": f"{event_type} - {status}.",
    }

    # Simulating a brute force attack pattern
    if event_type == "Login Attempt" and status == "Failed":
        log[
            "description"
        ] += " Multiple failed attempts detected. Possible brute force attack."
    return log


if __name__ == "__main__":
    print(json.dumps(generate_security_log(), indent=4))

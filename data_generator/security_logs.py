# security_logs.py

import json
from faker import Faker
from datetime import datetime
import random

fake = Faker()


def generate_security_log():
    event_type = random.choice(
        ["Login Attempt", "Firewall Breach", "Unauthorized Access"]
    )
    status = random.choice(["Successful", "Failed", "Blocked"])
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "log_type": "Security",
        "event_type": event_type,
        "source": fake.ipv4() if event_type == "Firewall Breach" else fake.user_name(),
        "ip": fake.ipv4(),
        "status": status,
        "description": f"{event_type} - {status}.",
    }


if __name__ == "__main__":
    print(json.dumps(generate_security_log(), indent=4))

# application_logs.py

import json
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker()


def generate_application_log():
    now = datetime.now()
    applications = ["CRM System", "Email Client", "Project Management Tool"]
    event_types = ["User Action", "Start", "Stop", "Error"]
    user_actions = ["logged in", "logged out", "uploaded a file", "updated a setting"]
    application_name = random.choice(applications)
    event_type = random.choice(event_types)

    log = {
        "timestamp": (now - timedelta(seconds=random.randint(0, 60))).strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "log_type": "Application",
        "application_name": application_name,
        "event_type": event_type,
        "user_id": fake.user_name(),
        "description": "",
    }

    if event_type == "User Action":
        action = random.choice(user_actions)
        log["description"] = f"User '{log['user_id']}' {action} in {application_name}."
    elif event_type == "Error":
        log["description"] = f"Error occurred in {application_name}: {fake.sentence()}"
    else:
        log[
            "description"
        ] = f"Application {event_type} event occurred in {application_name}"

    return log


if __name__ == "__main__":
    print(json.dumps(generate_application_log(), indent=4))

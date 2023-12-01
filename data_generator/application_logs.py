# application_logs.py

import json
from faker import Faker
from datetime import datetime
import random

fake = Faker()


def generate_application_log():
    application_names = ["AppA", "AppB", "AppC"]
    event_type = random.choice(["Start", "Stop", "Error", "Warning"])
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "log_type": "Application",
        "application_name": random.choice(application_names),
        "event_type": event_type,
        "description": f"Application {event_type} event occurred.",
    }


if __name__ == "__main__":
    print(json.dumps(generate_application_log(), indent=4))

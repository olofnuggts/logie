# system_logs.py

import json
from faker import Faker
from datetime import datetime
import random

fake = Faker()


def generate_system_log():
    event_type = random.choice(
        ["System Start", "System Shutdown", "Hardware Change", "System Error"]
    )
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "log_type": "System",
        "event_type": event_type,
        "description": f"{event_type} event occurred.",
    }


if __name__ == "__main__":
    print(json.dumps(generate_system_log(), indent=4))

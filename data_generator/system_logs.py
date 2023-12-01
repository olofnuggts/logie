# system_logs.py

import json
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker()


def generate_system_log():
    now = datetime.now()
    event_types = [
        "System Start",
        "System Shutdown",
        "Maintenance",
        "Performance Metric",
    ]
    event_type = random.choice(event_types)

    log = {
        "timestamp": (now - timedelta(seconds=random.randint(0, 300))).strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "log_type": "System",
        "event_type": event_type,
        "system_id": fake.uuid4(),
        "description": "",
    }

    if event_type == "Performance Metric":
        metric_type = random.choice(["CPU Usage", "Memory Usage", "Disk Space"])
        log["description"] = f"{metric_type}: {random.randint(1, 100)}%"
    else:
        log["description"] = f"{event_type} event occurred."

    return log


if __name__ == "__main__":
    print(json.dumps(generate_system_log(), indent=4))

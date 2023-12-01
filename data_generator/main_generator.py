# main_generator.py

import json
from system_logs import generate_system_log
from application_logs import generate_application_log
from security_logs import generate_security_log
import random


def generate_log():
    log_generators = [
        generate_system_log,
        generate_application_log,
        generate_security_log,
    ]
    selected_generator = random.choice(log_generators)
    return selected_generator()


if __name__ == "__main__":
    for i in range(10):
        print(json.dumps(generate_log(), indent=4))

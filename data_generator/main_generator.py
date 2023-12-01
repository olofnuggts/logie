# main_generator.py

import json
from system_logs import generate_system_log
from application_logs import generate_application_log
from security_logs import generate_security_log
import random
import time


def generate_log():
    log_generators = [
        generate_system_log,
        generate_application_log,
        generate_security_log,
    ]
    selected_generator = random.choice(log_generators)
    return selected_generator()


if __name__ == "__main__":
    try:
        while True:
            log_entry = generate_log()
            print(json.dumps(log_entry, indent=4))
            time.sleep(1)  # Wait for 1 second before generating the next log
    except KeyboardInterrupt:
        print("Log generation stopped by user.")

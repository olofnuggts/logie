# import json
import time
from system_logs import generate_system_log
from application_logs import generate_application_log
from security_logs import generate_security_log
import random
from db_connector.mongodb_connector import store_log


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
            # print(json.dumps(log_entry, indent=4))
            store_log(log_entry)  # Store the log in MongoDB
            time.sleep(1)
    except KeyboardInterrupt:
        print("Log generation stopped by user.")

from db_connector.mongodb_connector import get_database
from alert_system import send_email_alert
import collections


def fetch_logs():
    db = get_database()
    collection = db["logs"]
    logs = collection.find({})
    return list(logs)


def detect_brute_force(logs):
    failed_logins = collections.defaultdict(int)
    for log in logs:
        if (
            log["log_type"] == "Security"
            and log["event_type"] == "Login Attempt"
            and log["status"] == "Failed"
        ):
            failed_logins[log["source"]] += 1

    for source, count in failed_logins.items():
        if count >= 5:  # Threshold for brute-force detection
            print(f"Potential Brute-Force attack detected from: {source}")
            alert_message = f"Potential Brute-Force attack detected from: {log}"
            send_email_alert(
                "Brute-Force Alert",
                alert_message,
                "receiver@example.com",
                "sender@example.com",
            )


def detect_port_scanning(logs, threshold=100):
    port_activity = collections.defaultdict(int)
    for log in logs:
        if log["log_type"] == "Security" and log["event_type"] == "Connection Attempt":
            port_activity[log["source"]] += 1

    for source, count in port_activity.items():
        if count > threshold:
            print(f"Potential Port-Scanning activity detected from {source}")
            alert_message = f"Potential Port-Scanning activity detected from {log}"
            send_email_alert(
                "Port-Scanning Alert",
                alert_message,
                "receiver@example.com",
                "sender@example.com",
            )


def detect_application_errors(logs, threshold=10):
    app_errors = collections.defaultdict(int)
    for log in logs:
        if log["log_type"] == "Application" and log["event_type"] == "Error":
            app_errors[log["application_name"]] += 1

    for app, count in app_errors.items():
        if count > threshold:
            print(f"Unusual error frequency detected in application {app}")
            alert_message = f"Unusual error frequency detected in application \n {log}"
            send_email_alert(
                "Application Error Alert",
                alert_message,
                "receiver@example.com",
                "sender@example.com",
            )


def analyze_logs(logs):
    detect_brute_force(logs)
    detect_port_scanning(logs)
    detect_application_errors(logs)


if __name__ == "__main__":
    logs = fetch_logs()
    analyze_logs(logs)

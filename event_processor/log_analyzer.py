from db_connector.mongodb_connector import get_database
from datetime import datetime
import numpy as np
from alert_system import send_email_alert
import collections


def fetch_logs():
    db = get_database()
    collection = db["logs"]
    logs = collection.find({})
    return list(logs)


def parse_timestamp(log_entry):
    # Assuming your timestamp is in a format like '2023-04-01T12:00:00'
    return datetime.strptime(log_entry["timestamp"], "%Y-%m-%dT%H:%M:%S")


def detect_brute_force(logs, threshold=5, time_window_seconds=300):
    failed_logins = collections.defaultdict(list)
    for log in logs:
        if (
            log["log_type"] == "Security"
            and log["event_type"] == "Login Attempt"
            and log["status"] == "Failed"
        ):
            timestamp = parse_timestamp(log)
            failed_logins[log["source"]].append(timestamp)

    for source, timestamps in failed_logins.items():
        if len(timestamps) < threshold:
            continue

        timestamps.sort()
        for i in range(len(timestamps) - threshold + 1):
            if (
                timestamps[i + threshold - 1] - timestamps[i]
            ).total_seconds() <= time_window_seconds:
                print(f"Brute-Force detected from {source}")
                alert_message = f"Brute-Force detected from {log}"
                send_email_alert(
                    "Brute-Force Alert",
                    alert_message,
                    "receiver@example.com",
                    "sender@example.com",
                )
                break


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


def detect_anomalous_cpu_usage(logs, cpu_threshold=90):
    cpu_usages = [log["cpu_usage"] for log in logs if "cpu_usage" in log]

    if not cpu_usages:
        return

    # Simple statistical approach: flag usage higher than a threshold
    mean_usage = np.mean(cpu_usages)
    for log in logs:
        if log.get("cpu_usage", 0) > mean_usage + cpu_threshold:
            print(f"High CPU usage detected: {log['cpu_usage']}%")
            alert_message = f"High CPU usage detected: {log['cpu_usage']}%"
            send_email_alert(
                "CPU Usage Alert",
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

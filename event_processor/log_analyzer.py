# log_analyzer.py

from db_connector.mongodb_connector import get_database
from alert_system import send_email_alert
import collections


def fetch_logs():
    db = get_database()
    collection = db["logs"]
    # Hier können Sie die Abfrage an Ihre spezifischen Anforderungen anpassen
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

    # Prüfen, ob die Anzahl der fehlgeschlagenen Versuche einen Schwellenwert überschreitet
    angriff_erkannt = False
    for source, count in failed_logins.items():
        if count > 5:  # Schwellenwert, zum Beispiel 5
            print(f"Potenzieller Brute-Force-Angriff erkannt von: {source}")

    #   Dieser Teil das Code, wenn eine angriff_erkannt ist
    if angriff_erkannt:
        send_email_alert(
            "Brute-Force-Alarm",
            f"Brute-Force-Angriff erkannt von {source}",
            "empfaenger@example.com",
            "absender@example.com",
            "smtp.example.com",
            587,
            "smtp_user",
            "smtp_password",
        )


def detect_port_scanning(logs, threshold=100):
    # Erkennen von Port-Scanning-Aktivitäten
    port_activity = collections.defaultdict(int)
    for log in logs:
        if log["log_type"] == "Security" and log["event_type"] == "Connection Attempt":
            port_activity[log["source"]] += 1

    for source, count in port_activity.items():
        if count > threshold:
            print(f"Potenzielle Port-Scanning-Aktivität erkannt von {source}")


def detect_application_errors(logs, threshold=10):
    # Erkennen ungewöhnlicher Anwendungsfehler
    app_errors = collections.defaultdict(int)
    for log in logs:
        if log["log_type"] == "Application" and log["event_type"] == "Error":
            app_errors[log["application_name"]] += 1

    for app, count in app_errors.items():
        if count > threshold:
            print(f"Ungewöhnliche Fehlerhäufigkeit in Anwendung {app}")


def analyze_logs(logs):
    # Ein einfacher Ansatz, um wiederholte fehlgeschlagene Login-Versuche zu identifizieren
    detect_brute_force(logs)
    detect_port_scanning(logs)
    detect_application_errors(logs)


if __name__ == "__main__":
    logs = fetch_logs()
    analyze_logs(logs)

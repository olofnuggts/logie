# anomaly_detection.py
import numpy as np
from datetime import datetime
import joblib
from db_connector.mongodb_connector import get_database


def parse_timestamp(timestamp_str):
    return datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S").timestamp()


def extract_features(log):
    timestamp = parse_timestamp(log.get("timestamp", "1970-01-01 00:00:00"))
    response_time = log.get("event_type", 0)
    request_count = log.get("system_id", 0)
    error_count = log.get("log_type", 0)
    return [timestamp, response_time, request_count, error_count]


def preprocess_logs(logs):
    return np.array([extract_features(log) for log in logs])


def detect_anomalies(preprocessed_logs):
    model = joblib.load("models\isolation_forest_model.pkl")
    predictions = model.predict(preprocessed_logs)
    anomalies = preprocessed_logs[predictions == -1]
    return anomalies


def analyze_logs():
    db = get_database()
    collection = db["logs"]
    logs = collection.find({})
    preprocessed_logs = preprocess_logs(logs)
    anomalies = detect_anomalies(preprocessed_logs)
    for anomaly in anomalies:
        print(f"Anomaly detected: {anomaly}")


if __name__ == "__main__":
    analyze_logs()

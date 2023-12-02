from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, PyMongoError


def get_database():
    CONNECTION_STRING = "mongodb://localhost:27017/"  # Update this as needed
    try:
        client = MongoClient(CONNECTION_STRING)
        # The ismaster command is cheap and does not require auth.
        client.admin.command("ismaster")
        return client["siem_logs"]
    except ConnectionFailure:
        print("Failed to connect to server.")
        return None


def store_log(log):
    db = get_database()
    if db is not None:
        try:
            collection = db["logs"]
            collection.insert_one(log)
        except PyMongoError as e:
            print(f"An error occurred while inserting the log: {e}")

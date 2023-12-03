# train_model.py
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib


def generate_synthetic_data(num_samples=1000, num_features=4):
    return np.random.rand(num_samples, num_features)


def train_isolation_forest(data):
    model = IsolationForest(n_estimators=100, contamination="auto")
    model.fit(data)
    return model


data = generate_synthetic_data()
model = train_isolation_forest(data)

joblib.dump(model, "models\isolation_forest_model.pkl")

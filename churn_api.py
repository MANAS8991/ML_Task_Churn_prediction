import pickle
import pandas as pd
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Load the model and feature columns
with open("churn_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("feature_columns.pkl", "rb") as feature_file:
    feature_columns = pickle.load(feature_file)

@app.route('/')
def home():
    return "Churn Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict churn probability for a customer.
    Expects JSON input with feature values.
    """
    try:
        # Parse input JSON
        customer_data = request.json

        # Convert input to DataFrame
        input_df = pd.DataFrame([customer_data], columns=feature_columns)

        # Predict churn probability
        churn_prob = model.predict_proba(input_df)[:, 1][0]

        # Construct response
        response = {
            "churn_probability": churn_prob,
            "churn_risk": "High" if churn_prob > 0.5 else "Low"
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

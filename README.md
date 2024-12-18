# Churn Prediction API

This API provides churn probability predictions based on customer details. It accepts customer data as JSON input and returns the likelihood of churn.

---

## Requirements

Ensure the following are installed on your system:

- **Python 3.7 or above**
- Required Python libraries:
  - `Flask`
  - `pandas`
  - `scikit-learn`
  - `joblib`

### Install Dependencies

Install the required libraries using the following command:

pip install flask pandas scikit-learn joblib


## Setup and Run the API
Clone the Repository or Save Files
Save the API code (app.py) and the saved model file (churn_model.pkl) in the same directory.
### Run the API
Open your terminal.

Navigate to the directory containing app.py and churn_model.pkl.

Start the Flask application:
python app.py
The API will run locally at: http://127.0.0.1:5000/predict.

## Test the API Locally
### Using cURL
Run the following command in your terminal:

curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "DSL",
  "OnlineSecurity": "Yes",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "No",
  "StreamingMovies": "No",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 50.85,
  "TotalCharges": 608.7
}'


## Using Postman
Open Postman and create a new POST request.

Set the URL to: http://127.0.0.1:5000/predict.

In the Body section:

Select raw.
Set the type to JSON.
Paste the following sample input:
{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "DSL",
  "OnlineSecurity": "Yes",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "No",
  "StreamingMovies": "No",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 50.85,
  "TotalCharges": 608.7
}

Click Send to get the churn prediction in the response.

## Sample API Response
The API will return a JSON response with the churn probability, similar to the example below:
{
  "churn_probability": 0.78
}

## Modify for Your Use
Update the churn_model.pkl file with your own trained model if needed.
Extend the API to include additional endpoints or features as per your requirements.

## Stopping the Server
To stop the server, press CTRL + C in the terminal where the Flask app is running.

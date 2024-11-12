# frontend/app.py
import streamlit as st
import requests
from PIL import Image

# Set up the backend API URL (localhost should change to the server's IP address)
API_URL = 'http://localhost:5000/predict'

def set_page_config():
    """Sets the Streamlit page configuration."""
    st.set_page_config(page_title="Enhanced Decision Tree Prediction Demo", layout="centered")

def display_header():
    """Displays the header and introductory text."""
    st.title("🌳 Enhanced Decision Tree Classifier")
    st.write("Predict the class of a sample using a trained Decision Tree model. Adjust the input values and click 'Predict'.")

def display_input_form():
    """Displays the form for user input."""
    with st.form("prediction_form"):
        feature_1 = st.number_input("Feature 1 (e.g., sepal length)", min_value=0.0, max_value=10.0, step=0.1, help="Enter a numeric value")
        feature_2 = st.number_input("Feature 2 (e.g., sepal width)", min_value=0.0, max_value=10.0, step=0.1, help="Enter a numeric value")
        feature_3 = st.number_input("Feature 3 (e.g., petal length)", min_value=0.0, max_value=10.0, step=0.1, help="Enter a numeric value")
        feature_4 = st.number_input("Feature 4 (e.g., petal width)", min_value=0.0, max_value=10.0, step=0.1, help="Enter a numeric value")
        
        submit_button = st.form_submit_button("Predict")
    return submit_button, feature_1, feature_2, feature_3, feature_4

def make_prediction(features):
    """Makes a prediction by sending the features to the backend API."""
    try:
        response = requests.post(API_URL, json={"data": features})
        prediction = response.json()["prediction"]
        return prediction
    except requests.exceptions.RequestException:
        return None

def main():
    """Main function to run the Streamlit app."""
    set_page_config()
    display_header()
    
    # Input form for features
    submit_button, feature_1, feature_2, feature_3, feature_4 = display_input_form()

    # Handle prediction
    if submit_button:
        if any(val is None for val in [feature_1, feature_2, feature_3, feature_4]):
            st.error("Please fill in all features to get a prediction.")
        else:
            with st.spinner("Fetching prediction..."):
                features = [feature_1, feature_2, feature_3, feature_4]
                prediction = make_prediction(features)
                if prediction is not None:
                    st.success(f"The predicted class is: {prediction}")
                else:
                    st.error("Error connecting to the backend. Please try again later.")

if __name__ == "__main__":
    main()
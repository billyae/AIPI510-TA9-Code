from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load pretrained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Create a Flask app
app = Flask(__name__)

# Define a route for the prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
    data = np.array(data).reshape(1, -1)
    prediction = model.predict(data)
    return jsonify({"prediction": int(prediction[0])})

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
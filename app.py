from flask import Flask, render_template, request, jsonify
from utils import model_predict
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    review = request.form.get('content')
    prediction = model_predict(review)
    return render_template("index.html", prediction=prediction, review=review)

# Create an API endpoint
@app.route('/api/predict', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)  # Get data posted as a json
    review = data['content']
    prediction = model_predict()
    return jsonify({'prediction': prediction, 'review': review})  # Return prediction

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
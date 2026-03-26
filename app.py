from flask import Flask, request, render_template
import pickle
import numpy as np

# Load trained model
with open("data.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():
    prediction = None

    if request.method == "POST":
        try:
            # Get form inputs
            open_price = float(request.form["open_price"])
            high_price = float(request.form["high_price"])
            low_price = float(request.form["low_price"])
            volume = float(request.form["volume"])
            year = int(request.form["year"])
            month = int(request.form["month"])
            day = int(request.form["day"])

            # Prepare input for model
            data = np.array([[open_price, high_price, low_price, volume, year, month, day]])

            # Predict
            result = model.predict(data)[0]

            prediction = f"Predicted Price: ₹ {result:.2f}"

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
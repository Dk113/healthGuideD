import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=["POST"])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    if prediction == 0:
        output = "Extremely Weak. For health guide please go to the above relative page."
    elif prediction == 1:
        output = "Weak"
    elif prediction == 2:
        output = "Normal"
    elif prediction == 3:
        output = "Overweight"
    elif prediction == 4:
        output = "Obesity. For health guide please go to the above relative page."
    elif prediction == 5:
        output = "Extreme Obesity. For health guide please go to the above relative page."
    return render_template("index.html", prediction_text = output)


if __name__ == "__main__":
    app.run(port = 5000, debug=True)

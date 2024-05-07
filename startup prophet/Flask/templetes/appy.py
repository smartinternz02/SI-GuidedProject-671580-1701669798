from flask import Flask, request, render_template
from sklearn.ensemble import RandomForestClassifier
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the pre-trained RandomForestClassifier model
with open("Randf.pk1", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/inner-page.html')
def inner_page():
    return render_template("inner-page.html")

@app.route('/submit', methods=["POST", "GET"])
def submit():
    # Retrieve input features from the form
    input_feature = [float(x) for x in request.form.values()]
    
    # Assuming the order of input features matches the order used during training
    names = ['labels','closed_at', 'relationships', 'milestones', 'is_top500',
             'age_last_milestone_year', 'has_roundB', 'funding_rounds', 
             'avg_participants', 'has_roundA']
    # Create a DataFrame with the input features
    data = pd.DataFrame([input_feature], columns=names)
    
    # Make predictions using the pre-trained model
    predictions = model.predict(data)
    
    # Interpret predictions and render appropriate template
    if predictions == 1:
        return render_template("inner-page.html", predict="Success")
    else:
        return render_template("inner-page.html", predict="Closed")

if __name__ == "__main__":
    app.run(debug=True, port=2222)


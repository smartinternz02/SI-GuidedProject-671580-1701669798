from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()
import pickle
pickle.dump(rf,open("Randf.pk1","wb"))

from flask import Flask,request,render_template
import pickle
import numpy as np
import pandas as pd

app=Flask(__name__)
model = pickle.load(open("Randf.pk1","rb"))

@app.route('/')
def index():
    app = Flask(__name__, template_folder='templates')

    return render_template("index.html")

@app.route('/submit', methods=["POST", "GET"])# route to show the predictions in a web UI

def submit():

    # reading the inputs given by the user
    input_feature=[float(x) for x in request.form.values()]
   
    # input_feature =np.transpose(input_feature)

    x=[np.array(input_feature)]

    print(input_feature)

    names = ["is_ecommerce","is_otherstate", "has_VC", "has_angel", "has_roundA", "has_roundB","has_roundC","has_roundD","state_code"]

    data = pd.DataFrame(x,columns=names)

    print(data)

    pred =  model.predict(data)

    if (pred == 1):

        return render_template("inner-page.html", predict = "Success")

    else:

        return render_template("inner-page.html", predict =  "Closed")

if __name__=="__main__":
 
    app.run( debug=True,port=2222)
#Import Libraries
import numpy as np
from flask import Flask, render_template, request
import pickle 

#Initialize the flask app
app = Flask(__name__)

#open the pickle file in the read mode
clf = pickle.load(open('liverdisease_svc_kernel.pkl', 'rb'))

#define app route for the default page. i.e. root node for the API url
#whenever a user visits our app domain, at the given route, execute the home() function
@app.route("/")
def home():
    return render_template('index.html')

#To use the predict button in our webapp, create another API for the prediction part
@app.route("/predict", methods=['POST'])
def predict():
    #function for rendering results on HTML GUI
    #request.form.values is used to get the data inputted into our form by the user on our html page when the user clicks the predict button
    int_features = [float(i) for i in request.form.values()] #getting the inputs, convert to float, and storing them in a list
    final_features = np.array(int_features)  #converting the list to an array
    final_features = final_features.reshape(-1, len(final_features)) #reshaping the array into a 2D array
    prediction = clf.predict(final_features)    #making predictions on our new test data

    output = prediction

    if output == 1:
        return render_template('index.html', prediction_text = 'This patient has liver disease')

    elif output == 2:
        return render_template('index.html', prediction_text = 'This patient does not have liver disease')


#app.run is called, and the webapp is hosted locally
if __name__ == "__main__":
    app.debug = True
    app.run()     #debug=True, makes sure everytime we make a change in our code, it is reflected in our webapp auto..
    

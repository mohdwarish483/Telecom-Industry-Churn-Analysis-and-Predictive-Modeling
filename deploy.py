from flask import Flask, render_template, request
import pickle
app = Flask(__name__)
# load the model
model = pickle.load(open('modellCPS.sav', 'rb'))
@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'gender_Male','SeniorCitizen_1',
                'Partner_Yes', 'Dependents_Yes', 'PhoneService_Yes',
       'MultipleLines_No phone service', 'MultipleLines_Yes',
       'InternetService_Fiber optic', 'InternetService_No',
       'OnlineSecurity_No internet service', 'OnlineSecurity_Yes',
       'OnlineBackup_No internet service', 'OnlineBackup_Yes',
       'DeviceProtection_No internet service', 'DeviceProtection_Yes',
       'TechSupport_No internet service', 'TechSupport_Yes',
       'StreamingTV_No internet service', 'StreamingTV_Yes',
       'StreamingMovies_No internet service', 'StreamingMovies_Yes',
       'Contract_One year', 'Contract_Two year', 'PaperlessBilling_Yes',
       'PaymentMethod_Credit card', 'PaymentMethod_Electronic check',
       'PaymentMethod_Mailed check']
    input_values = [request.form[feature] for feature in features]

    input_values = list(map(int, input_values)) 
    result = model.predict([input_values])[0]
    return render_template('index.html', result=result)
if __name__ == '__main__':
    app.run(debug=True)
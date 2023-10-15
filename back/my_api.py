
import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi import FastAPI
import uvicorn
import  pickle
import json
# Create the app
app = FastAPI()

# Load trained Pipeline

with open(r"C:\Users\ESIEE-IT\Desktop\Crime\back\model3.pkl", "rb") as f:
    model = pickle.load(f)


# Define predict function
@app.get('/predict')
def predict(Heure, Day, Year, DayOfWeek, PdDistrict,X:float,Y:float):
    
    HARM = float(0.5/((1/X)+(1/Y)))
    data = pd.DataFrame([[Heure,Day,Year,DayOfWeek,PdDistrict, X,Y,HARM]])
    data.columns = [["Heure","Day","Year","DayOfWeek","PdDistrict", "X","Y","HARM"]]
    predictions = model.predict(data) 
    return {'prediction': predictions.tolist()}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)



'''
    
import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi import FastAPI
import uvicorn
import  pickle
import json
# Create the app
app = FastAPI()

# Load trained Pipeline

with open("model.pkl", "rb") as f:
    model = pickle.load(f)


# Define predict function
@app.get('/predict')
def predict( PdDistrict, Mois, Heure, NumJour, X,Y):
    data = pd.DataFrame([[ PdDistrict, Mois, Heure, NumJour, X, Y]])
    data.columns = [[ "PdDistrict", "Mois", "Heure", "NumJour", "X", "Y"]]
    predictions = model.predict(data) 
    return {'prediction': predictions.tolist()}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

    '''
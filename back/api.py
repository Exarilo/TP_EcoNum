from flask import Flask
from flask import request
from flask import Flask, jsonify
from numba import jit
from flask import Flask, request, jsonify
from flask_cors import CORS
#from codecarbon import EmissionsTracker

app = Flask(__name__)
CORS(app)  
isFirsTime=True

@app.route('/temp', methods=['GET'])
def login():
    global isFirsTime 
    global tc 
    windspeed = float(request.args.get('ws'))
    tempambiante = float(request.args.get('ta'))
    intensite = float(request.args.get('i'))


    if(isFirsTime==True):
        isFirsTime =False
        tc=tempambiante
    x, y = calcul(windspeed,tempambiante,tc,1800*1000,intensite)
    tc=y[-1]


    tempcable = {'temp-cable': y}

    return jsonify(tempcable)

@jit(nopython=True)
def calcul(ws, ta, tp, T, I,dt = 1):
   # tracker = EmissionsTracker()
   # tracker.start()
    x=[]
    y=[]
    x.append(0)
    y.append(tp)
    for i in range(T):
        tp= dt/60/1000*((-(ws*ws)/1600)* 0.4-0.1)*(tp-ta -(I**1.4 * 130/73785 ) )+tp
        if(i%1000 ==0):
            x.append(i)
            y.append(tp)
   # emissions: float = tracker.stop()
    return x, y
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8000)

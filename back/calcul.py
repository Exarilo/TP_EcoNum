import matplotlib.pyplot as plt
from numba import jit

windspeed=1.2
Ta=15.0
Tc=Ta

#avec T en seconde
@jit(nopython=True)
def calcul(ws, ta, tp, T, I,dt = 1):

    x=[]
    y=[]
    x.append(0)
    y.append(tp)
    for i in range(T):
        
        tp= dt/60/1000*((-(ws*ws)/1600)* 0.4-0.1)*(tp-ta -(I**1.4 * 130/73785 ) )+tp
        if(i%1000 ==0):
            x.append(i)
            y.append(tp)
    
    return x, y, tp



x, y,res = calcul(windspeed,Ta,Tc,1800*1000,500)
plt.scatter(x,y)
plt.title('Nuage de points : suite arithmétique')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



calcul(windspeed,Ta,Tc,180000,500)

import numpy as np
def toCelsius( f ) :
    return 5*(f-32)/9
def BMI( wh ) :
    return wh[::,0]/(wh[::,1]/100)**2
def distanceTo( p, Poins) :
    return np.array([(((int(x)-p[0])**2)+((int(y)-p[1])**2))**0.5 for x,y in Poins]) 

#exec(input().strip())
print(toCelsius(np.array([32,212])))
print(BMI(np.array([[60,170],[50,160]])))
print(distanceTo([0,0],np.array([[3,0],[0,4],[3,4]]))) 
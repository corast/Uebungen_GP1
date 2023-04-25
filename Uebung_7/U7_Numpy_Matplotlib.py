import matplotlib.pyplot as plt
import numpy as np

#Aufgabe 1

x = np.random.uniform(-100, 100, 1000)
y = np.random.uniform(-100, 100, 1000)
colors = np.random.rand(1000)

plt.scatter(x,y,c=colors)
plt.show()


#-------------------------------------------
#Aufgabe 2

def f(x,y):
    return(np.exp(-x**2))*np.sin(y)

x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)

X, Y = np.meshgrid(x, y)
Z = f(X,Y)

plt.pcolormesh(X, Y, Z) 
plt.show() 
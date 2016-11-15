'''/*******************************************************************************
 *  @file    animation.cpp
 *  @author  Benjamin GALLOIS
 *  @date    18/11/2016
 *  @version 1.0
 *  @resume
*******************************************************************************/'''



import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np


#extraction des donnees

marcheur = 500
radius = 2.
data = np.loadtxt("marcheur.txt")
x=np.zeros(((int(len(data[:,0])/marcheur)),marcheur))
y=np.zeros(((int(len(data[:,0])/marcheur)),marcheur))

for i in range(len(data[:,0])+1):
	for j in range(marcheur):
		if i < len(data[:,0])/marcheur:
			x[i,j]=data[marcheur*i+j,0]
			y[i,j]=data[marcheur*i+j,1]






#initialisation de la figure

fig = plt.figure(2)
ax = plt.axes(xlim=(-radius, radius), ylim=(-radius, radius),aspect='equal')
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
circle1 = plt.Circle((0, 0), radius, color='b',fill=False)
ax = plt.gca()
ax.add_artist(circle1)
line, = ax.plot([], [], '.', ms=5)



#animation du graphique

def animate(i):
    pas = str(i-1)
    line.set_data(x[i-1,:], y[i-1,:])
    time_text.set_text('Pas : ' + pas)
    return line, time_text,





#trace de l'animation

<<<<<<< HEAD
ani = animation.FuncAnimation(fig, animate, frames=len(x[:,0]), interval=400, blit=False , repeat=True)
=======
ani = animation.FuncAnimation(fig, animate, frames=len(x[:,0]), interval=200, blit=True, repeat=True)
>>>>>>> e857a65d290e549a11474e3d4a6a2ccaaec91bcc
legend_nbmarcheurs = "Nombre de bacteries : " + str(marcheur) + "\n"
legend_nbpas = "Nombre de pas : " + str(len(x[:,0])+1)
plt.title(legend_nbmarcheurs + legend_nbpas)
plt.show()

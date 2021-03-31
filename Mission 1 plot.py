# This example script demonstrates how to use Python to fly Tello in a box mission
# This script is part of our course on Tello drone programming
# https://learn.droneblocks.io/p/tello-drone-programming-with-python/

# Import the necessary modules
import socket
import threading
import time
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

#Set up 3 axies chart
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#XYZ data to be graphed
X=[0,0,25,25,0,0,  -25,-25,0,0,  40,90,130,0]
Y=[0,0,40,130,90,0,  -40,-130,-90,0,  25,25,0,0]
Z=[0,20,20,20,20,20,  20,20,20,20,  20,20,20,20]

#Make 3D plot of origonal XYZ data
ax.plot3D(X,Y,Z,'*-')

#Show 3d plot
plt.show()


#def makePedals ();
#    curve(64,102,0,0,229,0,60);
#    curve(-64,-102,0,0,-229,0,60);
    
#    curve(64,-102,0,0,-229,0,60);
#    curve(-64,102,0,0,229,0,60); 
#    curve(102,64,0,229,0,0,60);
#    curve(-102,-64,0,-229,0,0,60);
#    curve(-102,-64,0,-229,0,0,60);
#    curve(102,64,0,229,0,0,60);

def waypointA():
    send("stop" + str(5))

def waypointB():
    send("streamon")
    send("cw" + str(360),5)
    send("streamoff")

def waypointC():
    send("flip" + str(f),5)
    send("flip" + str(b),5)

def waypointD():
    radius = 10
    photo_count = 20
    angle_increment = 360 + photo_count
    x1 = radius
    y1 = 0
    x2 = cos(angle_increment)*radius
    y2 = sin(angle_increment)*radius 
    distance = ((x2-x1)**2+(y2-y1)**2)**(1/2)
    send("forward" + str(radius),5)
    send("cw" + str(180),5)
    time = 1
    while time < photo_count:
        send("stop"+ str(1))
        send("ccw" + str(angle_increment),5)
        send("right" + str(distance),5)
        time = time + 1






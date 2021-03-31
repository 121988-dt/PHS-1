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

# Put Tello into command mode
send("command", 5)

# Send the takeoff command
send("takeoff", 5)
send("stop", 5)

#def makePedals ():
    curve(64,102,0,0,229,0,60);
    curve(-64,-102,0,0,-229,0,60);
    
    curve(64,-102,0,0,-229,0,60);
    curve(-64,102,0,0,229,0,60); 
    curve(102,64,0,229,0,0,60);
    curve(-102,-64,0,-229,0,0,60);
    curve(-102,-64,0,-229,0,0,60);
    curve(102,64,0,229,0,0,60);
    
#def finishProgram ():
    right(12)
    curve(15,15,0,0,25,0,60)
    curve(-15,-15,0,0,-25,0,60)
    left(12)
    flip("r")
    up(20)
    flip("l")
    down(20)
    flip("f")
    up(20)
    flip("b")

# Land
send("land", 5)

# Print message
print("Mission completed successfully!")

# Close the socket
sock.close()



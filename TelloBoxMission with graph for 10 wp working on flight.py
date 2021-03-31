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

class Waypoint:
    """ A simple class that contains waypoint information """


    def __init__(self, x,y,z,wp_type):
        self.x = x
        self.y = y
        self.z = z
        self.wptype = wp_type

    def getX(self):
        return self.x 
    def getY(self):
        return self.y 
    def getZ(self):
        return self.z
    def getWPType(self):
        return self.wptype

    def setX(self,new_x):
        self.x = new_x
        return
    def setY(self,new_y):
        self.y = new_y
        return
    def setZ(self,new_z):
        self.z = new_z
        return
    def setType(self,new_type):
        self.wptype = new_type
        return    

#sample waypoint list of 10 waypoints
waypoint1 = Waypoint(30, 30, 40, 'A')
waypoint2 = Waypoint(0, -20, 40, 'B')
waypoint3 = Waypoint(10, 10, 40, 'C')
waypoint4 = Waypoint(0, -20, 20, 'D')
waypoint5 = Waypoint(20, 10, 20, 'A')
waypoint6 = Waypoint(10, 90, 40, 'B')
waypoint7 = Waypoint(40, 80, 40, 'C')
waypoint8 = Waypoint(30, 30, 40, 'D')
waypoint9 = Waypoint(50, 40, 70, 'A')
waypoint10 = Waypoint(0, 50, 60, 'B')

#wpList = [waypoint1]
#wpList = [waypoint1, waypoint2]
#wpList = [waypoint1, waypoint2, waypoint3]
#wpList = [waypoint1, waypoint2, waypoint3, waypoint4]
#wpList = [waypoint1, waypoint2, waypoint3, waypoint4, waypoint5]
#wpList = [waypoint1, waypoint2, waypoint3, waypoint4, waypoint5, waypoint6]
#wpList = [waypoint1, waypoint2, waypoint3, waypoint4, waypoint5, waypoint6, waypoint7]
#wpList = [waypoint1, waypoint2, waypoint3, waypoint4, waypoint5, waypoint6, waypoint7, waypoint8]
#wpList = [waypoint1, waypoint2, waypoint3, waypoint4, waypoint5, waypoint6, waypoint7, waypoint8, waypoint9]
wpList = [waypoint1, waypoint2, waypoint3, waypoint4, waypoint5, waypoint6, waypoint7, waypoint8, waypoint9, waypoint10]

###################Waypoint Legnth We will need to use this value tell us how many points go in our arrey
numberofwaypoints = len(wpList)
print('Number of Waypoints Read')
print(numberofwaypoints)
#x values for waypoints in order 0 is take off location if statments depending on how many waypoints are posted
x0 = 0
if numberofwaypoints >= 1:
    x1 = waypoint1.getX()
if numberofwaypoints >= 2:
    x2 = waypoint2.getX()
if numberofwaypoints >= 3:
    x3 = waypoint3.getX()
if numberofwaypoints >= 4:
    x4 = waypoint4.getX()
if numberofwaypoints >= 5:
    x5 = waypoint5.getX()
if numberofwaypoints >= 6:
    x6 = waypoint6.getX()
if numberofwaypoints >= 7:
    x7 = waypoint7.getX()
if numberofwaypoints >= 8:
    x8 = waypoint8.getX()
if numberofwaypoints >= 9:
    x9 = waypoint9.getX()
if numberofwaypoints >= 10:
    x10 = waypoint10.getX()
#Y values for waypoints in order 0 is take off location if statments depending on how many waypoints are posted
y0 = 0
if numberofwaypoints >= 1:
    y1 = waypoint1.getY()
if numberofwaypoints >= 2:
    y2 = waypoint2.getY()
if numberofwaypoints >= 3:
    y3 = waypoint3.getY()
if numberofwaypoints >= 4:
    y4 = waypoint4.getY()
if numberofwaypoints >= 5:
    y5 = waypoint5.getY()
if numberofwaypoints >= 6:
    y6 = waypoint6.getY()
if numberofwaypoints >= 7:
    y7 = waypoint7.getY()
if numberofwaypoints >= 8:
    y8 = waypoint8.getY()
if numberofwaypoints >= 9:
    y9 = waypoint9.getY()
if numberofwaypoints >= 10:
    y10 = waypoint10.getY()
#Z values for waypoints in order 0 is take off location if statments depending on how many waypoints are posted 
z0 = 20
if numberofwaypoints >= 1:
    z1 = waypoint1.getZ()
if numberofwaypoints >= 2:
    z2 = waypoint2.getZ()
if numberofwaypoints >= 3:
    z3 = waypoint3.getZ()
if numberofwaypoints >= 4:
    z4 = waypoint4.getZ()
if numberofwaypoints >= 5:
    z5 = waypoint5.getZ()
if numberofwaypoints >= 6:
    z6 = waypoint6.getZ()
if numberofwaypoints >= 7:
    z7 = waypoint7.getZ()
if numberofwaypoints >= 8:
    z8 = waypoint8.getZ()
if numberofwaypoints >= 9:
    z9 = waypoint9.getZ()
if numberofwaypoints >= 10:
    z10 = waypoint10.getZ()
#Waypoint Type values for waypoints in order 0 is take off location if statments depending on how many waypoints are posted
wp0 = 'O'
if numberofwaypoints >= 1:
    wp1 = waypoint1.getWPType()
if numberofwaypoints >= 2:
    wp2 = waypoint2.getWPType()
if numberofwaypoints >= 3:
    wp3 = waypoint3.getWPType()
if numberofwaypoints >= 4:
    wp4 = waypoint4.getWPType()
if numberofwaypoints >= 5:
    wp5 = waypoint5.getWPType()
if numberofwaypoints >= 6:
    wp6 = waypoint6.getWPType()
if numberofwaypoints >= 7:
    wp7 = waypoint7.getWPType()
if numberofwaypoints >= 8:
    wp8 = waypoint8.getWPType()
if numberofwaypoints >= 9:
    wp9 = waypoint9.getWPType()
if numberofwaypoints >= 10:
    wp10 = waypoint10.getWPType()

#Set up 3 axies chart
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#X, Y and Z data points for plot if else statments to plot based on how many points there are

print('Number of Waypoints Confirmed')

if numberofwaypoints == 1:
    X=[x0,x1]
    Y=[y0,y1]
    Z=[z0,z1]
    WP = [wp0,wp1]
    print(1)
elif numberofwaypoints == 2:
    X=[x0,x1,x2]
    Y=[y0,y1,y2]
    Z=[z0,z1,z2]
    WP = [wp0,wp1,wp2]
    print(2)
elif numberofwaypoints == 3:
    X=[x0,x1,x2,x3]
    Y=[y0,y1,y2,y3]
    Z=[z0,z1,z2,z3]
    WP = [wp0,wp1,wp2,wp3]
    print(3)
elif numberofwaypoints == 4:
    X=[x0,x1,x2,x3,x4]
    Y=[y0,y1,y2,y3,y4]
    Z=[z0,z1,z2,z3,z4]
    WP = [wp0,wp1,wp2,wp3,wp4]
    print(4)
elif numberofwaypoints == 5:
    X=[x0,x1,x2,x3,x4,x5]
    Y=[y0,y1,y2,y3,y4,y5]
    Z=[z0,z1,z2,z3,z4,z5]
    WP = [wp0,wp1,wp2,wp3,wp4,wp5]
    print(5)
elif numberofwaypoints == 6:
    X=[x0,x1,x2,x3,x4,x5,x6]
    Y=[y0,y1,y2,y3,y4,y5,y6]
    Z=[z0,z1,z2,z3,z4,z5,z6]
    WP = [wp0,wp1,wp2,wp3,wp4,wp5,wp6]
    print(6)
elif numberofwaypoints == 7:
    X=[x0,x1,x2,x3,x4,x5,x6,x7]
    Y=[y0,y1,y2,y3,y4,y5,y6,y7]
    Z=[z0,z1,z2,z3,z4,z5,z6,z7]
    WP = [wp0,wp1,wp2,wp3,wp4,wp5,wp6,wp7]
    print(7)
elif numberofwaypoints == 8:
    X=[x0,x1,x2,x3,x4,x5,x6,x7,x8]
    Y=[y0,y1,y2,y3,y4,y5,y6,y7,y8]
    Z=[z0,z1,z2,z3,z4,z5,z6,z7,z8]
    WP = [wp0,wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8]
    print(8)
elif numberofwaypoints == 9:
    X=[x0,x1,x2,x3,x4,x5,x6,x7,x8,x9]
    Y=[y0,y1,y2,y3,y4,y5,y6,y7,y8,y9]
    Z=[z0,z1,z2,z3,z4,z5,z6,z7,z8,z9]
    WP = [wp0,wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8,wp9]
    print(9)
elif numberofwaypoints == 10:
    X=[x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
    Y=[y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10]
    Z=[z0,z1,z2,z3,z4,z5,z6,z7,z8,z9,z10]
    WP = [wp0,wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8,wp9,wp10]
    print(10)
#Print list of Waypoints
print('X')
print(X)
print('Y')
print(Y)
print('Z')
print(Z)
print('WP Type')
print(WP)

#Trying to merge code here
origin = (x0, y0, z0, wp0) #This is the origin points above from where ever they come from in a list thing
points = zip(X, Y, Z,WP) # converting values to print as list, stays in same order but not a list
points = list(points) # turns zipped thing into sortable list
ordered = [] #Gives an empty set, origin inside adds the origin back to the list of points so we can start at the origin
current_point = (x0, y0, z0, wp0)

while len(points) > 0:
   min_distance = float('inf')
   x0, y0, z0, wp0 = current_point
   for (x, y, z, WP) in points:
       distance = ((x - x0) ** 2 + (y - y0) ** 2 + (z - z0) ** 2) ** (1 / 2)  # compute distance

       if distance < min_distance:
           min_distance = distance
           closest = (x, y, z, WP)

   ordered.append(closest)
   points.remove(closest)
   current_point = closest
ordered.append(origin) #Appends the origin to the end of the list so the drone returns home
#print(ordered) #Prints out the value for the ordered list of points to go to.

test_list = ordered
#print("Original list is : " + str(test_list)) # Printing original list
res = list(zip(*test_list)) # Using zip() and * operator to perform Unzipping
#print("Modified list is : " + str(res)) # Printing modified list
XXX = res[0] #These 3 lines get the X, Y, X values from the ordered system
YYY = res[1]
ZZZ = res[2]
WPP = res[3]
print('Optamize WP order')
print('XXX')
print(XXX) #Prints the values so you can see the X, Y, Z, Waypoints in the optimized order
print('YYY')
print(YYY)
print('ZZZ')
print(ZZZ)
print('WP Type')
print(WPP)

#Make 3D plot of origonal XYZ data
#ax.plot3D(X,Y,Z,'*-')

#Modifyied order of plot
ax.plot3D(XXX,YYY,ZZZ,'*-')

#Show 3d plot
plt.show()

# IP and port of Tello
tello_address = ('192.168.10.1', 8889)

# IP and port of local computer
local_address = ('', 9000)

# Create a UDP connection that we'll send the command to
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the local address and port
sock.bind(local_address)

# Send the message to Tello and allow for a delay in seconds
def send(message, delay):
  # Try to send the message otherwise print the exception
  try:
    sock.sendto(message.encode(), tello_address)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))

  # Delay for a user-defined period of time
  time.sleep(delay)

# Receive the message from Tello
def receive():
  # Continuously loop and listen for incoming messages
  while True:
    # Try to receive the message otherwise print the exception
    try:
      response, ip_address = sock.recvfrom(128)
      print("Received message: " + response.decode(encoding='utf-8'))
    except Exception as e:
      # If there's an error close the socket and break out of the loop
      sock.close()
      print("Error receiving: " + str(e))
      break

# Create and start a listening thread that runs in the background
# This utilizes our receive functions and will continuously monitor for incoming messages
receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()

# Put Tello into command mode
send("command", 5)

# Send the takeoff command
send("takeoff", 5)
send("stop", 5)

#Works great when i type in values for the x y z
send("go 30 30 30 50", 5)

#cannot get this to work with variables
send("go " + str(x1) + str(x2) + str(x3), 50, 5)

send("go 30 30 30 50", 5)
send("curve 25, -25, 0, 25, -75, 0, 20", 7)
send("curve 100, 100, 0, 200, 0, 0, 20", 7)


# Land
send("land", 5)

# Print message
print("Mission completed successfully!")

# Close the socket
sock.close()

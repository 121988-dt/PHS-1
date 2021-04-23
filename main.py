# Taken and adapter from https://github.com/dbaldwin/DroneBlocks-Tello-Python/blob/master/lesson4-box-mission/TelloBoxMission.ipynb
# This example script demonstrates how use Python to fly Tello in a box mission
# This script is part of our course on Tello drone programming
# https://learn.droneblocks.io/p/tello-drone-programming-with-python/

# Import the necessary modules
import socket
import threading
import time
import matplotlib.pyplot as plt
from Code.waypoint_class import Waypoint

# EDIT HERE
def main_function(waypoints, sock):
    # Insert your functions here. If you want to import additional functions that you've created, feel free to do so. However, make sure the
    # file paths still
    # This example script demonstrates how to use Python to fly Tello in a box mission
    # This script is part of our course on Tello drone programming
    # https://learn.droneblocks.io/p/tello-drone-programming-with-python/

    # Sets delay value after certain commands are sent to tello
    delay = 0

    # Run Mission A
    mission_A(delay)

    # Run mission B
    mission_B(waypoints, delay)

    return

def mission_A(delay):
    # Set up 3d chart
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # XYZ data to be graphed
    X = [0, 0, -25, -25, 0, 0, 25, 25, 0, 0, 40, 130, 90, 0, -40, -130, -90, 0, 0, 15, 15, 0, 0, 0, 0, 0, 0, 0]
    Y = [0, 0, 40, 130, 90, 0, -40, -130, -90, 0, 25, 25, 0, 0, -25, -25, 0, 0, -12.5, 2.5, 27.5, 12.5, -12.5, 0, 0, 0, 0, 0]
    Z = [0, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 40, 20, 40, 0]

    # Make 3D plot of origonal XYZ data
    ax.plot3D(X, Y, Z, '*-')

    # Show 3d plot
    plt.show()

    # Put Tello into command mode
    send("command", delay)

    # Send the takeoff command
    send("takeoff", delay)

    # Fly in 4 leaf clover
    send(
        "curve " + str(25) + " " + str(40) + " " + str(0) + " " + str(0) + " " + str(90) + " " + str(0) + " " + str(60),
        delay)
    send("curve " + str(-25) + " " + str(-40) + " " + str(0) + " " + str(0) + " " + str(-90) + " " + str(0) + " " + str(
        60), delay)
    send("curve " + str(25) + " " + str(-40) + " " + str(0) + " " + str(0) + " " + str(90) + " " + str(0) + " " + str(
        60), delay)
    send("curve " + str(-25) + " " + str(40) + " " + str(0) + " " + str(0) + " " + str(90) + " " + str(0) + " " + str(
        60), delay)
    send(
        "curve " + str(40) + " " + str(25) + " " + str(0) + " " + str(90) + " " + str(0) + " " + str(0) + " " + str(60),
        5)
    send("curve " + str(-40) + " " + str(-25) + " " + str(0) + " " + str(-90) + " " + str(0) + " " + str(0) + " " + str(
        60), delay)
    send("curve " + str(-40) + " " + str(-25) + " " + str(0) + " " + str(-90) + " " + str(0) + " " + str(0) + " " + str(
        60), delay)
    send(
        "curve " + str(40) + " " + str(25) + " " + str(0) + " " + str(90) + " " + str(0) + " " + str(0) + " " + str(60), delay)

    # Make 4 leaf clover into a flower
    send("right " + str(12.5), delay)
    send(
        "curve " + str(15) + " " + str(15) + " " + str(0) + " " + str(0) + " " + str(25) + " " + str(0) + " " + str(60), delay)
    send("curve " + str(-15) + " " + str(-15) + " " + str(0) + " " + str(0) + " " + str(-25) + " " + str(0) + " " + str(
        60), delay)
    send("left " + str(12.5), delay)
    send("flip " + str("r"), delay)
    send("up " + str(20), delay)
    send("flip " + str("l"), delay)
    send("down " + str(20), delay)
    send("flip " + str("f"), delay)
    send("up " + str(20), delay)
    send("flip " + str("b"), delay)

    # Land
    send("land", delay)

    # Print message
    print("Mission completed successfully!")

    return


def mission_B(waypoints, delay):

    def waypointA():
        send("stop", delay)

    def waypointB():
        send("streamon", delay)
        send("cw " + str(360), delay)
        send("streamoff", delay)

    def waypointC():
        send("flip " + str('f'), delay)
        send("flip " + str('b'), delay)

    def waypointD():
        radius = 78.74  # 2 meters converted into inches
        photo_count = 12  # Break circle up into a 12 sided hexagon
        send("forward " + str(radius), delay)  # Fly 2 meters away from waypoint
        send("cw " + str(180), delay)  # face camera towards waypoint
        send("streamon", delay)  # Turn on camera
        send("right " + str(20.3795), delay)  # Fly right 1/2 of a side of the hexagon
        time = 1
        while time < photo_count:  # turn and rotate around waypoint with cemera facing waypoint
            send("ccw " + str(30), delay)
            send("right " + str(40.759), delay)
            time = time + 1
        send("ccw " + str(30), delay)
        send("right " + str(20.3795), delay)  # Fly back to where circle started
        send("streamoff", delay)  # Turn off camera
        send("forward " + str(radius), delay)  # Fly back to waypoint
        send("cw " + str(180), delay)  # Turn back around

    # Waypoint Legnth We will need to use this value tell us how many points go in our arrey
    numberofwaypoints = len(waypoints)
    print(numberofwaypoints)
    # x values for waypoints in order 0 is take off location if statments depending on how many waypoints are posted
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
    # Y values for waypoints in order 0 is take off location if statments depending on how many waypoints are posted
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
    # Z values for waypoints in order 0 is take off location if statments depending on how many waypoints are posted
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
    # Waypoint Type values for waypoints in order 0 is take off location if statments depending on how many waypoints are posted
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

    # Set up 3 axies chart
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # X, Y and Z data points for plot if else statments to plot based on how many points there are

    if numberofwaypoints == 1:
        X = [x0, x1]
        Y = [y0, y1]
        Z = [z0, z1]
        WP = [wp0, wp1]
        print(1)
    elif numberofwaypoints == 2:
        X = [x0, x1, x2]
        Y = [y0, y1, y2]
        Z = [z0, z1, z2]
        WP = [wp0, wp1, wp2]
        print(2)
    elif numberofwaypoints == 3:
        X = [x0, x1, x2, x3]
        Y = [y0, y1, y2, y3]
        Z = [z0, z1, z2, z3]
        WP = [wp0, wp1, wp2, wp3]
        print(3)
    elif numberofwaypoints == 4:
        X = [x0, x1, x2, x3, x4]
        Y = [y0, y1, y2, y3, y4]
        Z = [z0, z1, z2, z3, z4]
        WP = [wp0, wp1, wp2, wp3, wp4]
        print(4)
    elif numberofwaypoints == 5:
        X = [x0, x1, x2, x3, x4, x5]
        Y = [y0, y1, y2, y3, y4, y5]
        Z = [z0, z1, z2, z3, z4, z5]
        WP = [wp0, wp1, wp2, wp3, wp4, wp5]
        print(5)
    elif numberofwaypoints == 6:
        X = [x0, x1, x2, x3, x4, x5, x6]
        Y = [y0, y1, y2, y3, y4, y5, y6]
        Z = [z0, z1, z2, z3, z4, z5, z6]
        WP = [wp0, wp1, wp2, wp3, wp4, wp5, wp6]
        print(6)
    elif numberofwaypoints == 7:
        X = [x0, x1, x2, x3, x4, x5, x6, x7]
        Y = [y0, y1, y2, y3, y4, y5, y6, y7]
        Z = [z0, z1, z2, z3, z4, z5, z6, z7]
        WP = [wp0, wp1, wp2, wp3, wp4, wp5, wp6, wp7]
        print(7)
    elif numberofwaypoints == 8:
        X = [x0, x1, x2, x3, x4, x5, x6, x7, x8]
        Y = [y0, y1, y2, y3, y4, y5, y6, y7, y8]
        Z = [z0, z1, z2, z3, z4, z5, z6, z7, z8]
        WP = [wp0, wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8]
        print(8)
    elif numberofwaypoints == 9:
        X = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9]
        Y = [y0, y1, y2, y3, y4, y5, y6, y7, y8, y9]
        Z = [z0, z1, z2, z3, z4, z5, z6, z7, z8, z9]
        WP = [wp0, wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8, wp9]
        print(9)
    elif numberofwaypoints == 10:
        X = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
        Y = [y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10]
        Z = [z0, z1, z2, z3, z4, z5, z6, z7, z8, z9, z10]
        WP = [wp0, wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8, wp9, wp10]
        print(10)
    # Print list of Waypoints
    print(X)
    print(Y)
    print(Z)
    print(WP)

    # Trying to merge code here
    origin = (x0, y0, z0, wp0)  # This is the origin points above from where ever they come from in a list thing
    points = zip(X, Y, Z, WP)  # converting values to print as list, stays in same order but not a list
    points = list(points)  # turns zipped thing into sortable list
    ordered = []  # Gives an empty set, origin inside adds the origin back to the list of points so we can start at the origin
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
    ordered.append(origin)  # Appends the origin to the end of the list so the drone returns home
    print(ordered)  # Prints out the value for the ordered list of points to go to.

    test_list = ordered
    print("Original list is : " + str(test_list))  # Printing original list
    res = list(zip(*test_list))  # Using zip() and * operator to perform Unzipping
    print("Modified list is : " + str(res))  # Printing modified list
    XXX = res[0]  # These 3 lines get the X, Y, X values from the ordered system
    YYY = res[1]
    ZZZ = res[2]
    WPP = res[3]
    print(XXX)  # Prints the values so you can see the X, Y, Z, Waypoints in the optimized order
    print(YYY)
    print(ZZZ)
    print(WPP)

    # Modifyied order of plot
    ax.plot3D(XXX, YYY, ZZZ, '*-')

    # Show 3d plot
    plt.show()

    # Put Tello into command mode
    send("command", delay)

    # Send the takeoff command
    send("takeoff", delay)

    # Flight plan for 1 waypoints
    if numberofwaypoints == 1:
        send("go " + str(XXX[1] - XXX[0]) + " " + str(YYY[1] - YYY[0]) + " " + str(ZZZ[1] - ZZZ[0]) + " " + str(100), delay)
        if WPP[1] == 'A':
            print('A')
            waypointA()
        elif WPP[1] == 'B':
            print('B')
            waypointB()
        elif WPP[1] == 'C':
            print('C')
            waypointC()
        elif WPP[1] == 'D':
            print('D')
            waypointD()
        elif WPP[1] == 'O':
            print('O')
        send("go " + str(XXX[2] - XXX[1]) + " " + str(YYY[2] - YYY[1]) + " " + str(ZZZ[2] - ZZZ[1]) + " " + str(100), delay)

    # Flight plan for 2 waypoints
    elif numberofwaypoints == 2:
        send("go " + str(XXX[1] - XXX[0]) + " " + str(YYY[1] - YYY[0]) + " " + str(ZZZ[1] - ZZZ[0]) + " " + str(100), delay)
        if WPP[1] == 'A':
            print('A')
            waypointA()
        elif WPP[1] == 'B':
            print('B')
            waypointB()
        elif WPP[1] == 'C':
            print('C')
            waypointC()
        elif WPP[1] == 'D':
            print('D')
            waypointD()
        elif WPP[1] == 'O':
            print('O')
        send("go " + str(XXX[2] - XXX[1]) + " " + str(YYY[2] - YYY[1]) + " " + str(ZZZ[2] - ZZZ[1]) + " " + str(100), delay)
        if WPP[2] == 'A':
            print('A')
            waypointA()
        elif WPP[2] == 'B':
            print('B')
            waypointB()
        elif WPP[2] == 'C':
            print('C')
            waypointC()
        elif WPP[2] == 'D':
            print('D')
            waypointD()
        elif WPP[2] == 'O':
            print('O')
        send("go " + str(XXX[3] - XXX[2]) + " " + str(YYY[3] - YYY[2]) + " " + str(ZZZ[3] - ZZZ[2]) + " " + str(100), delay)

    # Flight plan for 3 waypoints
    elif numberofwaypoints == 3:
        send("go " + str(XXX[1] - XXX[0]) + " " + str(YYY[1] - YYY[0]) + " " + str(ZZZ[1] - ZZZ[0]) + " " + str(100), delay)
        if WPP[1] == 'A':
            print('A')
            waypointA()
        elif WPP[1] == 'B':
            print('B')
            waypointB()
        elif WPP[1] == 'C':
            print('C')
            waypointC()
        elif WPP[1] == 'D':
            print('D')
            waypointD()
        elif WPP[1] == 'O':
            print('O')
        send("go " + str(XXX[2] - XXX[1]) + " " + str(YYY[2] - YYY[1]) + " " + str(ZZZ[2] - ZZZ[1]) + " " + str(100), delay)
        if WPP[2] == 'A':
            print('A')
            waypointA()
        elif WPP[2] == 'B':
            print('B')
            waypointB()
        elif WPP[2] == 'C':
            print('C')
            waypointC()
        elif WPP[2] == 'D':
            print('D')
            waypointD()
        elif WPP[2] == 'O':
            print('O')
        send("go " + str(XXX[3] - XXX[2]) + " " + str(YYY[3] - YYY[2]) + " " + str(ZZZ[3] - ZZZ[2]) + " " + str(100), delay)
        if WPP[3] == 'A':
            print('A')
            waypointA()
        elif WPP[3] == 'B':
            print('B')
            waypointB()
        elif WPP[3] == 'C':
            print('C')
            waypointC()
        elif WPP[3] == 'D':
            print('D')
            waypointD()
        elif WPP[3] == 'O':
            print('O')
        send("go " + str(XXX[4] - XXX[3]) + " " + str(YYY[4] - YYY[3]) + " " + str(ZZZ[4] - ZZZ[3]) + " " + str(100), delay)

    # Flight plan for 4 waypoints
    elif numberofwaypoints == 4:
        send("go " + str(XXX[1] - XXX[0]) + " " + str(YYY[1] - YYY[0]) + " " + str(ZZZ[1] - ZZZ[0]) + " " + str(100), delay)
        if WPP[1] == 'A':
            print('A')
            waypointA()
        elif WPP[1] == 'B':
            print('B')
            waypointB()
        elif WPP[1] == 'C':
            print('C')
            waypointC()
        elif WPP[1] == 'D':
            print('D')
            waypointD()
        elif WPP[1] == 'O':
            print('O')
        send("go " + str(XXX[2] - XXX[1]) + " " + str(YYY[2] - YYY[1]) + " " + str(ZZZ[2] - ZZZ[1]) + " " + str(100), delay)
        if WPP[2] == 'A':
            print('A')
            waypointA()
        elif WPP[2] == 'B':
            print('B')
            waypointB()
        elif WPP[2] == 'C':
            print('C')
            waypointC()
        elif WPP[2] == 'D':
            print('D')
            waypointD()
        elif WPP[2] == 'O':
            print('O')
        send("go " + str(XXX[3] - XXX[2]) + " " + str(YYY[3] - YYY[2]) + " " + str(ZZZ[3] - ZZZ[2]) + " " + str(100), delay)
        if WPP[3] == 'A':
            print('A')
            waypointA()
        elif WPP[3] == 'B':
            print('B')
            waypointB()
        elif WPP[3] == 'C':
            print('C')
            waypointC()
        elif WPP[3] == 'D':
            print('D')
            waypointD()
        elif WPP[3] == 'O':
            print('O')
        send("go " + str(XXX[4] - XXX[3]) + " " + str(YYY[4] - YYY[3]) + " " + str(ZZZ[4] - ZZZ[3]) + " " + str(100), delay)
        if WPP[4] == 'A':
            print('A')
            waypointA()
        elif WPP[4] == 'B':
            print('B')
            waypointB()
        elif WPP[4] == 'C':
            print('C')
            waypointC()
        elif WPP[4] == 'D':
            print('D')
            waypointD()
        elif WPP[4] == 'O':
            print('O')
        send("go " + str(XXX[5] - XXX[4]) + " " + str(YYY[5] - YYY[4]) + " " + str(ZZZ[5] - ZZZ[4]) + " " + str(100), delay)

    # Flight plan for 5 waypoints
    elif numberofwaypoints == 5:
        send("go " + str(XXX[1] - XXX[0]) + " " + str(YYY[1] - YYY[0]) + " " + str(ZZZ[1] - ZZZ[0]) + " " + str(100), delay)
        if WPP[1] == 'A':
            print('A')
            waypointA()
        elif WPP[1] == 'B':
            print('B')
            waypointB()
        elif WPP[1] == 'C':
            print('C')
            waypointC()
        elif WPP[1] == 'D':
            print('D')
            waypointD()
        elif WPP[1] == 'O':
            print('O')
        send("go " + str(XXX[2] - XXX[1]) + " " + str(YYY[2] - YYY[1]) + " " + str(ZZZ[2] - ZZZ[1]) + " " + str(100), delay)
        if WPP[2] == 'A':
            print('A')
            waypointA()
        elif WPP[2] == 'B':
            print('B')
            waypointB()
        elif WPP[2] == 'C':
            print('C')
            waypointC()
        elif WPP[2] == 'D':
            print('D')
            waypointD()
        elif WPP[2] == 'O':
            print('O')
        send("go " + str(XXX[3] - XXX[2]) + " " + str(YYY[3] - YYY[2]) + " " + str(ZZZ[3] - ZZZ[2]) + " " + str(100), delay)
        if WPP[3] == 'A':
            print('A')
            waypointA()
        elif WPP[3] == 'B':
            print('B')
            waypointB()
        elif WPP[3] == 'C':
            print('C')
            waypointC()
        elif WPP[3] == 'D':
            print('D')
            waypointD()
        elif WPP[3] == 'O':
            print('O')
        send("go " + str(XXX[4] - XXX[3]) + " " + str(YYY[4] - YYY[3]) + " " + str(ZZZ[4] - ZZZ[3]) + " " + str(100), delay)
        if WPP[4] == 'A':
            print('A')
            waypointA()
        elif WPP[4] == 'B':
            print('B')
            waypointB()
        elif WPP[4] == 'C':
            print('C')
            waypointC()
        elif WPP[4] == 'D':
            print('D')
            waypointD()
        elif WPP[4] == 'O':
            print('O')
        send("go " + str(XXX[5] - XXX[4]) + " " + str(YYY[5] - YYY[4]) + " " + str(ZZZ[5] - ZZZ[4]) + " " + str(100), delay)
        if WPP[5] == 'A':
            print('A')
            waypointA()
        elif WPP[5] == 'B':
            print('B')
            waypointB()
        elif WPP[5] == 'C':
            print('C')
            waypointC()
        elif WPP[5] == 'D':
            print('D')
            waypointD()
        elif WPP[5] == 'O':
            print('O')
        send("go " + str(XXX[6] - XXX[5]) + " " + str(YYY[6] - YYY[5]) + " " + str(ZZZ[6] - ZZZ[5]) + " " + str(100), delay)

    # Flight plan for 6 waypoints
    elif numberofwaypoints == 6:
        send("go " + str(XXX[1] - XXX[0]) + " " + str(YYY[1] - YYY[0]) + " " + str(ZZZ[1] - ZZZ[0]) + " " + str(100), delay)
        if WPP[1] == 'A':
            print('A')
            waypointA()
        elif WPP[1] == 'B':
            print('B')
            waypointB()
        elif WPP[1] == 'C':
            print('C')
            waypointC()
        elif WPP[1] == 'D':
            print('D')
            waypointD()
        elif WPP[1] == 'O':
            print('O')
        send("go " + str(XXX[2] - XXX[1]) + " " + str(YYY[2] - YYY[1]) + " " + str(ZZZ[2] - ZZZ[1]) + " " + str(100), delay)
        if WPP[2] == 'A':
            print('A')
            waypointA()
        elif WPP[2] == 'B':
            print('B')
            waypointB()
        elif WPP[2] == 'C':
            print('C')
            waypointC()
        elif WPP[2] == 'D':
            print('D')
            waypointD()
        elif WPP[2] == 'O':
            print('O')
        send("go " + str(XXX[3] - XXX[2]) + " " + str(YYY[3] - YYY[2]) + " " + str(ZZZ[3] - ZZZ[2]) + " " + str(100), delay)
        if WPP[3] == 'A':
            print('A')
            waypointA()
        elif WPP[3] == 'B':
            print('B')
            waypointB()
        elif WPP[3] == 'C':
            print('C')
            waypointC()
        elif WPP[3] == 'D':
            print('D')
            waypointD()
        elif WPP[3] == 'O':
            print('O')
        send("go " + str(XXX[4] - XXX[3]) + " " + str(YYY[4] - YYY[3]) + " " + str(ZZZ[4] - ZZZ[3]) + " " + str(100), delay)
        if WPP[4] == 'A':
            print('A')
            waypointA()
        elif WPP[4] == 'B':
            print('B')
            waypointB()
        elif WPP[4] == 'C':
            print('C')
            waypointC()
        elif WPP[4] == 'D':
            print('D')
            waypointD()
        elif WPP[4] == 'O':
            print('O')
        send("go " + str(XXX[5] - XXX[4]) + " " + str(YYY[5] - YYY[4]) + " " + str(ZZZ[5] - ZZZ[4]) + " " + str(100), delay)
        if WPP[5] == 'A':
            print('A')
            waypointA()
        elif WPP[5] == 'B':
            print('B')
            waypointB()
        elif WPP[5] == 'C':
            print('C')
            waypointC()
        elif WPP[5] == 'D':
            print('D')
            waypointD()
        elif WPP[5] == 'O':
            print('O')
        send("go " + str(XXX[6] - XXX[5]) + " " + str(YYY[6] - YYY[5]) + " " + str(ZZZ[6] - ZZZ[5]) + " " + str(100), delay)
        if WPP[6] == 'A':
            print('A')
            waypointA()
        elif WPP[6] == 'B':
            print('B')
            waypointB()
        elif WPP[6] == 'C':
            print('C')
            waypointC()
        elif WPP[6] == 'D':
            print('D')
            waypointD()
        elif WPP[6] == 'O':
            print('O')
        send("go " + str(XXX[7] - XXX[6]) + " " + str(YYY[7] - YYY[6]) + " " + str(ZZZ[7] - ZZZ[6]) + " " + str(100), delay)

    # Flight plan for 7 waypoints
    elif numberofwaypoints == 7:
        send("go " + str(XXX[1] - XXX[0]) + " " + str(YYY[1] - YYY[0]) + " " + str(ZZZ[1] - ZZZ[0]) + " " + str(100), delay)
        if WPP[1] == 'A':
            print('A')
            waypointA()
        elif WPP[1] == 'B':
            print('B')
            waypointB()
        elif WPP[1] == 'C':
            print('C')
            waypointC()
        elif WPP[1] == 'D':
            print('D')
            waypointD()
        elif WPP[1] == 'O':
            print('O')
        send("go " + str(XXX[2] - XXX[1]) + " " + str(YYY[2] - YYY[1]) + " " + str(ZZZ[2] - ZZZ[1]) + " " + str(100), delay)
        if WPP[2] == 'A':
            print('A')
            waypointA()
        elif WPP[2] == 'B':
            print('B')
            waypointB()
        elif WPP[2] == 'C':
            print('C')
            waypointC()
        elif WPP[2] == 'D':
            print('D')
            waypointD()
        elif WPP[2] == 'O':
            print('O')
        send("go " + str(XXX[3] - XXX[2]) + " " + str(YYY[3] - YYY[2]) + " " + str(ZZZ[3] - ZZZ[2]) + " " + str(100), delay)
        if WPP[3] == 'A':
            print('A')
            waypointA()
        elif WPP[3] == 'B':
            print('B')
            waypointB()
        elif WPP[3] == 'C':
            print('C')
            waypointC()
        elif WPP[3] == 'D':
            print('D')
            waypointD()
        elif WPP[3] == 'O':
            print('O')
        send("go " + str(XXX[4] - XXX[3]) + " " + str(YYY[4] - YYY[3]) + " " + str(ZZZ[4] - ZZZ[3]) + " " + str(100), delay)
        if WPP[4] == 'A':
            print('A')
            waypointA()
        elif WPP[4] == 'B':
            print('B')
            waypointB()
        elif WPP[4] == 'C':
            print('C')
            waypointC()
        elif WPP[4] == 'D':
            print('D')
            waypointD()
        elif WPP[4] == 'O':
            print('O')
        send("go " + str(XXX[5] - XXX[4]) + " " + str(YYY[5] - YYY[4]) + " " + str(ZZZ[5] - ZZZ[4]) + " " + str(100), delay)
        if WPP[5] == 'A':
            print('A')
            waypointA()
        elif WPP[5] == 'B':
            print('B')
            waypointB()
        elif WPP[5] == 'C':
            print('C')
            waypointC()
        elif WPP[5] == 'D':
            print('D')
            waypointD()
        elif WPP[5] == 'O':
            print('O')
        send("go " + str(XXX[6] - XXX[5]) + " " + str(YYY[6] - YYY[5]) + " " + str(ZZZ[6] - ZZZ[5]) + " " + str(100), delay)
        if WPP[6] == 'A':
            print('A')
            waypointA()
        elif WPP[6] == 'B':
            print('B')
            waypointB()
        elif WPP[6] == 'C':
            print('C')
            waypointC()
        elif WPP[6] == 'D':
            print('D')
            waypointD()
        elif WPP[6] == 'O':
            print('O')
        send("go " + str(XXX[7] - XXX[6]) + " " + str(YYY[7] - YYY[6]) + " " + str(ZZZ[7] - ZZZ[6]) + " " + str(100), delay)
        if WPP[7] == 'A':
            print('A')
            waypointA()
        elif WPP[7] == 'B':
            print('B')
            waypointB()
        elif WPP[7] == 'C':
            print('C')
            waypointC()
        elif WPP[7] == 'D':
            print('D')
            waypointD()
        elif WPP[7] == 'O':
            print('O')
        send("go " + str(XXX[8] - XXX[7]) + " " + str(YYY[8] - YYY[7]) + " " + str(ZZZ[8] - ZZZ[7]) + " " + str(100), delay)

    # Flight plan for 8 waypoints
    elif numberofwaypoints == 8:
        send("go " + str(XXX[1] - XXX[0]) + " " + str(YYY[1] - YYY[0]) + " " + str(ZZZ[1] - ZZZ[0]) + " " + str(100), delay)
        if WPP[1] == 'A':
            print('A')
            waypointA()
        elif WPP[1] == 'B':
            print('B')
            waypointB()
        elif WPP[1] == 'C':
            print('C')
            waypointC()
        elif WPP[1] == 'D':
            print('D')
            waypointD()
        elif WPP[1] == 'O':
            print('O')
        send("go " + str(XXX[2] - XXX[1]) + " " + str(YYY[2] - YYY[1]) + " " + str(ZZZ[2] - ZZZ[1]) + " " + str(100), delay)
        if WPP[2] == 'A':
            print('A')
            waypointA()
        elif WPP[2] == 'B':
            print('B')
            waypointB()
        elif WPP[2] == 'C':
            print('C')
            waypointC()
        elif WPP[2] == 'D':
            print('D')
            waypointD()
        elif WPP[2] == 'O':
            print('O')
        send("go " + str(XXX[3] - XXX[2]) + " " + str(YYY[3] - YYY[2]) + " " + str(ZZZ[3] - ZZZ[2]) + " " + str(100), delay)
        if WPP[3] == 'A':
            print('A')
            waypointA()
        elif WPP[3] == 'B':
            print('B')
            waypointB()
        elif WPP[3] == 'C':
            print('C')
            waypointC()
        elif WPP[3] == 'D':
            print('D')
            waypointD()
        elif WPP[3] == 'O':
            print('O')
        send("go " + str(XXX[4] - XXX[3]) + " " + str(YYY[4] - YYY[3]) + " " + str(ZZZ[4] - ZZZ[3]) + " " + str(100), delay)
        if WPP[4] == 'A':
            print('A')
            waypointA()
        elif WPP[4] == 'B':
            print('B')
            waypointB()
        elif WPP[4] == 'C':
            print('C')
            waypointC()
        elif WPP[4] == 'D':
            print('D')
            waypointD()
        elif WPP[4] == 'O':
            print('O')
        send("go " + str(XXX[5] - XXX[4]) + " " + str(YYY[5] - YYY[4]) + " " + str(ZZZ[5] - ZZZ[4]) + " " + str(100), delay)
        if WPP[5] == 'A':
            print('A')
            waypointA()
        elif WPP[5] == 'B':
            print('B')
            waypointB()
        elif WPP[5] == 'C':
            print('C')
            waypointC()
        elif WPP[5] == 'D':
            print('D')
            waypointD()
        elif WPP[5] == 'O':
            print('O')
        send("go " + str(XXX[6] - XXX[5]) + " " + str(YYY[6] - YYY[5]) + " " + str(ZZZ[6] - ZZZ[5]) + " " + str(100), delay)
        if WPP[6] == 'A':
            print('A')
            waypointA()
        elif WPP[6] == 'B':
            print('B')
            waypointB()
        elif WPP[6] == 'C':
            print('C')
            waypointC()
        elif WPP[6] == 'D':
            print('D')
            waypointD()
        elif WPP[6] == 'O':
            print('O')
        send("go " + str(XXX[7] - XXX[6]) + " " + str(YYY[7] - YYY[6]) + " " + str(ZZZ[7] - ZZZ[6]) + " " + str(100), delay)
        if WPP[7] == 'A':
            print('A')
            waypointA()
        elif WPP[7] == 'B':
            print('B')
            waypointB()
        elif WPP[7] == 'C':
            print('C')
            waypointC()
        elif WPP[7] == 'D':
            print('D')
            waypointD()
        elif WPP[7] == 'O':
            print('O')
        send("go " + str(XXX[8] - XXX[7]) + " " + str(YYY[8] - YYY[7]) + " " + str(ZZZ[8] - ZZZ[7]) + " " + str(100), delay)
        if WPP[8] == 'A':
            print('A')
            waypointA()
        elif WPP[8] == 'B':
            print('B')
            waypointB()
        elif WPP[8] == 'C':
            print('C')
            waypointC()
        elif WPP[8] == 'D':
            print('D')
            waypointD()
        elif WPP[8] == 'O':
            print('O')
        send("go " + str(XXX[9] - XXX[8]) + " " + str(YYY[9] - YYY[8]) + " " + str(ZZZ[9] - ZZZ[8]) + " " + str(100), delay)

    # Flight plan for 9 waypoints
    elif numberofwaypoints == 9:
        send("go " + str(XXX[1] - XXX[0]) + " " + str(YYY[1] - YYY[0]) + " " + str(ZZZ[1] - ZZZ[0]) + " " + str(100), delay)
        if WPP[1] == 'A':
            print('A')
            waypointA()
        elif WPP[1] == 'B':
            print('B')
            waypointB()
        elif WPP[1] == 'C':
            print('C')
            waypointC()
        elif WPP[1] == 'D':
            print('D')
            waypointD()
        elif WPP[1] == 'O':
            print('O')
        send("go " + str(XXX[2] - XXX[1]) + " " + str(YYY[2] - YYY[1]) + " " + str(ZZZ[2] - ZZZ[1]) + " " + str(100), delay)
        if WPP[2] == 'A':
            print('A')
            waypointA()
        elif WPP[2] == 'B':
            print('B')
            waypointB()
        elif WPP[2] == 'C':
            print('C')
            waypointC()
        elif WPP[2] == 'D':
            print('D')
            waypointD()
        elif WPP[2] == 'O':
            print('O')
        send("go " + str(XXX[3] - XXX[2]) + " " + str(YYY[3] - YYY[2]) + " " + str(ZZZ[3] - ZZZ[2]) + " " + str(100), delay)
        if WPP[3] == 'A':
            print('A')
            waypointA()
        elif WPP[3] == 'B':
            print('B')
            waypointB()
        elif WPP[3] == 'C':
            print('C')
            waypointC()
        elif WPP[3] == 'D':
            print('D')
            waypointD()
        elif WPP[3] == 'O':
            print('O')
        send("go " + str(XXX[4] - XXX[3]) + " " + str(YYY[4] - YYY[3]) + " " + str(ZZZ[4] - ZZZ[3]) + " " + str(100), delay)
        if WPP[4] == 'A':
            print('A')
            waypointA()
        elif WPP[4] == 'B':
            print('B')
            waypointB()
        elif WPP[4] == 'C':
            print('C')
            waypointC()
        elif WPP[4] == 'D':
            print('D')
            waypointD()
        elif WPP[4] == 'O':
            print('O')
        send("go " + str(XXX[5] - XXX[4]) + " " + str(YYY[5] - YYY[4]) + " " + str(ZZZ[5] - ZZZ[4]) + " " + str(100), delay)
        if WPP[5] == 'A':
            print('A')
            waypointA()
        elif WPP[5] == 'B':
            print('B')
            waypointB()
        elif WPP[5] == 'C':
            print('C')
            waypointC()
        elif WPP[5] == 'D':
            print('D')
            waypointD()
        elif WPP[5] == 'O':
            print('O')
        send("go " + str(XXX[6] - XXX[5]) + " " + str(YYY[6] - YYY[5]) + " " + str(ZZZ[6] - ZZZ[5]) + " " + str(100), delay)
        if WPP[6] == 'A':
            print('A')
            waypointA()
        elif WPP[6] == 'B':
            print('B')
            waypointB()
        elif WPP[6] == 'C':
            print('C')
            waypointC()
        elif WPP[6] == 'D':
            print('D')
            waypointD()
        elif WPP[6] == 'O':
            print('O')
        send("go " + str(XXX[7] - XXX[6]) + " " + str(YYY[7] - YYY[6]) + " " + str(ZZZ[7] - ZZZ[6]) + " " + str(100), delay)
        if WPP[7] == 'A':
            print('A')
            waypointA()
        elif WPP[7] == 'B':
            print('B')
            waypointB()
        elif WPP[7] == 'C':
            print('C')
            waypointC()
        elif WPP[7] == 'D':
            print('D')
            waypointD()
        elif WPP[7] == 'O':
            print('O')
        send("go " + str(XXX[8] - XXX[7]) + " " + str(YYY[8] - YYY[7]) + " " + str(ZZZ[8] - ZZZ[7]) + " " + str(100), delay)
        if WPP[8] == 'A':
            print('A')
            waypointA()
        elif WPP[8] == 'B':
            print('B')
            waypointB()
        elif WPP[8] == 'C':
            print('C')
            waypointC()
        elif WPP[8] == 'D':
            print('D')
            waypointD()
        elif WPP[8] == 'O':
            print('O')
        send("go " + str(XXX[9] - XXX[8]) + " " + str(YYY[9] - YYY[8]) + " " + str(ZZZ[9] - ZZZ[8]) + " " + str(100), delay)
        if WPP[9] == 'A':
            print('A')
            waypointA()
        elif WPP[9] == 'B':
            print('B')
            waypointB()
        elif WPP[9] == 'C':
            print('C')
            waypointC()
        elif WPP[9] == 'D':
            print('D')
            waypointD()
        elif WPP[9] == 'O':
            print('O')
        send("go " + str(XXX[10] - XXX[9]) + " " + str(YYY[10] - YYY[9]) + " " + str(ZZZ[10] - ZZZ[9]) + " " + str(100),
             5)

    # Flight plan for 10 waypoints
    elif numberofwaypoints == 10:
        send("go " + str(XXX[1] - XXX[0]) + " " + str(YYY[1] - YYY[0]) + " " + str(ZZZ[1] - ZZZ[0]) + " " + str(100), delay)
        if WPP[1] == 'A':
            print('A')
            waypointA()
        elif WPP[1] == 'B':
            print('B')
            waypointB()
        elif WPP[1] == 'C':
            print('C')
            waypointC()
        elif WPP[1] == 'D':
            print('D')
            waypointD()
        elif WPP[1] == 'O':
            print('O')
        send("go " + str(XXX[2] - XXX[1]) + " " + str(YYY[2] - YYY[1]) + " " + str(ZZZ[2] - ZZZ[1]) + " " + str(100), delay)
        if WPP[2] == 'A':
            print('A')
            waypointA()
        elif WPP[2] == 'B':
            print('B')
            waypointB()
        elif WPP[2] == 'C':
            print('C')
            waypointC()
        elif WPP[2] == 'D':
            print('D')
            waypointD()
        elif WPP[2] == 'O':
            print('O')
        send("go " + str(XXX[3] - XXX[2]) + " " + str(YYY[3] - YYY[2]) + " " + str(ZZZ[3] - ZZZ[2]) + " " + str(100), delay)
        if WPP[3] == 'A':
            print('A')
            waypointA()
        elif WPP[3] == 'B':
            print('B')
            waypointB()
        elif WPP[3] == 'C':
            print('C')
            waypointC()
        elif WPP[3] == 'D':
            print('D')
            waypointD()
        elif WPP[3] == 'O':
            print('O')
        send("go " + str(XXX[4] - XXX[3]) + " " + str(YYY[4] - YYY[3]) + " " + str(ZZZ[4] - ZZZ[3]) + " " + str(100), delay)
        if WPP[4] == 'A':
            print('A')
            waypointA()
        elif WPP[4] == 'B':
            print('B')
            waypointB()
        elif WPP[4] == 'C':
            print('C')
            waypointC()
        elif WPP[4] == 'D':
            print('D')
            waypointD()
        elif WPP[4] == 'O':
            print('O')
        send("go " + str(XXX[5] - XXX[4]) + " " + str(YYY[5] - YYY[4]) + " " + str(ZZZ[5] - ZZZ[4]) + " " + str(100), delay)
        if WPP[5] == 'A':
            print('A')
            waypointA()
        elif WPP[5] == 'B':
            print('B')
            waypointB()
        elif WPP[5] == 'C':
            print('C')
            waypointC()
        elif WPP[5] == 'D':
            print('D')
            waypointD()
        elif WPP[5] == 'O':
            print('O')
        send("go " + str(XXX[6] - XXX[5]) + " " + str(YYY[6] - YYY[5]) + " " + str(ZZZ[6] - ZZZ[5]) + " " + str(100), delay)
        if WPP[6] == 'A':
            print('A')
            waypointA()
        elif WPP[6] == 'B':
            print('B')
            waypointB()
        elif WPP[6] == 'C':
            print('C')
            waypointC()
        elif WPP[6] == 'D':
            print('D')
            waypointD()
        elif WPP[6] == 'O':
            print('O')
        send("go " + str(XXX[7] - XXX[6]) + " " + str(YYY[7] - YYY[6]) + " " + str(ZZZ[7] - ZZZ[6]) + " " + str(100), delay)
        if WPP[7] == 'A':
            print('A')
            waypointA()
        elif WPP[7] == 'B':
            print('B')
            waypointB()
        elif WPP[7] == 'C':
            print('C')
            waypointC()
        elif WPP[7] == 'D':
            print('D')
            waypointD()
        elif WPP[7] == 'O':
            print('O')
        send("go " + str(XXX[8] - XXX[7]) + " " + str(YYY[8] - YYY[7]) + " " + str(ZZZ[8] - ZZZ[7]) + " " + str(100), delay)
        if WPP[8] == 'A':
            print('A')
            waypointA()
        elif WPP[8] == 'B':
            print('B')
            waypointB()
        elif WPP[8] == 'C':
            print('C')
            waypointC()
        elif WPP[8] == 'D':
            print('D')
            waypointD()
        elif WPP[8] == 'O':
            print('O')
        send("go " + str(XXX[9] - XXX[8]) + " " + str(YYY[9] - YYY[8]) + " " + str(ZZZ[9] - ZZZ[8]) + " " + str(100), delay)
        if WPP[9] == 'A':
            print('A')
            waypointA()
        elif WPP[9] == 'B':
            print('B')
            waypointB()
        elif WPP[9] == 'C':
            print('C')
            waypointC()
        elif WPP[9] == 'D':
            print('D')
            waypointD()
        elif WPP[9] == 'O':
            print('O')
        send("go " + str(XXX[10] - XXX[9]) + " " + str(YYY[10] - YYY[9]) + " " + str(ZZZ[10] - ZZZ[9]) + " " + str(100),
             5)
        if WPP[10] == 'A':
            print('A')
            waypointA()
        elif WPP[10] == 'B':
            print('B')
            waypointB()
        elif WPP[10] == 'C':
            print('C')
            waypointC()
        elif WPP[10] == 'D':
            print('D')
            waypointD()
        elif WPP[10] == 'O':
            print('O')
        send("go " + str(XXX[11] - XXX[10]) + " " + str(YYY[11] - YYY[10]) + " " + str(ZZZ[11] - ZZZ[10]) + " " + str(
            100), delay)

    # Land
    send("land", delay)

    # Print message
    print("Mission completed successfully!")

    return




##############################################
# DO NOT EDIT ANYTHING BELOW HERE
##############################################

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


if __name__ == "__main__":
    # Create and start a listening thread that runs in the background
    # This utilizes our receive functions and will continuously monitor for incoming messages
    receiveThread = threading.Thread(target=receive)
    receiveThread.daemon = True
    receiveThread.start()

    # sample waypoint list of 10 waypoints
    waypoint1 = Waypoint(0, 20, 40, 'A')
    waypoint2 = Waypoint(0, -20, 40, 'B')
    waypoint3 = Waypoint(10, 10, 40, 'C')
    waypoint4 = Waypoint(0, -20, 20, 'A')
    waypoint5 = Waypoint(20, 10, 20, 'A')
    waypoint6 = Waypoint(10, 90, 40, 'B')
    waypoint7 = Waypoint(40, 80, 40, 'C')
    waypoint8 = Waypoint(30, 30, 40, 'A')
    waypoint9 = Waypoint(50, 40, 70, 'A')
    waypoint10 = Waypoint(0, 50, 60, 'D')

    # waypoints = [waypoint1]
    # waypoints = [waypoint1, waypoint2]
    # waypoints = [waypoint1, waypoint2, waypoint3]
    # waypoints = [waypoint1, waypoint2, waypoint3, waypoint4]
    # waypoints = [waypoint1, waypoint2, waypoint3, waypoint4, waypoint5]
    # waypoints = [waypoint1, waypoint2, waypoint3, waypoint4, waypoint5, waypoint6]
    # waypoints = [waypoint1, waypoint2, waypoint3, waypoint4, waypoint5, waypoint6, waypoint7]
    # waypoints = [waypoint1, waypoint2, waypoint3, waypoint4, waypoint5, waypoint6, waypoint7, waypoint8]
    # waypoints = [waypoint1, waypoint2, waypoint3, waypoint4, waypoint5, waypoint6, waypoint7, waypoint8, waypoint9]
    waypoints = [waypoint1, waypoint2, waypoint3, waypoint4, waypoint5, waypoint6, waypoint7, waypoint8, waypoint9, waypoint10]

    # Execute the actual algorithm
    main_function(waypoints, sock)

    # Close the socket
    sock.close()

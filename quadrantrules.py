#!/usr/bin/python
# This will be a test script for the quadrant conditional statements
from math import *
import time

GVlat = float(input("Input the GV Latitude:"))
GVlong = float(input("Input the GV Longitude:"))

QClat = float(input("Input the QC Latitude:"))
QClong = float(input("Input the QC Longitude:"))

#delta longitutde and delta latitude
d_lat = float(GVlat - QClat)
d_long = float(GVlong - QClong)

def theta(d_lat,d_long):
    global theta
    #Quadrant 1
    if d_lat > 0 and d_long > 0:
       theta = degrees(atan(d_long/d_lat))
    elif d_long > 0 and d_lat == 0:
        theta = 90
    elif d_lat > 0 and d_long == 0:
       theta = 0

    #Quadrant 2
    elif d_lat < 0 and d_long > 0:
        theta = 180 - degrees(atan(d_long/abs(d_lat)))
    elif d_long > 0 and d_lat == 0:
        theta = 90
    elif d_lat < 0 and d_long == 0:
        theta = 180

    #Quadrant 3
    elif d_lat < 0 and d_long < 0:
        theta = 180 + degrees(atan(d_long/d_lat))
    elif d_long < 0 and d_lat == 0:
        theta = 270
    elif d_lat < 0  and d_long == 0:
        theta = 180

    #Quadrant 4
    elif d_lat > 0 and d_long < 0:
        theta = 360-degrees(atan(abs(d_long)/d_lat))
    elif d_long < 0 and d_lat == 0:
        theta = 270
    elif d_lat > 0 and d_long == 0:
        theta = 0

    print(theta)


def rotZ(theta):
    #Quadrant I, II, III
    if theta >= 0 and theta <= 270:
       rotZ = theta - 90

    #Quadrant IV
    elif theta >= 271 and theta <= 360:
        rotZ = -90 - (360-theta)

    print(rotZ)
    return rotZ

while True:
    theta(d_lat,d_long)
    rotZ(theta)



'''Code to get theta to rotZ format
Quadrant I
for theta in range (0, 90):
    rotZ = theta - 90

Quadrant II
for theta in range (91, 180):
    rotZ = theta - 90

Quadrant III
for theta in range (181, 270):
    rotZ = theta - 90

Quadrant IV
for theta in range (360, 271, -1):
    rotZ = -90 - (360 - theta)
'''

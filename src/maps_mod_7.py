#!/usr/bin/env python
#	Python GPS Tracking Example
#	SparkFun Electronics, A.Weiss
#	Beerware: if you use this and meet me, you must buy me a beer
#
#	Function:
#	Takes GPS position and altitude data and plots it on a scaled map image of your
#	choice. Altitude can also be displayed in a separate graph.
#
#	The program has a console menu that allows you to configure your connection.
#	The program will run with either a GPS moudle connected or no moudle connected.
#	If a GPS is connected, the position and altitude data is automatically saved
#	to a file called nmea.txt. If no GPS is connected, you must create your own
#	nmea.txt and fill it with GPGGA NMEA sentences.
#	A map needs to be created and saved as a file called map.png. When you create
#	your map, note the lat and long of the bottom left and top right corner, in decimal
#	degrees. Then enter this information into the global variables below. This way,
#	your the border of your map image can be used as the graph mins and maxs.
#	Once you have a map loaded and a GPS connected, you can run the program and select
#	either your position to be displayed on your map, or display altitude on a separate
#	graph. The maps are not updated in realtime, so you must close the map and run
#	the map command again in order to read new data.

import matplotlib.pyplot as plt
import serial, time, sys, threading, datetime, shutil

######Global Variables#####################################################
# you must declare the variables as 'global' in the fxn before using#
ser = 0
lat = 0
long = 0
pos_x = 0
pos_y = 0
alt = 0
i = 0 #x units for altitude measurment

#adjust these values based on your location and map, lat and long are in decimal degrees
TRX = -118.168444          #top right longitude
TRY = 34.065869            #top right latitude
BLX = -118.170136          #bottom left longitude
BLY = 34.065122             #bottom left latitude
BAUDRATE = 57600				#double check
lat_input = 0            #latitude of home marker
long_input = 0           #longitude of home marker

######FUNCTIONS############################################################

def check_serial():
		init_serial()

def init_serial():
	#opens the serial port based on the COM number you choose
	print "Found Ports:"
	for n,s in scan():
		print "%s\n" % s
	#	print "%s1" % s1
	print " "

	comnum = '/dev/ttyUSB0'    #QC to define serial port
	comnum1 = '/dev/ttyACM0'   #GV

	# configure the serial connections		ser = qc ser1 = gv
	global ser, ser1, BAUDRATE
	ser = serial.Serial()
	ser.baudrate = BAUDRATE
	ser.port = comnum
	ser.timeout = 1
	ser.open()
	ser.isOpen()

	ser1 = serial.Serial()
	ser1.baudrate = BAUDRATE
	ser1.port = comnum1
	ser1.timeout = 1
	ser1.open()
	ser1.isOpen()

	#Prints menu and asks for input
	global lat_input, long_input

	print 'OPEN: '+ ser.name + '\n'
	print 'OPEN: '+ ser1.name
	print 'Im cereal'
	print ''

	#can be used to enter positions through the user interface
	#print 'enter your home position'
	#print '4001.54351'
	#print 'Lat<'
	#plat = raw_input()
	#lat_input = float(plat)
	#print '-10517.3005'
	#print 'Long<'
	#plong = raw_input()
	#long_input = float(plong)

	thread()

def save_raw():
    	#this fxn creates a txt file and saves only GPGGA sentences
    	while True:
			try:
				while 1:
			    		line = ser.readline()
			    		line_str = str(line)
					line1 = ser1.readline()
					line1_str = str(line1)
			    		if(line_str[0] == '$' and line1_str[0] == '$'): # $GPGGA
			    			if(len(line_str) > 10 and len(line1_str) > 10):
			    				# open txt file and log data
			    				f = open('nmea_qc.txt', 'a')
			 				f1 = open('nmea_gv.txt', 'a')
			    				try:
			    					f.write('{0:}'.format(line_str))
				        			f1.write('{0:}'.format(line1_str))

			    				finally:
			    					f.close()
								f1.close()
			    					stream_serial()
			except IndexError:
				pass

def scan():
        #scan for available ports. return a list of tuples (num, name)
        available = []
        for i in range(1):
            try:
		s1 = serial.Serial('/dev/ttyUSB1')
                available.append( (i, s1.name))
                s1.close()   # explicit close 'cause of delayed gv in java

                s = serial.Serial('/dev/ttyUSB0')
                available.append( (i, s.name))
                s.close()   # explicit close 'cause of delayed GC in java
            except serial.SerialException:
                pass
        return available

def stream_serial():
        #stream data directly from the serial port
        line = ser.readline()
        line_str = str(line)
        print line_str

	line1 = ser1.readline()
        line1_str = str(line1)
        print line1_str



def thread():
    	#threads - run idependent of main loop
    	thread1 = threading.Thread(target = save_raw) #saves the raw GPS data over serial while the main program runs
    	#thread2 = threading.Thread(target = user_input) #optional second thread
    	thread1.start()
    	#thread2.start()


check_serial()

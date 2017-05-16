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
import time


starttime=time.time()
while True:
	f = open('nmea_gv.txt', 'r+')
	f.truncate()
	f = open('nmea_qc.txt', 'r+')
	f.truncate()
	time.sleep(10.0 - ((time.time() - starttime) % 10.0))

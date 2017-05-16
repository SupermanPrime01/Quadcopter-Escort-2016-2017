#!/usr/bin/env python
import matplotlib.pyplot as plt
import serial, time, sys, threading, datetime, shutil
import time
###########START WHILE LOOP##########################
while True:
    try:
        ######################################################################
        ############################QC##########################################
        with open('nmea_qc.txt','r') as f:
            temp = f.readlines()
            qc_lat_lon=temp[-1]
            qc_lat = qc_lat_lon[1] + qc_lat_lon[2] + qc_lat_lon[3] + qc_lat_lon[4] + qc_lat_lon[5] + qc_lat_lon[6] + qc_lat_lon[7] + qc_lat_lon[8]
            #f.readline(4)       #moves pointer
            #qc_lat=f.readline(5)

            qc_lon = qc_lat_lon[11] + qc_lat_lon[12] + qc_lat_lon[13] + qc_lat_lon[14] + qc_lat_lon[15] + qc_lat_lon[16] + qc_lat_lon[17] + qc_lat_lon[16] + qc_lat_lon[18]
            #f.readline(5)
            #qc_lon=f.readline(5)

            qc_lat=float(qc_lat)
            qc_lon=float(qc_lon)

#            print qc_lat
#            print qc_lon
            f.close()

        ############################GV##########################################

        with open('nmea_gv.txt','r') as f:
            temp1 = f.readlines()
            gv_lat_lon=temp1[-1]
            gv_lat = gv_lat_lon[1] + gv_lat_lon[2] + gv_lat_lon[3] + gv_lat_lon[4] + gv_lat_lon[5] + gv_lat_lon[6] + gv_lat_lon[7] + gv_lat_lon[8]
            #f.readline(4)
            gv_lon = gv_lat_lon[11] + gv_lat_lon[12] + gv_lat_lon[13] + gv_lat_lon[14] + gv_lat_lon[15] + gv_lat_lon[16] + gv_lat_lon[17] + gv_lat_lon[16] + gv_lat_lon[18]
            #gv_lat=f.readline(5)
            #f.readline(5)
            #gv_lon=f.readline(5)

            gv_lat=float(gv_lat)
            gv_lon=float(gv_lon)

#            print gv_lat
#            print gv_lon
            f.close()
            delta_lat = (gv_lat - qc_lat)*(10000000/90)
            delta_lon = (gv_lon - qc_lon)*(10000000/90)          #(10,000,000/90)

            hyp_m = (delta_lat**2 + delta_lon**2)**0.5
            #hyp_m = hyp*(108000/60
            hyp_ft= (hyp_m*3.2800839)

            print hyp_ft
            time.sleep(1)

            f4 = open('distance.txt','a')
#        try:
            timeout = time.time() + 70
        while time.time < timeout:
            f4.write(hyp_ft)

        averages = {}
        with open('distance.txt','r') as f5:
            data = f5.read().split('\n')
        for index in range(len(data), 60):
            n = float(int(data[index]) + int(data[index+1]) + int(data[index+2] + int(data[index+3] + int(data[index+4] + int(data[index+5] + int(data[index+6] + int(data[index+7] + int(data[index+8] + int(data[index+9] + int(data[index+10] + int(data[index+11] + int(data[index+12] + int(data[index+13] + int(data[index+14] + int(data[index+15] + int(data[index+16] + int(data[index+17] + int(data[index+18] + int(data[index+19] + int(data[index+20] + int(data[index+21] + int(data[index+22] + int(data[index+23] + int(data[index+24] + int(data[index+25] + int(data[index+26] + int(data[index+27] + int(data[index+28] + int(data[index+29] + int(data[index+30] + int(data[index+31] + int(data[index+32] + int(data[index+33] + int(data[index+34] + int(data[index+35] + int(data[index+36] + int(data[index+37] + int(data[index+38] + int(data[index+39] + int(data[index+40] + int(data[index+41] + int(data[index+42] + int(data[index+43] + int(data[index+44] + int(data[index+45] + int(data[index+46] + int(data[index+47] + int(data[index+48] + int(data[index+49] + int(data[index+50] + int(data[index+51] + int(data[index+52] + int(data[index+53] + int(data[index+54] + int(data[index+55] + int(data[index+56] + int(data[index+57] + int(data[index+58] + int(data[index+59])) / 60
            averages[index] = n

            f4.close()
            f5.close()
            print averages

    starttime=time.time()
        	f = open('nmea_gv.txt', 'r+')
        	f.truncate()
        	f = open('nmea_qc.txt', 'r+')
        	f.truncate()
        	time.sleep(70.0 - ((time.time() - starttime) % 70.0))

    except ValueError:
         pass

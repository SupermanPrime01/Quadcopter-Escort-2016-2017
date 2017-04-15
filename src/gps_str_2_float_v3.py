import matplotlib.pyplot as plt
import serial, time, sys, threading, datetime, shutil

######################################################################
############################QC##########################################
with open('nmea_qc.txt','r') as f:
    temp = f.readlines()
    qc_lat_lon=temp[-1]
    qc_lat = qc_lat_lon[4] + qc_lat_lon[5] + qc_lat_lon[6] + qc_lat_lon[7] + qc_lat_lon[8]
    #f.readline(4)       #moves pointer
    #qc_lat=f.readline(5)

    qc_lon = qc_lat_lon[14] + qc_lat_lon[15] + qc_lat_lon[16] + qc_lat_lon[17] + qc_lat_lon[18]
    #f.readline(5)
    #qc_lon=f.readline(5)

    qc_lat=float(qc_lat)
    qc_lon=float(qc_lon)

    print qc_lat
    print qc_lon
    f.close()

############################GV##########################################

with open('nmea_gv.txt','r') as f:
    temp1 = f.readlines()
    gv_lat_lon=temp1[-1]
    gv_lat = gv_lat_lon[4] + gv_lat_lon[5] + gv_lat_lon[6] + gv_lat_lon[7] + gv_lat_lon[8]
    #f.readline(4)
    gv_lon = gv_lat_lon[14] + gv_lat_lon[15] + gv_lat_lon[16] + gv_lat_lon[17] + gv_lat_lon[18]
    #gv_lat=f.readline(5)
    #f.readline(5)
    #gv_lon=f.readline(5)

    gv_lat=float(gv_lat)
    gv_lon=float(gv_lon)

    print gv_lat
    print gv_lon
    f.close()


############################Conversion##########################################

delta_lat = (qc_lat - gv_lat)
delta_lon = (qc_lon - gv_lon)

hyp = (delta_lat**2 + delta_lon**2)**0.5
hyp_m = hyp*(108000/60)

print hyp_m

#!/usr/bin/env python3
import serial
import time


#baud  setting on all arduinos should be !! 115200 BAUD SETTING !!

if __name__ == '__main__':

    try:
        # LIDAR board
        dev1 = serial.Serial('/dev/ttyACM1', 115200, timeout = 1)
        dev1.flush()
        print("ACM1")
    except:
        print("\t no AMC1")

    while True:
        try:
            print("AMC1\t"+dev1.readline().decode('utf-8').rstrip())  #LIDAR BOARD
        except KeyboardInterrupt:
            break
        except:
            continue

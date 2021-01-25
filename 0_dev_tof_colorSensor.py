#!/usr/bin/env python3
import serial
import time


#baud  setting on all arduinos should be !! 115200 BAUD SETTING !!

if __name__ == '__main__':
    # try to connect to all usb periferals
    try:
        # ToF & Color Sensor board
        # NOTE: Color Sensor is not currently software integrated on ToF periph device
        dev0 = serial.Serial('/dev/ttyACM0', 115200, timeout = 1)
        dev0.flush()
        print("ACM0")
    except:
        print("\t no AMC0")

    while True:

        try:
            #sample read from AMC0
            print("AMC0\t"+dev0.readline().decode('utf-8').rstrip())
        except KeyboardInterrupt:
            break
        except:
            continue

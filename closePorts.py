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
        dev0.close()
        print("ACM0 closed")
    except:
        print("\t no AMC0")
    
    try:
        # motor and servo arm board
        dev1 = serial.Serial('/dev/ttyACM1', 115200, timeout = 1)
        dev1.flush()
        dev1.close()
        print("ACM1 closed")
    except:
        print("\t no AMC1")
    
    try:
        #
        dev2 = serial.Serial('/dev/ttyACM2', 115200) #, timeout = 1)
        dev2.flush()
        dev2.close()
        print("ACM2 Closed") 
    except:
        print("\t no AMC2")
    
    try:
        # 
        dev3 = serial.Serial('/dev/ttyACM3', 115200, timeout = 1)
        dev3.flush()
        dev3.close()
        print("ACM3closed")
    except:
        print("\t no AMC3")

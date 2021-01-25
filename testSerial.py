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
    
    try:
        # LIDAR board
        dev1 = serial.Serial('/dev/ttyACM1', 115200, timeout = 1)
        dev1.flush()
        print("ACM1")
    except:
        print("\t no AMC1")
    
    try:
        # motor and servo arm board
        dev2 = serial.Serial('/dev/ttyACM2', 115200) #, timeout = 1)
        dev2.flush()
        print("ACM2") 
    except:
        print("\t no AMC2")
    
    try:
        # 
        dev3 = serial.Serial('/dev/ttyACM3', 115200, timeout = 1)
        dev3.flush()
        print("ACM3")
    except:
        print("\t no AMC3")
    
    
    #writing too quickly causes read errors on the arduino, writes should be seperated by a delay of ~.05 seconds  
     
    while True:
        #if jank % 22 == 0:
        #    print("sending 1:0:1")
            #sample write
            #dev2.write(b'1:0:1\x00')
        #time.sleep(1)
        try:
            #sample read from AMC0
            #print("AMC0\t"+dev0.readline().decode('utf-8').rstrip())
            print("AMC1\t"+dev1.readline().decode('utf-8').rstrip())  #motor and servo arm board
            #print("AMC2\t"+dev2.readline().decode('utf-8').rstrip())
            #print("AMC3\t"+dev0.readline().decode('utf-8').rstrip())
        except KeyboardInterrupt:
            break
        except:
            continue

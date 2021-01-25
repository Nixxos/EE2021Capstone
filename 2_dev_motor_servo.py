#!/usr/bin/env python3
import serial
import time


#baud  setting on all arduinos should be !! 115200 BAUD SETTING !!

if __name__ == '__main__':

    try:
        # motor and servo arm board
        dev2 = serial.Serial('/dev/ttyACM2', 115200) #, timeout = 1)
        dev2.flush()
        print("ACM2") 
    except:
        print("\t no AMC2")
        
    try:
        # motor and servo arm board
        dev2 = serial.Serial('/dev/ttyACM3', 115200) #, timeout = 1)
        dev2.flush()
        print("ACM3") 
    except:
        print("\t no AMC3")

    while True:
        #if jank % 22 == 0:
        #    print("sending 1:0:1")
            #sample write
            #dev2.write(b'1:0:1\x00')
        #time.sleep(1)
        try:
            print("AMC2\t"+dev2.readline().decode('utf-8').rstrip())
        except KeyboardInterrupt:
            break
        except:
            continue

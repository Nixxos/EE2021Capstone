from collections import namedtuple
import serial


#Establish Connection to RPI
try:
    usb = serial.Serial(USB_PORT, 9600, timeout=2)
    #usb.write(b'')
    #usb.readline()
except:
    print("error connecting")
    exit()

#Execution Loop
while True:
    command = input("Enter command: ")
if command == "a":  # read Arduino A0 pin value
    print("Arduino A0 value:", value)
elif command == "x":  # exit program
    print("Exiting program.")
else:
    exit()


'''
import serial
import RPi.GPIO as GPIO
import time
ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
'''
#needs lidars, gyro, and motor controller
def drive(target_distance, direction):
    #PID loop to account for distance error and theta error
    distance_init=lidar.getDistance()
    gyro_init=gyro.getAngle()
    itteration_time = #arbitrary value

    #linear variable init
    linear_error_prior = 0
    linear_integral_prior = 0
    linear_KP = 2 #arbitrary value
    linear_KI = 5 #arbitrary value
    linear_KD = 0 #arbitrary value
    linear_tolerance = #arbitrary value
    #angular variable init
    angular_error_prior = 0
    angular_integral_prior = 0
    angular_KP = #arbitrary value
    angular_KI = #arbitrary value
    angular_KD = #arbitrary value
    angular_tolerance = #arbitrary value

    for(linear_error=linear_tolerance+1;linear_error>linear_tolerance;) 
        linear_error = target_distance – (distance_init-lidar.getDistance())
        angular_error = gyro_init – gyro.getAngle()

        linear_integral = linear_integral_prior + linear_error * iteration_time
        angular_integral = angular_integral_prior + angular_error * iteration_time

        linear_derivative = (linear_error – linear_error_prior) / iteration_time
        angular_derivative = (angular_error – angular_error_prior) / iteration_time

        linear_output = linear_KP*linear_error + linear_KI*linear_integral + linear_KD*linear_derivative
        angular_output = angular_KP*angular_error + angular_KI*angular_integral + angular_KD*angular_derivative

        if(direction = 1)
            x=linear_output
            y=0
        elif(direction = 2)
            x=0
            y=linear_output
        elif(direction = 3)
            x=-linear_output
            y=0
        elif(direction = 4)
            x=0
            y=-linear_output

        Serial.send(encode(arduino.drive, x, y, angular_output))
        linear_error_prior = linear_error
        angular_error_prior = angular_error

        linear_integral_prior = linear_integral
        angular_integral_prior = angular_integral

        sleep(iteration_time)
    
    

#needs motor control and gyro
def rotate(target_angle):
    itteration_time = #arbitrary value
    #angular variable init
    angular_error_prior = 0
    angular_integral_prior = 0
    angular_KP = #arbitrary value
    angular_KI = #arbitrary value
    angular_KD = #arbitrary value
    angular_tolerance = #arbitrary value
    for(angular_error=angular_tolerance+1;angular_error>angular_tolerance;) 
        angular_error = target_angle – gyro.getAngle()
        angular_integral = angular_integral_prior + angular_error * iteration_time
        angular_derivative = (angular_error – angular_error_prior) / iteration_time
        angular_output = angular_KP*angular_error + angular_KI*angular_integral + angular_KD*angular_derivative
        Serial.send(encode(arduino.drive, 0, 0, angular_output))
        angular_error_prior = angular_error
        angular_integral_prior = angular_integral
        sleep(iteration_time)
    

Decode = namedtuple("Decode", "lvl1 lvl2 getball hitg1 hitg2 ret")


class DecodeOpcode:
 
    def switch(self, opcode):
        default = "Incorrect code"
        return getattr(self, 'case_' + str(opcode), lambda: default)()
 
    def case_0(self):
        m = Decode(0,0,0,0,0,0)
        #lvl1
        drive(15,1)
        drive(5,2)
        #lvl2
        drive(14,2)
        #getball
        drive(7,2)
        drive(52,3)
        #Call Arm Function
        drive(52,1)
        drive(7,0)
        return m
 
    def case_1(self):
        m = Decode(0,1,2,2,3,3)
        #lvl1
        drive(15,1)
        drive(5,2)
        #lvl2
        drive(5,2)
        drive(33,3)
        drive(9,2)
        #getball
        drive(7,2)
        drive(19,3)
        #Call Arm Function
        drive(19,1)
        drive(7,0)
        return m
 
    def case_2(self):
        m = Decode(0,0,0,1,5,8)
        #lvl1
        drive(15,1)
        drive(5,2)
        #lvl2
        drive(14,2)
        #getball
        drive(7,2)
        drive(52,3)
        #Call Arm Function
        drive(52,1)
        drive(7,0)
        return m
 
    def case_3(self):
        m = Decode(0,0,0,0,0,0)
        #lvl1
        drive(15,1)
        drive(5,2)
        #lvl2
        drive(14,2)
        #getball
        drive(7,2)
        drive(52,3)
        #Call Arm Function
        drive(19,1)
        drive(5,0)
        drive(5,2)
        drive(33,1)
        drive(7,0)
        return m
 
    def case_4(self):
        m = Decode(1,3,0,0,0,0)
        #lvl1
        drive(15,3)
        drive(5,2)
        #lvl2
        drive(5,2)
        drive(33,1)
        drive(9,2)
        #getball
        drive(7,2)
        drive(52,3)
        #Call Arm Function
        drive(19,1)
        drive(5,0)
        drive(5,2)
        drive(33,1)
        drive(7,0)
        return m
 
    def case_5(self):
        m = Decode(0,0,0,0,0,0)
        #lvl1
        drive(15,1)
        drive(5,2)
        #lvl2
        drive(14,2)
        #getball
        drive(7,2)
        drive(52,3)
        #Call Arm Function
        drive(19,1)
        drive(5,0)
        drive(5,2)
        drive(33,1)
        drive(7,0)
        return m
 
    def case_6(self):
        m = Decode(0,1,2,0,0,0)
        #lvl1
        drive(15,1)
        drive(5,2)
        #lvl2
        drive(5,2)
        drive(33,3)
        drive(9,2)
        #getball
        drive(7,2)
        drive(19,3)
        #Call Arm Function
        drive(19,1)
        drive(7,0)
        return m
        
    def case_7(self):
        m = Decode(1,2,2,0,0,0)
        #lvl1
        drive(15,3)
        drive(5,2)
        #lvl2
        drive(14,2)
        #getball
        drive(7,2)
        drive(19,3)
        #Call Arm Function
        drive(19,1)
        drive(7,0)
        return m

    def case_8(self):
        m = Decode(1,2,2,0,0,0)
        #lvl1
        drive(15,3)
        drive(5,2)
        #lvl2
        drive(14,2)
        #getball
        drive(7,2)
        drive(19,3)
        #Call Arm Function
        drive(19,1)
        drive(7,0)
        return m

    def case_9(self):
        m = Decode(1,3,0,0,0,0)
        #lvl1
        drive(15,3)
        drive(5,2)
        #lvl2
        drive(5,2)
        drive(33,1)
        drive(9,2)
        #getball
        drive(7,2)
        drive(52,3)
        #Call Arm Function
        drive(52,1)
        drive(7,0)
        return m

    def case_10(self):
        m = Decode(1,2,2,0,0,0)
        #lvl1
        drive(15,3)
        drive(5,2)
        #lvl2
        drive(14,2)
        #getball
        drive(7,2)
        drive(19,3)
        #Call Arm Function
        drive(19,1)
        drive(7,0)
        return m

    def case_11(self):
        m = Decode(1,2,2,0,0,0)
        #lvl1
        drive(15,3)
        drive(5,2)
        #lvl2
        drive(14,2)
        #getball
        drive(7,2)
        drive(19,3)
        #Call Arm Function
        drive(19,1)
        drive(7,0)
        return m

    def case_12(self):
        m = Decode(0,0,0,0,0,0)
        #lvl1
        drive(15,1)
        drive(5,2)
        #lvl2
        drive(14,2)
        #getball
        drive(7,2)
        drive(52,3)
        #Call Arm Function
        drive(52,1)
        drive(7,0)
        return m

    def case_13(self):
        m = Decode(0,0,0,0,0,0)
        #lvl1
        drive(15,1)
        drive(5,2)
        #lvl2
        drive(14,2)
        #getball
        drive(7,2)
        drive(52,3)
        #Call Arm Function
        drive(52,1)
        drive(7,0)
        return m

    def case_14(self):
        m = Decode(1,2,2,0,0,0)
        #lvl1
        drive(15,3)
        drive(5,2)
        #lvl2
        drive(14,2)
        #getball
        drive(7,2)
        drive(19,3)
        #Call Arm Function
        drive(19,1)
        drive(7,0)
        return m

    def case_15(self):
        m = Decode(1,2,2,0,0,0)
        #lvl1
        drive(15,3)
        drive(5,2)
        #lvl2
        drive(14,2)
        #getball
        drive(7,2)
        drive(19,3)
        #Call Arm Function
        drive(19,1)
        drive(7,0)
        return m
    
    def case_16(self):  #ghosts 0,1
        #lvl1
        drive(15,1)
        drive(5,2)   #in block 3 location
        #lvl2
        drive(14,2)  #in block 2 location
        #getball
        drive(7,2)   #in power pellet highway
        drive(19,1)  #power pellet 1
        
    def case_17(self):  #ghosts 0,2
        #lvl1
        drive(15,1)
        drive(5,2)   #in block 3 location
        #lvl2
        drive(5,2)
        drive(33,3)  #crossing block 4 location
        drive(9,2)   #in block 1 location
        #getball
        drive(7,2)
        drive(52,1)  #power pellet 1
        #call arm
        
    def case_18(self):    #ghosts 0,4
        #lvl1
        drive(15,1)
        drive(5,2)  #in block 3 location
        #lvl2
        drive(14,2)  #in block 2 location
        #getball
        drive(7,2)   #in power pellet highway
        drive(19,1)  #power pellet 1
        #call arm
        
    def case_19(self):   #ghosts 0,1  same route at op 16
        #lvl1
        drive(15,1)
        drive(5,2)   #in block 3 location
        #lvl2
        drive(14,2)  #in block 2 location
        #getball
        drive(7,2)
        drive(19,1)  #power pellet 1
        #call arm
        
    def case_20(self):  #ghosts 1,3
        #lvl1
        drive(15,3)
        drive(5,2)  #in block 0 location
        #lvl2
        drive(5,2)
        drive(33,1) #crossing block 4
        drive(9,2)  #in block 2 location
        #getball
        drive(7,2)
        drive(19,1)  #power pellet 1
        #call arm

    def case_21(self):  #ghosts 1,4
        #lvl1
        drive(15,1)
        drive(5,2)  #in block 3 location
        #lvl2
        drive(14,2)  #in block 2 location
        #getball
        drive(7,2)
        drive(19,1) #power pellet 1
        #call arm
    
    def case_22(self):  #ghosts 2,0
        #lvl1
        drive(15,1)
        drive(5,2)   #in block 3 location
        #lvl2
        drive(5,2)
        drive(33,3) #crossing block 4
        drive(9,2)  #in block 1
        #getball
        drive(7,2)
        drive(52,1) #power pellet 1
        #call arm
        
    def case_23(self):  #ghosts 2,3
        #lvl1
        drive(15,3)
        drive(5,2)  #in block 0 location
        #lvl2
        drive(14,2) #in block 1 location
        #getball
        drive(7,2)
        drive(52,1)  #power pellet 1
        #call arm
        
    def case_24(self):  #ghosts 2,4
        #lvl1
        drive(15,3)
        drive(5,2)  #in block 0 location
        #lvl2
        drive(14,2)  #in block 1 location
        #getball
        drive(7,2)
        drive(52,1)  #power pellet 1
        #call arm
        
    def case_25(self):  #ghosts 3,1
        #lvl1
        drive(15,3)
        drive(5,2)  #in block 0 location
        #lvl2
        drive(5,2)
        drive(33,1) #crossing block 4
        drive(9,2)  #in block 2 location
        #getball
        drive(7,2)
        drive(19,1)  #power pellet 1
        #call arm
    
    def case_26(self):  #ghosts 3,2
        #lvl1
        drive(15,3)
        drive(5,2)  #in block o location
        #lv2
        drive(14,2) #in block 1 location
        #getball
        drive(7,2)
        drive(52,1) #power pellet 1
        #call arm
        
    def case_27(self):  #ghosts 3,4
        #lvl1
        drive(15,3)
        drive(5,2)  #in block 0 location
        #lvl2
        drive(14,2) #in block 1 location
        #getball
        drive(7,2)
        drive(52,1) #power pellet 1
        #call arm
    def case_28(self):  #ghosts 4,0
        #lvl1
        drive(15,1)
        drive(5,2)  #in block 3 location
        #lvl2
        drive(14,2) #in block 2 location
        #getball
        drive(7,2)
        drive(19,1)  #power pellet 1
        #call arm
    
    def case_29(self):  #ghosts 4,1
        #lvl1
        drive(15,1)
        drive(5,2)  #in block 3
        #lvl2
        drive(14,2) #in block 2 location
        #get ball
        drive(7,2)
        drive(19,1) #power pellet 1
        #call arm
        
    def case_30(self):  #ghosts 4,2
        #lvl1
        drive(15,3)
        drive(5,2)  #in block 0 location
        #lvl2
        drive(14,2)  #in block 1 location
        #get ball
        drive(7,2)
        drive(52,1)  #power pellet 1
        #call arm
        
    def case_31(self):  #ghosts 4,3
        #lvl1
        drive(15,3)
        drive(5,2)  #in block 0 location
        #lvl2
        drive(14,2)  #in block 1 locaion
        #getball
        drive(7,2)
        drive(52,1)
        #call arm
        
    
        
s = DecodeOpcode()
 
t = s.switch(3)

print(t.ret)

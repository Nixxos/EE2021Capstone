import time
import serial


if __name__ == '__main__':

  three_flag = 0

  try:
		# motor and servo arm board
    dev2 = serial.Serial('/dev/ttyACM2', 115200) #, timeout = 1)
    dev2.flush()
    print("ACM2 Motor Input Initialized") 
    dev2.isOpen()
    print("Enter your commands below.\r\nInsert 'exit' to leave the application.")
		
  except:
    three_flag = 1
    print("\t no AMC2 Motor Serial Port")

  if three_flag == 1:
    try:
  		# motor and servo arm board
      dev2 = serial.Serial('/dev/ttyACM3', 115200) #, timeout = 1)
      dev2.flush()
      print("ACM3 Motor Input Initialized") 
      dev2.isOpen()
      print("Enter your commands below.\r\nInsert 'exit' to leave the application.")
    except:
      print("\t no AMC3 Motor Serial Port")
   
#	try:
#		# motor and servo arm board
#		dev2 = serial.Serial('/dev/ttyACM1', 115200) #, timeout = 1)
#		dev2.flush()
#		print("ACM1 Motor Input Initialized") 
#		dev2.isOpen()
#		print("Enter your commands below.\r\nInsert 'exit' to leave the application.")
		
#	except:
#		print("\t no AMC1 Motor Serial Port")

    #input = 1
  while True:
        #print("AMC2\t"+dev2.readline().decode('utf-8').rstrip())
    inputt = input(">> ")
    if inputt == "exit":
      print("exiting...")
      dev2.close()
      exit()
			
		#halt command
    if inputt == "r":
      inputt="1:0:1\n"
      inputt = inputt.encode()
      dev2.write(inputt)
      inputt = ""
			
		#move forward command
    if inputt == "w":
      inputt="1:0:2\n"
      inputt = inputt.encode()
      dev2.write(inputt)
      #dev2.write(inputt)
      inputt = ""
		
		#move backward command
    if inputt == "s":
      inputt="1:0:5\n"
      inputt = inputt.encode()
      dev2.write(inputt)
			#dev2.write(inputt)
      inputt = ""
			
		#move left command
    if inputt == "a":
      inputt="1:0:8\n"
      inputt = inputt.encode()
      dev2.write(inputt)
			#dev2.write(inputt)
      inputt = ""
			
		#move right command
    if inputt == "d":
      inputt="1:0:11\n"
      inputt = inputt.encode()
      dev2.write(inputt)
			#dev2.write(inputt)
      inputt = ""
			
		#yeet command
    if inputt == "q":
      inputt="1:0:14\n"
      inputt = inputt.encode()
      dev2.write(inputt)
			#dev2.write(inputt)
      inputt = ""

		#yeet reverse command
    if inputt == "e":
      inputt="1:0:15\n"
      inputt = inputt.encode()
      dev2.write(inputt)
			#dev2.write(inputt)
      inputt = ""
			
    else:
			# send the character to the device
			# (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
      inputt = inputt + "\n"
      inputt = inputt.encode()
      dev2.write(inputt)
			#dev2.write(inputt)
      print(inputt)
				#out = ''
			# let's wait one second before reading output (let's give device time to answer)
			#time.sleep(1)
      inputt = ""
		   # while ser.inWaiting() > 0:
			#    out += ser.read(1)

			#if out != '':
			#    print(">>" + out)
			
		

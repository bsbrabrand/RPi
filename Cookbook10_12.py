import serial
import time

ser = serial.Serial("/dev/serial0",9600, timeout=1)

#ser.write(bytes('a', 'utf-8'))
while(True):
    if(ser.in_waiting >0):
        data =ser.readline()
        print(data)

    
    #if ser.in_waiting >0:
     #   print("test2")
      #  line = ser.readline()
       # print(line)

#test
import serial
import time

ser = serial.Serial('/dev/serial0',9600)

#ser.write(bytes('a', 'utf-8'))
while(True):
    if(ser.in_waiting >0):
        print('e')
        data =ser.readline()
        print(data)
    #else:
        #print('a')


    
    #if ser.in_waiting >0:
     #   print("test2")
      #  line = ser.readline()
       # print(line)

#test
import serial

ser = serial.Serial('/dev/serial0',9600)

ser.write("testing")

#test
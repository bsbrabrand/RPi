from gpiozero import Button, DigitalOutputDevice
import time

rows = [Button(18), Button(17), Button(27), Button(23)]
cols = [DigitalOutputDevice(22), DigitalOutputDevice(25),
    DigitalOutputDevice(24),DigitalOutputDevice(16)]
keys = [
    ['1', '2', '3','A'],
    ['4', '5', '6','B'],
    ['7', '8', '9','C'],
    ['*', '0', '#','D']]

def get_key():
    key = 0
    for col_num, col_pin in enumerate(cols):
        col_pin.off()
        for row_num, row_pin in enumerate(rows):
            if row_pin.is_pressed:
                key = keys[row_num][col_num]
        col_pin.on()
    return key

while True:
    key = get_key()
    if key :
        print(key)
    time.sleep(0.3)
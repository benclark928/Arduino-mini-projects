import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
pins = [board.digital[4], board.digital[5], board.digital[6],  board.digital[7]]

while True: 
    for pin in pins: 
        pin.write(1)
        time.sleep(0.5)
        pin.write(0)
        time.sleep(0.5)
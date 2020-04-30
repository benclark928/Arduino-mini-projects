import pyfirmata
import time

board = pyfirmata.Arduino('COM3')

while True:
    board.digital[12].write(1)
    time.sleep(3)
    board.digital[12].write(0)
    time.sleep(1
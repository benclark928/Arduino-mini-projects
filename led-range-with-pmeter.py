import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
it = pyfirmata.util.Iterator(board)
it.start()

pins = [4, 5, 6, 7]

analog_input = board.get_pin('a:0:i')

while True:
    analog_value = analog_input.read()
    print(analog_value)
    for pin in pins: 
        if analog_value is not None:
            delay = analog_value + 0.01 
            board.digital[pin].write(1)
            time.sleep(delay)
            board.digital[pin].write(0)
            time.sleep(delay)
        else:
            time.sleep(0.1)
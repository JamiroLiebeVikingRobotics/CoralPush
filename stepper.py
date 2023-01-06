import os
import board
import digitalio
import time
pulse = digitalio.DigitalInOut(board.GPIO_P36)  # pin 37
pulse.direction = digitalio.Direction.OUTPUT

dir = digitalio.DigitalInOut(board.GPIO_P37)  # pin 37
dir.direction = digitalio.Direction.OUTPUT

target = 1000
steps = 0
while steps < target:
    pulse.value = True
    time.sleep(0.05)
    pulse.value = False
    time.sleep(0.1)
    steps+=1

dir.deinit()
pulse.deinit()

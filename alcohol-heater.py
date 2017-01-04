#!/usr/bin/env python
# heat the alcohol sensor.
# run every 5minites.

import RPi.GPIO as GPIO
import time

### Heater ON
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.OUT)
GPIO.output(6, False)

### Heat time (second(s))
time.sleep(299)

### Heater OFF
GPIO.cleanup()


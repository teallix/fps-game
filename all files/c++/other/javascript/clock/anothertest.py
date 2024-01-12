#!/usr/bin/python
import time  # This is required to include time module.

while True:
    ticks = time.time()
    print("seconds counting:", ticks)
    time.sleep(0.01)
#!/bin/bash
circup install adafruit_display_text adafruit_display_shapes adafruit_sdcard adafruit_bus_device
export TARGET=/media/romilly/CIRCUITPY/
cp src/microplot/shared/*.py $TARGET
cp src/microplot/adafruit/*.py $TARGET

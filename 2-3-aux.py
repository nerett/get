import RPi.GPIO as gpio
import time

gpio.setmode( gpio.BCM )

leds = [ 21, 20, 16, 12, 7, 8, 25, 24 ]
gpio.setup( leds, gpio.OUT )

aux = [ 22, 23, 27, 18, 15, 14, 3, 2 ]
gpio.setup( aux, gpio.IN )

if 0:
    while 1:
        for led, pin in zip( leds, aux ):
            pin_value = gpio.input( pin )
            gpio.output( led, pin_value )

gpio.output( leds, 0 )
gpio.cleanup()
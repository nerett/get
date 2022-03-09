import RPi.GPIO as gpio
import time

gpio.setmode( gpio.BCM )

#gpio.setup( 26, gpio.OUT )
#gpio.output( 26, 1 )

leds = [ 21, 20, 16, 12, 7, 8, 25, 24 ]
gpio.setup( leds, gpio.OUT )

for i in range( 3 ):
    for k in leds:
        gpio.output( k, 1 )
        time.sleep( 0.2 )
        gpio.output( k, 0 )
        #time.sleep( 0.2 )

gpio.cleanup()
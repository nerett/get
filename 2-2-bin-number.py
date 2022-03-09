import RPi.GPIO as gpio
import time

gpio.setmode( gpio.BCM )

dac = [ 26, 19, 13, 6, 5, 11, 9, 10 ]
#number = [ 0, 1, 0, 0, 1, 1 , 1, 0 ]
number_255 = [ 1, 1, 1, 1, 1, 1, 1, 1 ] #считаем unsigned
number_127 = [ 0, 1, 1, 1, 1, 1, 1, 1 ]
number_64 =  [ 0, 1, 0, 0, 0, 0, 0, 0 ]
number_32 =  [ 0, 0, 1, 0, 0, 0, 0, 0 ]
number_5 =   [ 0, 0, 0, 0, 0, 1, 0, 1 ]
number_0 =   [ 0, 0, 0, 0, 0, 0, 0, 0 ]
number_256 = [ 0, 0, 0, 0, 0, 0, 0, 0 ] #переполнение

gpio.setup( dac, gpio.OUT )

gpio.output( dac, number_255 )
#gpio.output( dac, number_127 )
#gpio.output( dac, number_64 )
#gpio.output( dac, number_32 )
#gpio.output( dac, number_5 )
#gpio.output( dac, number_0 )
#gpio.output( dac, number_256 )

time.sleep( 15 )

gpio.output( dac, 0 )

gpio.cleanup()


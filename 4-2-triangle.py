import RPi.GPIO as gpio
import time


dac = [ 26, 19, 13, 6, 5, 11, 9, 10 ]
bdepth = 8 #хардкод разрядности

gpio.setmode( gpio.BCM )
gpio.setup( dac, gpio.OUT )


def decimal2binary( value ):
    return [int(bit) for bit in bin( value ) [2:].zfill( bdepth )]


try:
    period = int( input() )
    iterationt = period / ( 2 ** ( bdepth + 1 )  )
    
    while True:
        for decsignal in range( 2 ** bdepth ):
            gpio.output( dac, decimal2binary( int( decsignal ) ) )
            time.sleep( iterationt )
        for decsignal in reversed( range( 2 ** bdepth ) ):
            gpio.output( dac, decimal2binary( int( decsignal ) ) )
            time.sleep( iterationt )
        

finally:
    gpio.output( dac, 0 )
    gpio.cleanup()
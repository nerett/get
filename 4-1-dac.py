import RPi.GPIO as gpio


dac = [ 26, 19, 13, 6, 5, 11, 9, 10 ]
bdepth = 8 #хардкод разрядности
Vref = 3.3

gpio.setmode( gpio.BCM )
gpio.setup( dac, gpio.OUT )


def decimal2binary( value ):
    return [int(bit) for bit in bin( value ) [2:].zfill( bdepth )]


try:
    while True:
        inputvalue = input()

        if inputvalue == 'q':
            break
        if not inputvalue.isdigit() or int( inputvalue ) > ( 2 ** bdepth - 1 ):
            print( "Invalid value!\n" )
            continue

        Vout = Vref * ( int( inputvalue ) / 2 ** bdepth )
        print('V = {}'.format(Vout))

        gpio.output( dac, decimal2binary( int( inputvalue ) ) )

finally:
    gpio.output( dac, 0 )
    gpio.cleanup()
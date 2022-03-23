import RPi.GPIO as gpio

gpio.setmode( gpio.BCM )
gpio.setup( 2, gpio.OUT )
pwmctrl = gpio.PWM( 2, 1000 )

try:
    pwmctrl.start( 0 )

    while True:
        inputval = float( input() )
        if inputval < 0 or inputval > 100:
            print( "Invalid value!" )
            continue

        
        pwmctrl.ChangeDutyCycle( inputval )

finally:
    #gpio.output( , 0 )
    gpio.cleanup()
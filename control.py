# import curses and GPIO
import curses
import RPi.GPIO as GPIO

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)


# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
        while True:
            char = screen.getch()
            if char == ord('q'):
                break
                GPIO.output(10, GPIO.LOW)
                GPIO.output(12, GPIO.LOW)
                GPIO.output(13, GPIO.LOW)
                GPIO.output(4, GPIO.LOW)
            if char == ord('b'):
                GPIO.output(10, GPIO.LOW)
                GPIO.output(12, GPIO.LOW)
                GPIO.output(13, GPIO.LOW)
                GPIO.output(4, GPIO.LOW)
            elif char == curses.KEY_UP:
                GPIO.output(10, GPIO.LOW)
                GPIO.output(12, GPIO.LOW)
                GPIO.output(13, GPIO.LOW)
                GPIO.output(4, GPIO.LOW)
                GPIO.output(12, GPIO.HIGH)
                GPIO.output(13, GPIO.HIGH)
                print("UP")
            elif char == curses.KEY_DOWN:
                GPIO.output(10, GPIO.LOW)
                GPIO.output(12, GPIO.LOW)
                GPIO.output(13, GPIO.LOW)
                GPIO.output(4, GPIO.LOW)
                GPIO.output(4, GPIO.HIGH)
                GPIO.output(10, GPIO.HIGH)
                print("DOWN")
            elif char == curses.KEY_RIGHT:
                GPIO.output(10, GPIO.LOW)
                GPIO.output(12, GPIO.LOW)
                GPIO.output(13, GPIO.LOW)
                GPIO.output(4, GPIO.LOW)
                GPIO.output(10, GPIO.HIGH)
                GPIO.output(13, GPIO.HIGH)
                print("RIGHT")
            elif char == curses.KEY_LEFT:
                GPIO.output(10, GPIO.LOW)
                GPIO.output(12, GPIO.LOW)
                GPIO.output(13, GPIO.LOW)
                GPIO.output(4, GPIO.LOW)
                GPIO.output(12, GPIO.HIGH)
                GPIO.output(4, GPIO.HIGH)
                print("LEFT")
	   # elif char == curses.KEY_SPACE:
           #     GPIO.output(14, GPIO.LOW)
	   #   	GPIO.output(15, GPIO.LOW)
	   #	GPIO.output(18, GPIO.LOW)
	   #	GPIO.output(23, GPIO.LOW)
           # elif char == 10:
           #     GPIO.output(7,False)
           #     GPIO.output(11,False)
           #     GPIO.output(13,False)
           #     GPIO.output(15,False)

finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()

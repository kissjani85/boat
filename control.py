# import curses and GPIO
import curses
import RPi.GPIO as GPIO

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BCM) 
GPIO.setup(2,GPIO.OUT)  # Lampa
GPIO.setup(5,GPIO.OUT)  # Bal kulso hatra
GPIO.setup(7,GPIO.OUT)  # Bal kulso elore
GPIO.setup(8,GPIO.OUT)  # Jobb kulso hatra
GPIO.setup(12,GPIO.OUT) # Jobb belso hatra 
GPIO.setup(16,GPIO.OUT) # Jobb belso elore 
GPIO.setup(20,GPIO.OUT) # Bal belso hatra 
GPIO.setup(21,GPIO.OUT) # Bal belso elore 
GPIO.setup(25,GPIO.OUT) # Jobb kulso elore 


# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
        while True:
            char = screen.getch()
            if char == ord('q'):            # Kilepes
                GPIO.output(5, GPIO.LOW)
                GPIO.output(7, GPIO.LOW)
                GPIO.output(8, GPIO.LOW)
                GPIO.output(12, GPIO.LOW)
                GPIO.output(16, GPIO.LOW)
                GPIO.output(20, GPIO.LOW)
                GPIO.output(21, GPIO.LOW)
                GPIO.output(25, GPIO.LOW)
                break
            if char == ord('e'):            # Vilagitas be
                GPIO.output(2, GPIO.LOW)
                print("LAMP ON")
            if char == ord('r'):            # Vilagitas ki
                GPIO.output(2, GPIO.HIGH)
                print("LAMP OFF")
            if char == ord('b'):            # Minden motor leall
                GPIO.output(5, GPIO.LOW)
                GPIO.output(7, GPIO.LOW)
                GPIO.output(8, GPIO.LOW)
                GPIO.output(12, GPIO.LOW)
                GPIO.output(16, GPIO.LOW)
                GPIO.output(20, GPIO.LOW)
                GPIO.output(21, GPIO.LOW)
                GPIO.output(25, GPIO.LOW)
                print("All engines STOP")
            elif char == curses.KEY_UP:     #Ket kulso elore 
                GPIO.output(5, GPIO.LOW)
                GPIO.output(7, GPIO.LOW)
                GPIO.output(8, GPIO.LOW)
                GPIO.output(25, GPIO.LOW)
                GPIO.output(7, GPIO.HIGH)
                GPIO.output(25, GPIO.HIGH)
                print("Outside FORWARD")
            elif char == curses.KEY_DOWN:   # Ket kulso hatra
                GPIO.output(5, GPIO.LOW)
                GPIO.output(7, GPIO.LOW)
                GPIO.output(8, GPIO.LOW)
                GPIO.output(25, GPIO.LOW)
                GPIO.output(5, GPIO.HIGH)
                GPIO.output(8, GPIO.HIGH)
                print("Outside BACK")
            elif char == curses.KEY_RIGHT:  # Enyhe jobb fordulat
                GPIO.output(5, GPIO.LOW)
                GPIO.output(7, GPIO.LOW)
                GPIO.output(8, GPIO.LOW)
                GPIO.output(25, GPIO.LOW)
                GPIO.output(7, GPIO.HIGH)
                print("RIGHT")
            elif char == curses.KEY_LEFT:   # Enyhe bal fordulat
                GPIO.output(5, GPIO.LOW)
                GPIO.output(7, GPIO.LOW)
                GPIO.output(8, GPIO.LOW)
                GPIO.output(25, GPIO.LOW)
                GPIO.output(25, GPIO.HIGH)
                print("LEFT")
            elif char == ord('w'):          # Ket belso elore
                GPIO.output(12, GPIO.LOW)
                GPIO.output(16, GPIO.LOW)
                GPIO.output(20, GPIO.LOW)
                GPIO.output(21, GPIO.LOW)
                GPIO.output(16, GPIO.HIGH)
                GPIO.output(21, GPIO.HIGH)
                print("TURBO FORWARD")
            elif char == ord('s'):          # Ket belso hatra
                GPIO.output(12, GPIO.LOW)
                GPIO.output(16, GPIO.LOW)
                GPIO.output(20, GPIO.LOW)
                GPIO.output(21, GPIO.LOW)
                GPIO.output(12, GPIO.HIGH)
                GPIO.output(20, GPIO.HIGH)
                print("TURBO BACK")
            elif char == ord('t'):          # Belsok kikapcs
                GPIO.output(12, GPIO.LOW)
                GPIO.output(16, GPIO.LOW)
                GPIO.output(20, GPIO.LOW)
                GPIO.output(21, GPIO.LOW)
                print("TURBO OFF")
            elif char == ord('d'):          # Teljes fordulat jobbra
                GPIO.output(5, GPIO.LOW)
                GPIO.output(7, GPIO.LOW)
                GPIO.output(8, GPIO.LOW)
                GPIO.output(12, GPIO.LOW)
                GPIO.output(16, GPIO.LOW)
                GPIO.output(20, GPIO.LOW)
                GPIO.output(21, GPIO.LOW)
                GPIO.output(25, GPIO.LOW)
                GPIO.output(7, GPIO.HIGH)
                GPIO.output(8, GPIO.HIGH)
                print("FULL RIGHT")
            elif char == ord('a'):          # Teljes fordulat balra
                GPIO.output(5, GPIO.LOW)
                GPIO.output(7, GPIO.LOW)
                GPIO.output(8, GPIO.LOW)
                GPIO.output(12, GPIO.LOW)
                GPIO.output(16, GPIO.LOW)
                GPIO.output(20, GPIO.LOW)
                GPIO.output(21, GPIO.LOW)
                GPIO.output(25, GPIO.LOW)
                GPIO.output(25, GPIO.HIGH)
                GPIO.output(5, GPIO.HIGH)
                print("FULL RIGHT")
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()

import RPi.GPIO as GPIO
import time

# Define the GPIO pins for the LEDs
led_pins = [2, 3, 4, 17, 27, 22, 10, 9]

def setup():
    GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
    for pin in led_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

def back_and_forth():
    for pin in led_pins:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(pin, GPIO.LOW)

    for pin in reversed(led_pins):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(pin, GPIO.LOW)

def destroy():
    for pin in led_pins:
        GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()

# Setup GPIO
setup()

try:
    while True:
        back_and_forth()
        time.sleep(1)  # Pause for 1 second between sequences

except KeyboardInterrupt:
    destroy()


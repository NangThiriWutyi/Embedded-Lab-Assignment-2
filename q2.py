

import RPi.GPIO as GPIO
import time

# Define GPIO pins for the LEDs
led_pins = [2, 3, 4, 17, 27, 22, 10, 9]

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pins, GPIO.OUT)

# Function to turn off all LEDs
def turn_off_all():
    GPIO.output(led_pins, GPIO.LOW)

# Initial state: Turn off all LEDs
turn_off_all()

def move_leds(led_pins):
    for i in range(len(led_pins) // 2):
        turn_off_all()  # Turn off all LEDs before turning on the specified ones
        GPIO.output(led_pins[i], GPIO.HIGH)
        GPIO.output(led_pins[-(i+1)], GPIO.HIGH)
        time.sleep(0.2)  # Adjust the sleep time for a faster movement
        turn_off_all()  # Turn off all LEDs before the next iteration

try:
    while True:
        # Move LEDs towards each other
        move_leds(led_pins)

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    GPIO.cleanup()


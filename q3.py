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
    middle = len(led_pins) // 2
    for i in range(middle):
        turn_off_all()  # Turn off all LEDs before turning on the specified ones
        GPIO.output(led_pins[middle - i - 1], GPIO.HIGH)
        GPIO.output(led_pins[middle + i], GPIO.HIGH)
        time.sleep(0.2)  # Adjust the sleep time for the movement speed
        turn_off_all()  # Turn off all LEDs before the next iteration

    # Turn on the middle two LEDs
    GPIO.output(led_pins[middle - 1], GPIO.HIGH)
    GPIO.output(led_pins[middle], GPIO.HIGH)
    time.sleep(0.2)  # Adjust the sleep time for the movement speed
    turn_off_all()  # Turn off all LEDs before the next iteration

try:
    while True:
        # Move LEDs from the middle outwards
        move_leds(led_pins)

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    GPIO.cleanup()


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led_pin = 17  # Change this to the GPIO pin you connected the LED to

GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        GPIO.output(led_pin, GPIO.HIGH)  # Turn the LED on
        time.sleep(1)                   # Wait for 1 second
        GPIO.output(led_pin, GPIO.LOW)   # Turn the LED off
        time.sleep(1)                   # Wait for 1 second

except KeyboardInterrupt:
    GPIO.cleanup()

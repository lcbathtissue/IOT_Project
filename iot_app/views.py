from .models import LightIntensity
from django.shortcuts import render
from django.http import HttpResponse
import serial, time
import RPi.GPIO as GPIO

import sys

GPIO.setmode(GPIO.BCM)
led_pin = 17
GPIO.setup(led_pin, GPIO.OUT)
led_state = GPIO.LOW  # Initial LED state

intensity_value = 42
light_intensity = LightIntensity.objects.create(intensity_value=intensity_value)
light_intensity.save()

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import LightIntensity  # Import your LightIntensity model

# STARTING VALUES
led_value = "OFF"
mode = "MANUAL"

# high values are low light, low values are high light
LI_LOWER_LIMIT = 100    # when BELOW this value, turn the light off (when automatic is enabled)
LI_UPPER_LIMIT = 10000  # when ABOVE this value, turn the light on (when automatic is enabled)

# USED TO CHECK AUTOMATIC BEHAVIOUR TO THRESHOLD VALUES
SIMULATE = False
SIMULATE_MDOE = "DARK"
# SIMULATE_MDOE = "LIGHT"
if SIMULATE_MDOE == "DARK":
    SIM_VALUE = 11000
elif SIMULATE_MDOE == "LIGHT":
    SIM_VALUE = 50
def index(request):
    global led_state
    ser = serial.Serial()
    ser.port = "/dev/rfcomm0"
    ser.baudrate = 115200
    ser.timeout = 1
    ser.setDTR(False)
    ser.setRTS(False)
    ser.open()
    new_data = 0
    ser.flushInput()
    ser.flush()
    ser.flushOutput()
    time.sleep(1)
    raw_data = ser.readline()
    try:
        ser.flushInput()
        new_data = int(raw_data)
        ser.flush()
    except ValueError:
        pass
    latest_intensity = raw_data
    if SIMULATE:
        latest_intensity = SIM_VALUE

    if request.method == 'POST':
        global led_value
        global mode

        if 'mode-manual' in request.POST:
            mode = "MANUAL"
        if 'mode-automatic' in request.POST:
            mode = "AUTOMATIC"

        if 'toggle' in request.POST:
            global led_state
            led_state = not led_state
            if mode == "MANUAL":
                if led_state:
                    print("[LED-MANUAL] Attempting to turn LED on!")
                    led_value = "ON"
                    GPIO.output(led_pin, GPIO.HIGH)
                else:
                    print("[LED-MANUAL] Attempting to turn LED off!")
                    led_value = "OFF"
                    GPIO.output(led_pin, GPIO.LOW)

    # MOVED TO TOP OF FILE
    # else:
    #     led_value = "OFF"
    #     mode = "MANUAL"

    if mode == "AUTOMATIC":
        if latest_intensity > LI_UPPER_LIMIT:  # SENSOR IS READING DARK - TURN ON LED
            led_state = not led_state
            print("[LED-AUTO] Attempting to turn LED on!")
            led_value = "ON"
            GPIO.output(led_pin, GPIO.HIGH)
        elif latest_intensity < LI_LOWER_LIMIT:  # SENSOR IS READING LIGHT - TURN OFF LED
            led_state = not led_state
            print("[LED-AUTO] Attempting to turn LED off!")
            led_value = "OFF"
            GPIO.output(led_pin, GPIO.LOW)

    # latest_intensity = LightIntensity.objects.last()
    # return render(request, 'index.html', {'latest_intensity': latest_intensity if latest_intensity else 'N/A'})
    return render(request, 'index.html', {
        'latest_intensity': latest_intensity if latest_intensity else 'N/A',
        'led_value': led_value,
        'mode': mode,
    })


def oldindex(request):
    latest_intensity = LightIntensity.objects.last()
    return render(request, 'index.html', {'latest_intensity': latest_intensity.intensity_value if latest_intensity else 'N/A'})


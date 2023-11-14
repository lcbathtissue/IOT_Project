from .models import LightIntensity
from django.shortcuts import render
from django.http import HttpResponse
import serial, time

import sys


intensity_value = 42
light_intensity = LightIntensity.objects.create(intensity_value=intensity_value)
light_intensity.save()

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import LightIntensity  # Import your LightIntensity model


def index(request):
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
    # latest_intensity = LightIntensity.objects.last()
    return render(request, 'index.html', {'latest_intensity': latest_intensity if latest_intensity else 'N/A'})


def oldindex(request):
    latest_intensity = LightIntensity.objects.last()
    return render(request, 'index.html', {'latest_intensity': latest_intensity.intensity_value if latest_intensity else 'N/A'})


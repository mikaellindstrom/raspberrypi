#!/usr/bin/python
import Adafruit_DHT
import paho.mqtt.client as mqtt
import time

sensor = Adafruit_DHT.AM2302
pin = 4
sleeptime = 60

client=mqtt.Client()
client.connect("192.168.2.199")

while True:
# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature_c = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
#if humidity is not None and temperature is not None:
#    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature_c, humidity))
#else:
#    print('Failed to get reading. Try again!')

    if humidity is not None and temperature_c is not None:
        temperature_f = temperature_c * (9.0/5) + 32 
        client.publish("attic/temp", temperature_f)
        client.publish("attic/humidity", humidity)
    time.sleep(sleeptime) 


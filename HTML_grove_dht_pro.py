#!/usr/bin/env python
#
# GrovePi Example for using the Grove Temperature & Humidity Sensor Pro 
# (http://www.seeedstudio.com/wiki/Grove_-_Temperature_and_Humidity_Sensor_Pro)
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  
# You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this example?  Ask on the forums here:  http://forum.dexterindustries.com/c/grovepi
#
'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
import grovepi
from grove_rgb_lcd import *
from time import sleep
# import math
from math import isnan
# to import json library
import json
 
# connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# this example uses the blue colored sensor.
# SIG,NC,VCC,GND
sensor = 4   # The Sensor goes on digital port 4.

# temp_humidity_sensor_type
# grove Base Kit comes with the blue sensor.
blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.

# added coded to set the backlight to Green
# we need to do it just once
# setting the backlight color once reduces the amount of data transfer over the I2C line
setRGB(0,255,0)

while True:
    try:
        
# this gets the temperature and Humidity from the DHT sensor
        [temp,hum] = grovepi.dht(sensor,blue)
        
# added to change temp from Celcius to Fahrenheit
        temp = ((temp/5.0)*9)+32
        
# added to round the temp to 2 decimal places
        new_temp = round(temp,2)

# prints temp and humidity to LCD
        print("temp =" , new_temp, "F\thumidity =" , hum, "%")

# to check if we have nans
# if we do then raise a type error exception
        if isnan(new_temp) is True or isnan(hum) is True:
          raise TypeError('nan error')
                
        t = str(new_temp)
        h = str(hum)
            
# instead of inserting a bunch of whitespace, we can just insert a \n
# we're ensuring that if we get some strange strings on one line, the 2nd one won't be affected
        setText_norefresh("Temperature:" + t + "Humidity:" + h + "%")

    except (IOError, TypeError) as e:
        print(str(e))
        #and since we got a type error
        #then reset the LCD's text
        setText("")
        
    except KeyboardInterrupt as e:
        print(str(e))
        # to blank the LCD when exiting program
        setText("")
        break
    
# create JSON dataset temphum
    temphum ={
        'Temperature':t,
        'Humidity':h
        }
    
# append data to File
    with open('temphum.json','a')as my_json:
        
        json.dump(temphum,my_json)
    
    time.sleep(60) #updates the records every minute
    
# time delay before refreshing LCD
    sleep(0.05)
        


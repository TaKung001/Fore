from machine import Pin, I2C, PWM
from imu import MPU6050
from time import sleep
from NetworkHelper import NetworkHelper
import time, sys
import utime
import math

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=40000)
imu = MPU6050(i2c)
buzzer = PWM(Pin(18))
trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)

def sound_on():
    for i in range(5):
        buzzer.duty_u16(900000)
        utime.sleep_ms(80)
        buzzer.duty_u16(0)
        utime.sleep_ms(80)
        
def sound_on1():
    for i in range(3):
        buzzer.duty_u16(900000)
        utime.sleep_ms(80)
        buzzer.duty_u16(0)
        utime.sleep_ms(80)
        
def sound_on2():
    for i in range(5):
        buzzer.duty_u16(900000)
        utime.sleep_ms(80)
        buzzer.duty_u16(0)
        utime.sleep_ms(80)

def sound_on3():
    for i in range(1):
        buzzer.duty_u16(900000)
        utime.sleep_ms(1000)
        buzzer.duty_u16(0)
        utime.sleep_ms(80)

def sound_off():
    for i in range(0):
        buzzer.duty_u16(0)
        utime.sleep_ms(80)
        buzzer.duty_u16(0)
        utime.sleep_ms(80)

def wifi():
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("RPi-Pico MicroPython Ver:", sys.version)
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    esp8266_at_ver = None
    print("StartUP", con.startUP())
    # print("ReStart",con.reStart())
    print("StartUP", con.startUP())
    print("Echo-Off", con.echoING())
    print("\r\n\r\n")
    esp8266_at_ver = con.getVersion()
    if esp8266_at_ver != None:
        print(esp8266_at_ver)
    con.setCurrentWiFiMode()
    print("\r\n\r\n")
    """
    Connect with the WiFi
    """
    ssid = "TUTAO" #wifi name
    pwd = "6666666690" # password
    print("Try to connect with the WiFi..")
    timeout = 0
    # default delay wifi delay 5 sec
    while timeout < 6:
        if "WIFI CONNECTED" in con.connectWiFi(ssid, pwd,delay=3):
            print("ESP8266 connect with the WiFi..")
            return True
            break
        else:
            print(".")
            timeout += 1
            time.sleep(0.5)
    if timeout >= 6:
        print("Timeout connect with the WiFi")
        return False
    
def getApi(host, path, param=""):
    print("\r\n\r\n")
    print("Now it's time to start HTTP Get/Post Operation.......\r\n")
    # host = "192.168.1.2"  # host
    # path = "/"  # path  ?? url
    #param = ""
    if param != "":
        path = path + "?" + param
    else:
        path = path
    timeout = 0
    # default delay get api delay 3 sec
    while timeout < 3:
        httpCode, httpRes = con.doHttpGet(host, path,delay=1)
        print(
            "-----------------------------------------------------------------------------"
        )
        print("HTTP Code:", httpCode)
        print("HTTP Response:", httpRes)
        print(
            "-----------------------------------------------------------------------------\r\n"
        )
        if httpCode == 200:
            print("Get data successful..\r\n")
            return httpRes
            break
        else:
            print("Error")
            print("Get data fail...")
            print("Please wait to try again....\r\n")
            timeout += 1
            time.sleep(0.5)
        if timeout >= 3:
            return False

con = NetworkHelper()
wifiCon = wifi()

while True:
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    print("The distance from object is" ,distance,"cm")
    utime.sleep(0.5) 
    print(imu.accel.xyz,end='\r')
    ax = round(imu.accel.x,1)
    ay = round(imu.accel.y,1)
    tem=round(imu.temperature,1)
    utime.sleep(0.5)
    print(ax,"\t",ay,"\t",tem,"   ",end="\r")
    if(distance < 50):
        sound_on()
    positive = 0.05
    if(ay > 0.274+positive or ay < -0.274-positive ): #32
        sound_on1()
        
    if(ay > 0.473+positive or ay < -0.473-positive ):#52
        sound_on2()

    if(ay > 0.674+positive or ay < -0.674-positive ):#87
        sound_on3()
        


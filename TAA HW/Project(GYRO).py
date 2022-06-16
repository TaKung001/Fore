from machine import Pin, I2C, PWM
from imu import MPU6050
import utime
import math

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=40000)
imu = MPU6050(i2c)
buzzer = PWM(Pin(18))

def sound_on():
    for i in range(5):
        buzzer.duty_u16(900000)
        utime.sleep_ms(80)
        buzzer.duty_u16(0)
        utime.sleep_ms(80)

def sound_off():
    for i in range(0):
        buzzer.duty_u16(0)
        utime.sleep_ms(80)
        buzzer.duty_u16(0)
        utime.sleep_ms(80)

while True:
    print(imu.accel.xyz,imu.temperature,end='\r')
    ax = round(imu.accel.x,1)
    ay = round(imu.accel.y,1)
    tem=round(imu.temperature,1)
    utime.sleep(1)
    print(ax,"\t",ay,"\t",tem,"   ",end="\r")
    if(ax > 0.5 ):
        degrees = math.degrees(math.asin(0.7070))
        print(degrees)
        degrees = math.degrees(math.asin())
        print(degrees)
        sound_on()
    #if(ay > 0.5 ):
        #degrees = math.degrees(math.asin(0.7710))
        #print(degrees)
        #sound_off()


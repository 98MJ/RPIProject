import I2C_driver as LCD
from time import *
import RPi.GPIO as GPIO


mylcd= LCD.lcd()

def main():
    k= ""
    Maxduty= 10
    PWMpin= 12
    duty_ratio= 0
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PWMpin, GPIO.OUT)
    
    seg= [29, 31, 32, 33, 35, 36, 37]
    GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)

    fnd = [(1,1,1,1,1,1,0), (0,1,1,0,0,0,0), (1,1,0,1,1,0,1), (1,1,1,1,0,0,1,),(0,1,1,0,0,1,1),(1,0,1,1,0,1,1), (1,0,1,1,1,1,1),
       (1,1,1,0,0,1,0), (1,1,1,1,1,1,1), (1,1,1,1,0,1,1)]

    
    
    Servo= GPIO.PWM(PWMpin, 50)
    
    Servo.start(0)
    Servo.ChangeDutyCycle(0)
    mylcd.lcd_display_string('Wating for 1s', 1)
    mylcd.lcd_display_string('Rotating 0-12 ', 2)
    sleep(2)   
    mylcd.lcd_clear()
    
    while duty_ratio <= Maxduty:
        Servo.ChangeDutyCycle(duty_ratio)
        mylcd.lcd_display_string('Rotating', 1)
        GPIO.output(seg, fnd[duty_ratio])
        m= str(duty_ratio)
        k= "Duty Rate : " + m
        mylcd.lcd_display_string(k, 2)
        int(duty_ratio)
        duty_ratio+= 1
        sleep(2)
        mylcd.lcd_clear()
        
    if duty_ratio > Maxduty:
        duty_ratio= 0
        Servo.ChangeDutyCycle(duty_ratio)
        mylcd.lcd_clear()
    
    Servo.stop()
    GPIO.cleanup()
    print('Everythings cleanup')

if __name__ == '__main__':
    main()
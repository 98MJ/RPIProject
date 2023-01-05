import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

RGB = [11, 13, 15]
seg= [29, 31, 32, 33, 35, 36, 37]
num= 0|1|2|3|4|5|6|7|8|9

GPIO.setup(RGB, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)



fnd = [(1,1,1,1,1,1,0), (0,1,1,0,0,0,0), (1,1,0,1,1,0,1), (1,1,1,1,0,0,1,),(0,1,1,0,0,1,1),(1,0,1,1,0,1,1), (1,0,1,1,1,1,1),
       (1,1,1,0,0,1,0), (1,1,1,1,1,1,1), (1,1,1,1,0,1,1)]


while 1:
    
    a= input('r, g, b or 0~9 중 하나를 선택하세요')
    GPIO.output(RGB, GPIO.LOW)
    

    if (a == 'r'):
        GPIO.output(RGB[0], GPIO.HIGH)
        time.sleep(1)
    elif (a == 'g'):
        GPIO.output(RGB[1], GPIO.HIGH)
        time.sleep(1)
    elif (a == 'b'):
        GPIO.output(RGB[2], GPIO.HIGH)
        time.sleep(1)
    elif (a == num):
        GPIO.output(seg, fnd[num])
    else:
        GPIO.output(RGB, GPIO.LOW)
        time.sleep(1)
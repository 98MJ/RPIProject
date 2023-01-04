import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

RGB = [11, 13, 15]

GPIO.setup(RGB, GPIO.OUT, initial=GPIO.LOW)

while 1:
    
    a= input('r, g, b 중 하나를 선택하세요')
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
    else:
        GPIO.output(RGB, GPIO.LOW)
        time.sleep(1)
    
# print('LED Test Start')
# # for i in range(11,17,2):
# for i in RGB:
#     GPIO.output(i, GPIO.HIGH)
#     time.sleep(1)
#     GPIO.output(i, GPIO.LOW)
#     time.sleep(1)
    

print('Test End')


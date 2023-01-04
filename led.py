import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# LED_R = 11
# LED_G = 13
# LED_B = 15

RGB = [11, 13, 15]

GPIO.setup(RGB, GPIO.OUT, initial=GPIO.LOW)

# GPIO.setup(LED_R, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(LED_G, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(LED_B, GPIO.OUT, initial=GPIO.LOW)

print('LED Test Start')
# for i in range(11,17,2):
for i in RGB:
    GPIO.output(i, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(i, GPIO.LOW)
    time.sleep(1)
    # GPIO.output(LED_G, GPIO.HIGH)
    # time.sleep(1)
    # GPIO.output(LED_G, GPIO.LOW)
    # time.sleep(1)
    # GPIO.output(LED_B, GPIO.HIGH)
    # time.sleep(1)
    # GPIO.output(LED_B, GPIO.LOW)
    # time.sleep(1)
    
    # GPIO.output(LED_R, GPIO.HIGH)
    # GPIO.output(LED_G, GPIO.HIGH)
    # time.sleep(1)
    # GPIO.output(LED_R, GPIO.LOW)
    # GPIO.output(LED_G, GPIO.LOW)
    # time.sleep(1)
    
    # GPIO.output(LED_B, GPIO.HIGH)
    # GPIO.output(LED_G, GPIO.HIGH)
    # time.sleep(1)
    # GPIO.output(LED_B, GPIO.LOW)
    # GPIO.output(LED_G, GPIO.LOW)
    # time.sleep(1)
    
    # GPIO.output(LED_R, GPIO.HIGH)
    # GPIO.output(LED_B, GPIO.HIGH)
    # time.sleep(1)
    # GPIO.output(LED_R, GPIO.LOW)
    # GPIO.output(LED_B, GPIO.LOW)
    # time.sleep(1)
    
    # GPIO.output(LED_R, GPIO.HIGH)
    # GPIO.output(LED_G, GPIO.HIGH)
    # GPIO.output(LED_B, GPIO.HIGH)
    # time.sleep(1)
    # GPIO.output(LED_R, GPIO.LOW)
    # GPIO.output(LED_G, GPIO.LOW)
    # GPIO.output(LED_B, GPIO.LOW)
    # time.sleep(1)

print('Test End')


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


seg= [29, 31, 32, 33, 35, 36, 37]
GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)

fnd = [(1,1,1,1,1,1,0), (0,1,1,0,0,0,0), (1,1,0,1,1,0,1), (1,1,1,1,0,0,1,),(0,1,1,0,0,1,1),(1,0,1,1,0,1,1), (1,0,1,1,1,1,1),
       (1,1,1,0,0,1,0), (1,1,1,1,1,1,1), (1,1,1,1,0,1,1)]


for i in range(10):
    GPIO.output(seg, fnd[i])
    time.sleep(2)
# for i in seg:
#     GPIO.output(i, GPIO.HIGH)
#     time.sleep(1)
#     GPIO.output(i, GPIO.LOW)
#     time.sleep(1)



# GPIO.output(fnd[seg], GPIO.HIGH)

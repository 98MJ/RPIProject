import RPi.GPIO as GPIO
import time

def main():
    
    Maxduty= 12
    
    PWMpin= 12
    i=0
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PWMpin, GPIO.OUT)
    
    Servo= GPIO.PWM(PWMpin, 50)
    
    seg= [29, 31, 32, 33, 35, 36, 37]
    GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)

    fnd = [(1,1,1,1,1,1,0), (0,1,1,0,0,0,0), (1,1,0,1,1,0,1), (1,1,1,1,0,0,1,),(0,1,1,0,0,1,1),(1,0,1,1,0,1,1), (1,0,1,1,1,1,1),
       (1,1,1,0,0,1,0), (1,1,1,1,1,1,1), (1,1,1,1,0,1,1)]
    
    Servo.start(0)
    Servo.ChangeDutyCycle(0)
    print('Wating for 1sec')
    time.sleep(1)
    
    print('Rotating at interval of 0-12 degrees')
    
    
    while 1:
        
        Servo.start(0)
        duty_ratio= float(input('duty_ratio를 입력하세요. 단 0~11'))
        Servo.ChangeDutyCycle(duty_ratio)
        GPIO.output(seg, fnd[int(duty_ratio)])
        time.sleep(1)
        
        if duty_ratio > Maxduty:
            duty_ratio= 0
            Servo.ChangeDutyCycle(duty_ratio)
            print('Do not Try over 12')
            Servo.stop()
    
    Servo.stop()
    GPIO.cleanup()
    print('Everythings cleanup')

if __name__ == '__main__':
    main()
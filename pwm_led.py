import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

LED = 12

GPIO.setup(LED, GPIO.OUT)

PWM_LED= GPIO.PWM(LED, 50)
PWM_LED.start(0)

try:
    while True:
        Duty_led= input('듀티비를 입력하세요')
        Freq= input('주파수를 입력하세요')
        
        duty= int(Duty_led)
        f= int(Freq)
        print('Duty rate : ' ,duty)
        print('frequancy : ' ,f)
        
        PWM_LED.ChangeDutyCycle(duty)
        PWM_LED.ChangeFrequency(f)
finally: 
    PWM_LED.stop()
    print('Cleaning up! ')
    GPIO.cleanup()

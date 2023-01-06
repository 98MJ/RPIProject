import RPi.GPIO as GPIO                   
import time       
import I2C_driver as LCD                        

# Trig=11 초음파 신호 전송핀 번호 지정 및 출력지정
# Echo=12 초음파 수신하는 수신 핀 번호 지정 및 입력지정

mylcd= LCD.lcd()

def main():
    duty= 1
    PinTrig=16
    PinEcho=18
    PWMpin= 12
    GPIO.setmode(GPIO.BOARD)  
    GPIO.setup(PWMpin, GPIO.OUT)
    GPIO.setup(PinTrig, GPIO.OUT)           
    GPIO.setup(PinEcho, GPIO.IN)    
    
    Servo= GPIO.PWM(PWMpin, 50)
    seg= [29, 31, 32, 33, 35, 36, 37]
    GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)

    fnd = [(0,1,1,0,0,0,0), (1,1,0,1,1,0,1), (1,1,1,1,0,0,1,)]                

    Servo.start(0)
    Servo.ChangeDutyCycle(duty)

    startTime=0
    stopTime=0
    mylcd.lcd_display_string("Close door", 2)
    
    while True:
        
        
        
        for i in reversed(range(3)):
            GPIO.output(PinTrig, False)    
            time.sleep(0.1)
            GPIO.output(PinTrig, True)          
            time.sleep(0.00001)            
            GPIO.output(PinTrig, False)  
            while GPIO.input(PinEcho) == 0:   
                startTime = time.time()
            while GPIO.input(PinEcho) == 1:   
                stopTime = time.time()

            Time_interval= stopTime - startTime     
            Distance = Time_interval * 17000
            Distance = round(Distance, 2) 
            m= str(Distance)
            k= "Distance:" + m + "cm"
            

            mylcd.lcd_display_string(k, 1)
            if (Distance < 10):
                duty= 10
                Servo.ChangeDutyCycle(duty)
                mylcd.lcd_clear()
                mylcd.lcd_display_string(k, 1)
                mylcd.lcd_display_string("Open door", 2)
                i=2
                GPIO.output(seg, fnd[i])
                
            else:
                time.sleep(1)
                GPIO.output(seg, fnd[i])
                mylcd.lcd_clear()
                mylcd.lcd_display_string(k, 1)
                if (i==0):
                    mylcd.lcd_display_string("Close door", 2)
                    duty=1
                    Servo.ChangeDutyCycle(duty)            
            
                
            
            
            
            


        
        
        


if __name__ == '__main__':
    main()
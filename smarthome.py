from Adafruit_BME280 import *
import I2C_driver as LCD  
import RPi.GPIO as GPIO                   
import time       


def main():
    mylcd= LCD.lcd()
    duty= 1
    
    PWMpin= 12    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PWMpin, GPIO.OUT)
    
    Servo= GPIO.PWM(PWMpin, 50)
    
    seg= [29, 31, 32, 33, 35, 36, 37]
    GPIO.setup(seg, GPIO.OUT, initial=GPIO.LOW)

    fnd = [(1,1,1,1,1,1,0), (0,1,1,0,0,0,0), (1,1,0,1,1,0,1), (1,1,1,1,0,0,1,),(0,1,1,0,0,1,1),(1,0,1,1,0,1,1), (1,0,1,1,1,1,1),
       (1,1,1,0,0,1,0), (1,1,1,1,1,1,1), (1,1,1,1,0,1,1), (0,0,0,0,0,0,0)]
    
    Servo.start(0)
    Servo.ChangeDutyCycle(duty)
    sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
    degrees = sensor.read_temperature()
    led = 30.57
    print('Wating for 1sec')
    time.sleep(1)
    
    while True:    
       
        
        degrees = sensor.read_temperature()
        # pascals = sensor.read_pressure()
        # hectopascals = pascals / 100
        # humidity = sensor.read_humidity()
        
        print(degrees)
        print(led)

        if (degrees > led):
            GPIO.output(seg, fnd[8])
            time.sleep(1)
            GPIO.output(seg, fnd[10])    
        
        led = degrees
        degreess= round(degrees, 2)
        str_Temp= str(degreess)
        k= "Temp=" + str_Temp+ "C"
        

        mylcd.lcd_clear() 
        mylcd.lcd_display_string(k, 1)
        time.sleep(1)
        
        if(degreess > 24):
            for i in range(3):
                duty= 10
                Servo.ChangeDutyCycle(duty)
                time.sleep(1)
                duty= 1
                Servo.ChangeDutyCycle(duty)
                time.sleep(1)
            # GPIO.output(seg, fnd[8])
            # time.sleep(1)
            # GPIO.output(seg, fnd[10])
                     
        else:
            GPIO.output(seg, fnd[10])
            
            
            

if __name__ == '__main__':
    main()



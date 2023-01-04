
# 1.라이브러리/모듈 선언
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

def main():
    #2.보드에 연결된 주변 장치 핀 번호 설정
    GPIO.setup(핀번호, 핀상태(input/output), 초기상태)
    #3.주변 장치 입력/출력 모드 상태 설정
    GPIO.output(핀번호, 출력상태)
    #4. 상황에 따른 동작 응용
    while True:

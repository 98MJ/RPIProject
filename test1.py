a= int(input('숫자를 입력하세요'))

odd= bool(a%2 == 1)
even= bool(a%2 == 0)

if (a > 10):
    print('10보다 크다.')
else:
    print('10보다 작거나 같다.')
    
if (odd == True):
    print(a, '은(는) 홀수입니다.')
if (even == True):
    print(a, '은(는) 짝수입니다.')    
    
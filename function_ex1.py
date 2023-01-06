def AB_plus(): #함수의 기본문법 1 - 매개변수 x, return x
    
    a= int(input('a='))
    b= int(input('b='))
    
    print('a+b = ', a+b)
    
AB_plus() #함수의 기본문법 1


def AB_minus(): #함수의 기본문법 2 - 매개변수 x, return o
    
    a,b = input('a b=').spilt()
    c= a-b
    
    print('a-b = ', c)
    return c

AB_minus() #함수의 기본문법 2

def AB_Multiply(c, d): #함수의 기본문법 3  - 매개변수 o, return x
    print('ab = ', c*d)

a= int(input('a='))
b= int(input('b='))

AB_Multiply(a, b)  #함수의 기본문법 3


def AB_Divide(e, f): #함수의 기본문법 4  - 매개변수 o, return o
    value= e/f # e/f: 실수출력, e//f: 정수출력
    return value
    
div =AB_Divide(a, b)
print(div)


# print('a+b = ', a+b)
# print('a-b = ', a-b)
# print('ab = ', a*b)
# print('a/b = ', a/b)
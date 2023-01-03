num= int(input('숫자를 입력하세요'))
count= 0
#even = bool(num%2 == 1)

for i in range(num+1):
    if( int(i%2) == 0):
        count +=  i
        
print(count)
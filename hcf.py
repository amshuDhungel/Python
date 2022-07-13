a,b = 10,5

if a < b:
    temp = a
    a = b
    b = temp

rem = a%b
if rem!=0:
    while(rem!=0):
        a = b
        b = rem
        rem = a % b    

print(b)        
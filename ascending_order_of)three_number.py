a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a < b < c:
    print("The number in ascending order is ", "(",a,b,c,")")
elif b < c < a:
    print("The number in ascending order is ", "(",b,c,a,")")
else:    
    print("The number in ascending order is ", "(",c,b,a,")")
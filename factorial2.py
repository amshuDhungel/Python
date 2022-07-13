n = int(input("Enter the number: "))
fact = 1

if n < 0:
    print("You cannot find the factorial of 0 and negative number")

else:
    while(n>1):
        fact = fact*n
        n = n-1

print(fact)
n = int(input("Enter the number: "))
fact = 1

if n < 0:
    print("You cannot find the factorial of 0 and negative number")

if n == 0:
    print("The value is ", 1)

else:
    while(n>1):
        fact = fact*n
        n = n-1

print("The factorial of given number is " ,fact)

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1;
#     else:
#         return     
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

if a > b  and a > c:
    largest = a
elif b > c:
    largest = b
else:
    largest = c 

print(largest, "is the largest of three numbers.")          
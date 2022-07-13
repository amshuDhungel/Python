a = int(input("Enter the number:"))

if a <= 0:
    print("The number is invalid")
else:    
    if a%2 == 0:
        print(f"{a} is even number")
        
    else:
        print(f"{a} is odd number")
            
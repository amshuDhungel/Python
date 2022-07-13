# def gcd(a, b):
#     if m< n:
#         (m,n) = (n,m)
#     if(m%n) == 0:
#         return n
#     else:
#         return(gcd(n, m%n)) #recusrion taking place
# print(gcd(8,12))                        

#calculating HCF using Euclidean Algorithm

#Defining function to calculatie hcf by EA

def hcf(a,b):
    while b:
        temp = b 
        b = a %b
        a = temp
    return a

#Reading numbers from user
first = int(input("Enter first number: "))        
second = int(input("Enter second number: "))

#function call & displaying output hcf
print("HCF of %d and %d is %d" %(first, second, hcf(first, second)))
n = int(input("How many number you want to input\n"))

nums = []

for i in range(n):
    num = int(input(f"Enter {i+1} number\n"))
    nums.append(num)
    

print(f"Number array is: {nums}")    

odd_sum = 0
even_sum = 0

for number in nums:
    print(f"The num is: {number}")
    if number %2 == 0:
        even_sum = even_sum + number
    else:
        odd_sum = odd_sum + number        
print(f'Even number is {even_sum}')        
print(f'odd number is {odd_sum}')        
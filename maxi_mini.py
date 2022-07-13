n = int(input("How many number you want to enter?\n"))

nums = []

for i in range(n):
    num = int(input(f"Enter {i+1} number\n"))
    nums.append(num)
    print(nums)

max = nums[0]    
min = nums[0]

for number in nums:
    if number<min:
        min = number
    else:
        max = number
print("The maximum number is ",max)            
print("The minimum number is ",min)            
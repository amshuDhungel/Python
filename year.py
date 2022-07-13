year = int(input('Enter the year of birth: '))

birth = 2078

if year < 1950:
    print(f'The person is alive. he exist in history')
elif year < birth:
    print(f"The person is born in today generation. He is {birth - year} years old.")    
else:
    print(f'The person may exist in history.')    
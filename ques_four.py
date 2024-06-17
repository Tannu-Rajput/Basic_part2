n=int(input("Enter the digit:  "))
resverse_digit=0
while n!=0:
    res=n%10
    resverse_digit=resverse_digit*10 + res
    n=n//10
print("number is ",resverse_digit)    
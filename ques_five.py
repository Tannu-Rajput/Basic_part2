# Armstrong number

n=int(input("enter the number: "))
m=n
count=0
sum =0
while n != 0:
    n % 10
    n=n//10
    count+=1
n=m
temp=n
while temp>0:
    res=temp%10
    sum=sum+res**count
    temp//=10
if n==sum:
    print("yes")
else:
    print("no")  
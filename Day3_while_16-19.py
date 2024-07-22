#while: if range is unknown, then to reduce the size we use while loop

#16. sum of digits------very important
n=int(input())
sum=0
while(n>0):
    a=n%10
    sum=sum+a
    n=n//10
print(sum)

#17. sum of squares of a digit in a given num
n=int(input())
sum=0
while(n>0):
    a=n%10
    sum=sum+a**2
    n=n//10
print(sum)

#18. sum of even digits in a num
n=int(input())
sum=0
while(n>0):
    a=n%10
    if(a%2==0):
       sum=sum+a
    n=n//10
print(sum)

#19. *******************************************************
# reverse the number-----123=321
#***********************************************************
n=int(input())
rev="" #empty string
while(n>0):
    a=n%10
    rev=rev+str(a) #since a is in int it must be converted to str
    n=n//10
print(int(rev)) #again later covert it into int

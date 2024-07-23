#1. find if the given num is even or odd
n=int(input())
if( n%2 == 0):
    print("even")
else:
    print("odd")    

#2. find greatest of 3 numbers
a=int(input())
b=int(input())
c=int(input())
if( a>b and a>c ):
    print(a)
elif( b>a and b>c):
    print(b)
else:
    print(c)  
    
#3. find sum of all the elements in array
arr=list(map(int,input().split()))
sum=arr[0]
for i in range(1,len(arr)):
    sum=sum+arr[i]
print(sum)

#4. *** find the peak element
#prints a single peak elemet
n=list(map(int,input().split()))
peak=0
for i in range(1,len(n)-1):
    if(n[i]>n[i-1] and n[i]>n[i+1]):
        peak=i
        break
print(n[peak],end=" ")#------ if print is writtrn out of if and for with break then it will print one peak element---- to print all peak elements write it inside for and if without break
#OR
#prints more than one peak element
n=list(map(int,input().split()))
for i in range(1,len(n)-1):
    if(n[i]>n[i-1] and n[i]>n[i+1]):
       print(n[i],end=" ")
#OR
#highest peak element
n=list(map(int,input().split()))
peak=0
for i in range(1,len(n)-1):
    if(n[i]>n[i-1] and n[i]>n[i+1]):
        peak=i
if(n[-1]>n[-2] and n[-1]>count):
    count=len(n)-1
print(n[peak]) 

#5. find max in array
arr=list(map(int,input().split()))
max=0
for i in range(len(arr)):
    if(max < arr[i]):
        max = arr[i]
print(max)

#6. find the sum of sqs of given num
n=list(map(int,input().split()))
sum=0
for i in n:
    sum=sum+i**2
print(sum) 

#7. find sum of sqs of even and odd digit seperatly
n=list(map(int,input().split()))
even_sum=0
odd_sum=0
for i in range(len(n)):
    if( n[i]%2 == 0):
        even_sum=even_sum+n[i]**2
    else:
        odd_sum=odd_sum+n[i]**2    
print(even_sum,odd_sum)  

#8. check whether given num is palindrome or not using while loop
n=int(input())
ori=n
rev=0
while(n>0):
    a=n%10
    rev=rev*10+a #since a is in int it must be converted to str
    n=n//10
if( ori == rev):
    print("yes")
else:
    print("no")

#9. print 1st n Fibonacci series
n = int(input(""))
a, b = 0, 1
count = 0
while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1
#26. checking for a prime number
#sq root method is the most optimized method
a=int(input())
r=a**0.5
count=0
if a==1:
    print("No, it is not a Prime Number")
elif a==2:
    print("Yes, it is a Prime Number")    
for i in range(2,int(r+1)):
    if a%i==0:
        count=1
        break
if count==0:
    print("Yes, it is Prime Number")
else:
    print("No, it is not a Prime Number")

#write a program to print all the primr no inn a given range
#try solving in sq root method
start=int(input())
end=int(input())
for i in range(start,end+1):
    for j in range(2,i):
        if i%j==0:
          break
        else:
          print(i)

#5%15-------------5 
    #%-----------to cut the num size
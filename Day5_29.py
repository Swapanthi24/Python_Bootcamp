#29. Write a program to print all the vowles followed by consonants
#example: hello world----eoo hllwrld
str=input()
inp=str.lower()
vol=['a','e','i','o','u']
con="bcdfghjklnmprstvwxyz"
ans=""
for i in str:
    if(i in vol):
        ans+=i
for i in  str:
    if(i in con):
        ans+=i
print(ans) 
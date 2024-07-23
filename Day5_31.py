#31. example: hello 123 world ----output=6
str=input()
inp=str.lower()
vol=['a','e','i','o','u']
check="0123456789"
con="bcdfghjklnmprstvwxyz"
ans=0
for i in str:
    if(i in check):
        ans+=int(i)
print(ans) 

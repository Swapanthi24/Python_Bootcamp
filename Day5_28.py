#28. check many vowles are there in a string
str=input()
vol=['a','e','i','o','u']
count=0
for i in str:
    if(i in vol):
        count+=1
print(count)

#for vowles and consonants
#donot use len- or not in as it also counts spaces
str=input()
inp=str.lower()
vol=['a','e','i','o','u']
con="bcdfghjklnmprstvwxyz"
vol_count=0
con_count=0
for i in str:
    if(i in vol):
        vol_count+=1
for i in  str:
    if(i in con):
        con_count+=1    
print(f"vowles are:{vol_count}, consonants are:{con_count}")
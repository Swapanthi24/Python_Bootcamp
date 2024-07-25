#34. write a code to print all the capital leters in a given string
str=input()
for i in str:
    if(i.isupper()):
        print(i,end=" ")
#OR
str=input()
for i in str:
    if(ord(i)>=65 and ord(i)<=90):
        print(i,end=" ")

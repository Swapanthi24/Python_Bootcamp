#36. input=ABC, skip value=4, output=EFG
str = input()
for i in str:
        if(ord(i)>=65 and ord(i)<=90):
                ans=ord(i)+4
        print(chr(ans),end=" ")
#cannot be done for XYZ so do it in cyclic printing
#OR

'''xyz
x=120+3=123---------->a=97
char(123)
y=121+3=124---------->a=98
char(124)
x=122+3=125---------->a=99
char(125)'''

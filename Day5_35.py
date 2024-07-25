#35. remove brackets from the given expression
#[=91, ]=93, {=123, }=125, (=40, )=41
str = input()
for i in str:
        if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
                pass #used to pass the values
        else:
                print(i,end=" ")
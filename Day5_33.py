
#33. Sum of digits in a number using ascii values 
#example: 123 are given, we need to perform 1+2+3=6, but we need to access with ascii values
n=input()
sum=0
for i in n:
    if(ord(i)>=48 and ord(i)<=57):
        sum+=int(i)
print(sum)

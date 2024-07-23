#21. swap a and b without using any third variable
a=int(input())
b=int(input())
b=b+a
a=b-a
b=b-a
print(a,b)
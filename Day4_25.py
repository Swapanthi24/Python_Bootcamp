#25. LCM
a=int(input("enter the number:"))
b=int(input("enter the number:"))
mul=a*b    #lcm*gcd=a*b
while b!=0:
    a,b=b,a%b
gcd=a
lcm=mul//gcd
print(lcm)
#CM and GCD(HCF)
#24. GCD of 2 numbers ------fixed logic
a=int(input("enter the number:"))
b=int(input("enter the number:"))
while b!=0:
    a,b=b,a%b #assignment opearator-----------a=b and b=a%b
print("the HCF/GCD is",a)


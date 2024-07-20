#operators: binary(operation with more operands) and unary(operation on single operand)
#arithemetic operation
num1=int(input())
num2=int(input())
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)
#integer divion, removes the decimal doesnt round off
print(num1//num2)
#power operator 2 power 3 can be written as 2**3
print(num1**num2)

#logical operators:and(&&),or(||),not
#and->(num1 && num2)
#or->(num1 || num2)
#not->
#problem
age=int(input())
if(age>=18 and  age<24):
    print("allowed to drive only 2 wheeler")
elif(age>=24 and age<45):
    print("allowed for 2 and 4 wheeler")
else:
    print("all")
    
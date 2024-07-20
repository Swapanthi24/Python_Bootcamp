#3.12.7 latest version
#print stmt used to give output
print("Sridevi college")
print("hello")
#by default python prints in new line
#Printing formats:
#1.using print stmt
print("good morning")
#2. to print hello, name( for this we need to store the name in a variable) 
var1="manga"
print("good morning",var1,)
#it could be used anyways 
var2="hi"
print("good morning",var1,"hello",var2)

#to take input values
name=input("enter your name:")
#now the input is entered into the variable name which can we printed
print("hello",name)
#to get it in next line use \n
name=input("enter your name:\n")
print("new")
#**fstring: used to write multiple data types togther
#to take input directlt just put input()
name=input()
age=input("age")
#using fstring
print(f"hello {name} Im {age} years old")
#regular way 
print("hello, I'm",name,"I'm",age,"years old")

#take user name , take marks of 3 sub, print user name,total marks and avg of the marks
# example: hello, swap your marks are 140, avg is 50
name=input()
#here as string is the default type we need to typecast it into integer type
sub1=int(input())
sub2=int(input())
sub3=int(input())
#we could also do it directly by using sub1+sub2+sub3 intead of sum
# best is to store it in sum for code reusability
sum=sub1+sub2+sub3
#avg=float(input()) 
print(f"hello {name} your marks are {sum}, avg is {sum/300}")
#end is used to give space or we could also put anything (desired output format)
var=input()
print(var)
print(var,end=" ")
print(var,end=" @@@")
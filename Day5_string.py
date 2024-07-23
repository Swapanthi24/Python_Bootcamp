#string: a sequence od characters
#string methods:
#isalpha, isdigit, isalam(alpha numeric), isupper, islower, 
#converting to lower, converting to upper, titlecase, swap case, 
str="      haLlo     world"
print(str.lower())#to small
print(str.upper())#to capital
print(str.title())#first letter capital---helo world=Helo World
print(str.swapcase())#viseversa
print(str.strip())#spaces trim at the beging and end
print(str.capitalize())#only the first word first letter is capital--helo world=Helo world
print(str.replace('a','z'))#replace the values
print(str.split())#shows each word seperatly

#using is will check the string and produce true or false, without is we can convert them
str="Helloworld0"
print(str.islower())
print(str.isupper())
print(str.isalpha())#should not have spaces
print(str.isnumeric())#all numbers
print(str.isalnum())#both alphabet and numbers
print(str.isascii())#whether the given input is ascii or not
print(str.isdigit())#only from 0 to 9

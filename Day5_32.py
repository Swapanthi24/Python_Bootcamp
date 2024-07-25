#32. example: hello 123 world ----output=hello 321 world
str=input()
rev=""
temp=""
digits="0123456789"
for char in str:
    if char in digits:
        temp+=char
    else:
        if temp:
            i=len(temp)-1
            while i>=0:
                rev+=temp[i]
                i-=1
            temp=""
        rev+=char
if temp:
    i=len(temp)-1
    while i>=0:
        rev+=temp[i]
        i-=1
print(rev)


#20. password verifier
#MR. X is trying to create a new password for this insta acc these are the req con for creating a new password
#con1 min len is 8 max is 15, con2 only @,/ are allowed in a password, con 3 no spaces are allowed, con 4 only alpha numeric are allowed,
#you are supposed to print weak if length is excat 8, mediun len is btw 8 to 12, strong if len is btw 12 to 15
str=input()
a="@"
b="/"
if( a or b in str):
    if " " not in str:
        if(len(str) == 8):
            print("weak password")
        elif(len(str)>8 and len(str)<=12):
            print("medium password")
        elif(len(str)>12 and len(str)<=15):
            print("strong password")
    else:
        print("please follow the conditions")
else:
    print("please follow the conditions")
#we can use for loops how many times without interlooping them because for+for+for=tc---O(n), but for*for*for=tc----O(n^3)

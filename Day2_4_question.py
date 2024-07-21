#4 take input from the user, choice 1 append, 2 pop, 3 sort, 4 print gm,length of string
my_list=list(map(int,input().split(" ")))
print("press 1 to append\n press 2 to pop\n press 3 to sort\n press 4 to ptint length ")
choice=int(input())
if( choice==1):
    my_list.append(6)
    print(*my_list)
elif( choice==2 ):
    my_list.pop(2)
    print(*my_list)
elif( choice==3):
    my_list.sort()
    print(*my_list)
else:
    print("gm",len(my_list)) 
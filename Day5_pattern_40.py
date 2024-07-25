#40. print upper triangular matrix
for i in range(4):
    for j in range(4):
        if(i>j):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
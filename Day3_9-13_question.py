#9 find the elements that is present in k+N index
# k is given by user k=3, input paramets are {3 6 8 4 61 2} and N=2
#k=3 n=4 { 80 70 54 72 } Output=error
my_list=list(map(int,input().split()))
k=int(input())
n=int(input())
for i in range(0,len(my_list)):
       print(my_list[k+n])
       break #break used to stop ietrating in between
if( k+n > len(my_list)):
     print("error")

#10 print the element in a particular index, but the condi is cyclic printing
my_list=list(map(int,input().split(" ")))
k=int(input())
index = k-len(my_list)
for i in range(0,len(my_list)):
       print(my_list[index])
       break
#if input size is more then then it will error in this method

#OR
my_list=list(map(int,input().split(" ")))
k=int(input())
index = k%len(my_list)
for i in range(0,len(my_list)):
       print(my_list[index])
       break 
# we could use for and break or not use aswell

#*****11. find the max element in a given list-------tc=O(n)
# 12 23 36 44 45 57----
#val=my_list.sort()------ no sort function as tc of sort is O(nlogn)
my_list=list(map(int,input().split(" ")))
temp=my_list[0]
for i in range(0,len(my_list)):
    if( temp < my_list[i]):
       temp = my_list[i]
print(temp)

#12. write the code for min element
my_list=list(map(int,input().split(" ")))
temp=my_list[0]
for i in range(0,len(my_list)):
    if( temp > my_list[i]):
       temp = my_list[i]
print(temp)

#13. replace the elements in a array with avg of max and min element
my_list=list(map(int,input().split(" ")))
max=my_list[0]
min=my_list[0]
for i in range(len(my_list)):
    if( max < my_list[i]):
        max = my_list[i]
    elif(min > my_list[i]):
        min = my_list[i]
avg=(max+min)//2        
for i in range(len(my_list)):
        my_list[i] = avg
print(*my_list)


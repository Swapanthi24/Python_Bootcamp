#list are ordered, sets are unorded
#list declaration
#lists are declared with square brackets and commos
my_list=[1,2,3,4]
print(my_list)

my_list.append(123456)#performing append to add at the end
print(*my_list)
#adding star will remove the bracket and commas

my_list.insert(0,999)
#(position, value to be inserted)
print(*my_list)
my_list.insert(8000,999)#if there is no 8000 position it will insert at end 
print(*my_list)

print(len(my_list))
#to print the lenght of the list

my_list.pop()#if ntg specific is mentioned then it pops the last value
print(my_list)
my_list.pop(4)# specific index is poped
print(*my_list)
#my_list.pop(11)------if the specified index is not there it will throw error
#print(*my_list)

my_list2=[5,6,7,8]
#adding list 1 and list 2( wipro interview Question)
new_list=my_list+my_list2
print(new_list)
new_list.pop()
print(*new_list)

#count returns the number of times a number is repeated in a list
cnt=new_list.count(2)
print(cnt)

#sorting
my_list.sort()
print(*my_list)
#TC of quick sort is nlogn

#to take dynaamic input-------**-------
my_list=list(map(int,input().split(" ")))
print(*my_list)
#my_list=list(map(int,input().split(",")))
#print(*my_list)

    
    
















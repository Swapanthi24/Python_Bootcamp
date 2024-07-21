#7.1 you are given with , seperated natural numbers 1 to 10, print only even numbers
my_list=list(map(int,input().split(",")))
for i in range (1,len(my_list),2):
    print(my_list[i])

#7.2 how many even numbers are there in the above question
my_list=list(map(int,input().split(",")))
count=0
for i in range (len(my_list)):
    if(my_list[i]%2 == 0):
        count+=1
print(count)      

#7.3 you are given with a space separated integer list, num of even elements and no. of odd elements in a given list
my_list=list(map(int,input().split(",")))
even=0
odd=0
for i in range(0,len(my_list)):
     if( my_list[i]%2 == 0):
           even+=1
     else:
          odd+=1
print(even,odd)

#8. given an space seperated integer list find the avg of elements present in the even index 
my_list=list(map(int,input().split(" ")))
sum=0
count=0
for i in range(len(my_list)):
    if(i%2 == 0):
          sum+=my_list[i]
          count+=1
print(sum/count)          


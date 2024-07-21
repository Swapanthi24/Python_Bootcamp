#5.1 using for loop print 1 to 100 numbers
for i in range(1,101):#(inistal value is considered, final value is not consisderd)
#for i in range(1,n+1)----when n=100   
   print(i,end=" ") 

#5.1 using for loop append 1 to 100 numbers in an empty list
n=[]#creating an empty list
for i in range(1,101):
    n.append(i)#appending the list
print(n)

#5.3 sum of all the numbers in a list by using for loop
my_list=list(map(int,input().split(" ")))
sum=0
for i in range(len(my_list)):
    sum+=my_list[i]
print(sum)    

#6. take space seperated input from a user and print atlernate elements
my_list=list(map(int,input().split()))
for i in range (0,len(my_list),2):#the last one is step count since we want atternative we take step count as 2
    print(my_list[i],end=" ")

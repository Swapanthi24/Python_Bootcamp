#14. find the missing nnumber in an array 
#my_list=list(map(int,input().split(" ")))
n=list(map(int,input().split(" ")))
exp_sum=0
for i in range(1,len(n)+2):
        exp_sum += i
act_sum=0        
for j in n:
    act_sum += j
miss = exp_sum-act_sum  
print(miss)

#15. find the duplicates in an array-----O(n)
my_list=list(map(int,input().split()))
new_list=[]
for i in my_list:
    if( i not in new_list ):
        new_list.append(i)
print(*new_list)





             








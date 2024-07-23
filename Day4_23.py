#23. sort the elements : 1st half in ascending order and 2nd half in descending order
my_list=list(map(int, input().split()))
middle=len(my_list)//2
first=my_list[:middle]
second=my_list[middle:]
for i in range(len(first)):
    for j in range(i+1,len(first)):
        if first[i]>first[j]:
            first[i],first[j]=first[j],first[i]
for i in range(len(second)):
    for j in range(i+1,len(second)):
        if second[i]<second[j]:
            second[i],second[j]=second[j],second[i]
result=first+second
print(result)
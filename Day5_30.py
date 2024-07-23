#30. print the non reapting characters in a string/ print the unique characters in a string
str=input()
ans=""
for i in str:
    if(i not in ans):
        ans+=i
print(ans) 

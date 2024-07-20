#conditional stmts: checks the condition, if, elif, else
#take name of user take age input, check eligibity for voting, if yes name,age,eligible for voting
name=input()
age=int(input())
if(age >= 18):
  print(name,"eligible for voting")
#we could also use fstring
else:
  print("cannot vote")
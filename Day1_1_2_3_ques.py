#1. person x goes to market, buy 10 apples, 2 dozen bananas(24), 8 oranges, the cost of each apple is 15/-, 1 banana =  4/-, 1 orange = 5/-, mother of X is mrs Y, she gave x 700/- to x. she said some amt will be left over with x if x is left with money then fruit vendor cannot fooled the kid
apple=int(input())
banana=int(input())
orange=int(input())
total=apple*15+banana*4+orange*5
if(total<700):
  print("not cheated")
else:
  print("cheated")
  
#2. take input from user and check whether the given number is positive and even, posi and odd, neg and even, neg and odd
number=int(input())
if(number>=0 and number%2==0):
  print("posi and even")
elif(number>=0 and number%2!=0):
  print("posi and odd")
elif(number<0 and number%2==0):
  print("neg and even")
else:
  print("neg and odd")
  
#3 Mr Z is selected for olympics he is participating in swiming compitation only one winner is slected among all the participants, anyhow he got selected.
#Mr X and Y are frnds of Z. Mr X is participating in badminton and Mr Y is table  tennis.
#acc to selection committe the req for badminton players are height=140cm, weight= factor of 2, body fat= less than 12%.
#acc to selection commiittee req for table tennis are height = min 118cm to 148cm, weight= factors of no of medals won by Mr Z, body fat= 14%.
#acc to the previous history z participated in 14 games out of which he is having success rate of 50% now
#write a program to check Mr X, Mr Y, Mr Z from India will travel in a same train or not ( there is only one train so check if they are selected or not)
height=int(input())
weight=int(input())
#bodyfat is not required
if ( height == 140 and weight%2 == 0 ):
    print("same train")
elif ( height>=118 or height>=148 and weight%7 == 0 ):
    print("same train")
else:
    print("not same train")
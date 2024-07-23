#27. find the leap year
#number shpould be dividble by 400 or  divisible by 4 but not in 100
year=int(input())
if( year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 ):
    print("It is a leap year")
else:
    print("It is not a leap year")

#find leap year when given a range
year=int(input())
if(2000<=year and year<=2025):
    print("the given year is out of range")
else:    
    if(year % 4 == 0 and year % 100 != 0) or (year%400 == 0):
        print("it is a leap year")
    else:
        print("it is not a leap year")
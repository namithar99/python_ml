year = int(input("enter a year:"))
if(year%4 == 0 and year%100 == 0 and year%400 == 0):
     print("yes a leap year")
else:
    print("not a leap year")


year = int(input("enter a year"))
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("yes a leap year")
        else:
            print("not a leap year")
    else:
        print("not a leap year")
else:
    print("not a leap year")








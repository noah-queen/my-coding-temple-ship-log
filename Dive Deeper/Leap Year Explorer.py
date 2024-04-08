var_year = int (input("please input a year to check for leap year"))
if (var_year % 4 == 0 and var_year % 100 != 0) or var_year % 400 == 0:
    print("this is a leap year")
else: print("this is not a leap year")
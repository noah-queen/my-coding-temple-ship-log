#Task 1
first_number = int (input("enter your first number"))
second_number = int (input("enter your second number"))
third_number = int (input("enter your third number"))

if first_number > second_number and first_number > third_number :
    print(first_number)
elif second_number > first_number and second_number > third_number:
    print(second_number)
elif third_number > first_number and third_number > second_number:
    print(third_number)

#Task 2

first_number = int (input("enter your first number"))
second_number = int (input("enter your second number"))
third_number = int (input("enter your third number"))

if first_number < second_number and first_number < third_number :
    print(first_number)
elif second_number < first_number and second_number < third_number:
    print(second_number)
elif third_number < first_number and third_number < second_number:
    print(third_number)

#Task 3
first_number = int (input("enter your first number"))
second_number = int (input("enter your second number"))
third_number = int (input("enter your third number"))

if first_number > second_number and first_number > third_number :
    print("the first number", first_number, "is biggest")
elif second_number > first_number and second_number > third_number:
    print("the second number", second_number, "is biggest")
elif third_number > first_number and third_number > second_number:
    print("the third number", third_number, "is biggest")
elif first_number == second_number and first_number > third_number:
    print("the first and second numbers are", first_number, "and greater than the third!", third_number)
elif first_number == third_number and first_number > second_number:
    print("the first and third numbers are", first_number, "and are equal and greater than the second!", second_number)
elif second_number == third_number and second_number > first_number:
    print("the second and third numbers are", second_number, "and are equal and greater than the first!", first_number)
elif first_number == second_number == third_number:
    print("all the numbers are", first_number)
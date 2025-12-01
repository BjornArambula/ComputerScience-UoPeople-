# Chained Conditional Example
def chained_conditional():
    print("This is the chained conditional example")
    number = int(input("Enter a number: "))

    if number <= 10:
        print("Number is less than or equal to 10")
    elif number <= 20:
        print("Number is between 11 and 20")
    else:
        print("Number is greater than 20")


chained_conditional()


# Nested Conditional Example
def nested_conditional():
    print("This is the nested conditional example")
    number = int(input("Enter a number: "))
    if number == 21:
        print("You found the magic number")
    else:
        if number <= 10:
            print("Number is less than or equal to 10")
        elif number <= 20:
            print("Number is less than or equal to 20")
        else:
            print("Number is greater than 20")


nested_conditional()


def simplified_version(number):
    # All conditions are now on the same level, removing the nested indentation.
    print("This is the simplied version of the chained conditional")
    if number == 21:
        print("You found the magic number (21)")
    elif number <= 10:
        print("Number is less than or equal to 10")
    elif number <= 20:
        print("Number is less than or equal to 20")
    else:
        print("Number is greater than 20")


simplified_version(10)
simplified_version(21)
simplified_version(20)

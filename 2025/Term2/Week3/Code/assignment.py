# Q1
def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)


def count_up(number):
    if number == 0:
        print("Blastoff!")
    else:
        print(number)
        count_up(number + 1)


def counting():  # checking for a positive number, or negative number, then calls the function necessary.
    num = int(input("Enter any number: "))
    if num < 0:
        count_up(num)
    elif num > 0:
        countdown(num)
    else:
        countdown(
            0
        )  # Chose countdown just simply because it is the top level function.


counting()
counting()


# Q2
def division(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(result)


division(int(input("Enter numerator: ")), 0) #Forced ZeroDivisionError to show exception handling
division(int(input("Enter numerator: ")), int(input("Enter denominator: ")))

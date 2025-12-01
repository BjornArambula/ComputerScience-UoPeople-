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
        countdown(0)


counting()

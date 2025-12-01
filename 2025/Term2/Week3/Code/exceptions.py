# Code from https://www.youtube.com/watch?v=V_NXT2-QIlE

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter only numbers please!")

finally:
    print("Do some cleanup here")

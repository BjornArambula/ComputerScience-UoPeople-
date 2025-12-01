def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)


countdown(10)


def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n - 1)


print_n("Help Me!!", 10)

text = "Please enter any number "
number = int(input(text))
print(number)

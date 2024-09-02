# print(*objects, sep=' ', end='\n', file=sys.stdout, flush = False)

name = input("Enter your name: ").strip().capitalize()
print(f'Your name is {name}')

title = input("Enter sentence: ").title()
print(title)

#adding 2 numbers in one line
print(int(input("What's number 1: ")) + int(input("Enter the 2nd number: ")))

# round(number[, ndigits])

x = float(input())
y = float(input())
z = x / y
print(f"{z:.3f}")     #it will put comma in between
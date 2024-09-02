def main():
    x = int(input("Enter input 1: "))
    y = int(input("Enter input 2: "))
    print(f"The output is {square(x, y)}")

def square(a, b):
    c = (a+b)**2   #OR pow((a+b), 2)
    return c

main()
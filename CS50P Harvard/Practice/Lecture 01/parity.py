def main():
    x = int(input("Enter number: "))
    if x_even(x):
        print("Even")
    else:
        print("Odd")

def x_even(a):
    #OR   return True if a % 2 == 0 else False
    return a % 2 == 0

main()
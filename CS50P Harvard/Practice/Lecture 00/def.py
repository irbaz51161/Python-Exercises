def main():
    hello()
    name = input("What's your name? ").title()
    hello(name)

def hello(to = 'world'):
    print(f"Hello, {to}")

main()
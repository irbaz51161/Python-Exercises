def palindrome(str):
    if str[::-1] == str:
        print("Yes! The given word is palindrome!")
    else:
        print("No! It's not a palindrome!")

def again():
    againn = input("Do you want to check again? Y/N ")
    if againn.upper() == 'Y':
        string1 = input("Enter string: ")
        palindrome(string1)
        again()
    else:
        print("See you soon :)")

string = input("Enter string: ")
palindrome(string)
again()
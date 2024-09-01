user_input=input("Enter words: ")
if list(user_input) == list(user_input[::-1]):
    print('True')
else:
    print('False')
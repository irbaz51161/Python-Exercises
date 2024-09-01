word = input("Enter a word: ")
if len(word) > 3:
    print(word[:3]+word[-3:])
else:
    print('')
def anagramss(input1, input2):
    short1 = input1.replace(" ","").lower()
    short2 = input2.replace(" ","").lower()
    
    sort1 = sorted(short1)
    sort2 = sorted(short2)

    if sort1 == sort2:
        print("Yes it is anagrams.")
    else:
        print("No these are not anagrams.")

i1 = input("Enter the input: ")
i2 = input("Enter the 2nd input: ")

anagramss(i1, i2)
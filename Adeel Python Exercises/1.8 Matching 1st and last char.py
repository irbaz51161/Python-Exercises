def taking_user_list(abc, mno):
    for i in range(abc):
        a = input("Enter word: ")
        mno.append(a)
    print(f"Your created list is: {mno}")

def matching(mno):
    count=0
    for words in for_list:
        if len(words) >= 2 and words[0] == words[-1]:
            count+=1
    print(f"Number of matching words: {count}")

word = int(input("How many words you want to enter into the list: "))
for_list = []

taking_user_list(word, for_list)   #Function=1

matching(for_list)           #Function=2
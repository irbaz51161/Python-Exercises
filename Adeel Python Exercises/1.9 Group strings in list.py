def user_list_take(abc):
    for i in range(1, abc+1):
        a = input(f"Enter word {i}: ")
        user_list.append(a)
    print(user_list)

def sort(abc):
    b = sorted(user_list)
    print(b)
num = int(input("How many words you want to enter into the list: "))
user_list = []

user_list_take(num)
sort(user_list)
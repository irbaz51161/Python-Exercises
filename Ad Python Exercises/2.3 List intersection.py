def comparing(l1,l2):
    common = []
    if l1 == l2:
        print("The commom integers in the both list are:", l1)
    else:
        for element in l1:
            if element in l2 and element not in common:
                common.append(element)

        print("The commom integers in the both list are: ", common)


l = int(input("How many numbers you want to enter into the list? : "))
list1 = []
for _ in range(1, l+1):
    num = int(input(f"Enter number {_}: "))
    list1.append(num)
m = int(input("How many numbers you want to enter into the list? : "))
list2 = []
for _ in range(1, m+1):
    num0 = int(input(f"Enter number {_}: "))
    list2.append(num0)

print("List#01", list1)
print("List#02", list2)


comparing(list1, list2)
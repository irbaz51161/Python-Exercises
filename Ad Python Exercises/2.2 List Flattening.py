def flatten_list(l):
    flat_list = []
    for i in l:
        flat_list.extend(i)
    print(*flat_list)

    #  OR

    for i in l:
        flat_list += i
    print(*flat_list)
    
list = [[1,2,3],[4,5],[788,9,34]]
flatten_list(list)
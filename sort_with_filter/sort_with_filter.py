lst = [x for x in range(101)]

filtered_lst = filter(lambda x: x % 2 == 0 and x !=0, lst)

print([x for x in filtered_lst])

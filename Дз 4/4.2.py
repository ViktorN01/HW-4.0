list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [list[n] for n in range(1, len(list)) if list[n] > list[n - 1]]
print(new_list)

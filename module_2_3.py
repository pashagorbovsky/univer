my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
k = len(my_list)
n = 0
while not n == k:
    if my_list[n] < 0:
        break
    elif my_list[n] == 0:
        n = n + 1
        continue
    else:
        print(my_list[n])
        n = n + 1

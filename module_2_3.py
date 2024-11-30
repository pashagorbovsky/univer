my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
k = len(my_list)
n = 0
while not n == k:
    if my_list[n] > 10:
        print(my_list[n])
        n = n + 1
    else:
        n = n + 1
immutable_var = 1, False, 'Saints-Petersburg', 0.423
print(immutable_var)
#immutable_var[2] = 'Moscow'
# #TypeError: 'tuple' object does not support item assignment
mutable_list = [1, False, 'Saints-Petersburg', 0.423]
mutable_list[0] = mutable_list[1] + 0.5
mutable_list[1] = True
mutable_list[2] = (mutable_list[2][1:-1:3].upper())
mutable_list[-1] = int(mutable_list[-1] // 1)
print(mutable_list)



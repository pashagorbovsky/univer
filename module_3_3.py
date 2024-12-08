def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [5, 'monday', [1, 2, 3]]
values_dict = {'a': 2331,'b': 'thusday','c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [25, 'wednasday']
print_params(*values_list_2, 42)

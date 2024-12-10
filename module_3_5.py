def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    elif not len(str_number) > 1:
        if first == 0:
            first = 1
        return first


result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
result2 = get_multiplied_digits(4172002500)
print(result2)
result2 = get_multiplied_digits(132588)
print(result2)


data_structure = [

  [1, 2, 3],

  {'a': 4, 'b': 5},

  (6, {'cube': 7, 'drum': 8}),

  "Hello",

  ((), [{(2, 'Urban', ('Urban2', 35))}])

]

def calculate_structure_sum(args):
    sum1 = 0
    sum2 = 0
    for i in args:
        if isinstance(i, int):
            sum1 += i
        if isinstance(i, str):
            sum2 += len(i)
        if isinstance(i, list):
            res = calculate_structure_sum(i)
            sum1 += res[0]
            sum2 += res[1]
        if isinstance(i, set):
            i = list(i)
            res = calculate_structure_sum(i)
            sum1 += res[0]
            sum2 += res[1]
        if isinstance(i, tuple):
            res = calculate_structure_sum(i)
            sum1 += res[0]
            sum2 += res[1]
        if isinstance(i, dict):
            for k in i.values():
                sum1 += k
            for j in i.keys():
                sum2 += len(j)
    return sum1, sum2


result = calculate_structure_sum(data_structure)

print(result)
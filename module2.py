num = list(range(3,21))
passwords = dict()

for i in num:
    key = str()
    for j in range(1,i):
        for k in range(1,i):
            if j < k and j != k and  i % (j + k) == 0:
                key = key + str(j) + str(k)
    passwords.update({i:key})

n = int(input('Введите число от 3 до 20: '))
if n in range(3,21):
    print(passwords[n])
else:
    print('Мимо')


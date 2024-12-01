numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = set({})
not_primes = set({})
for i in numbers:
    for j in range(1,i):
        if i % j == 0 and i != 1 and i > j != 1:
            not_primes.update({i})
        else:
            primes.update({i})

primes = primes - not_primes
print('Primes: ',(list(primes)))
print('Not Primes: ',(list(not_primes)))








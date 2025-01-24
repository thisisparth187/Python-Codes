def fibb(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)

num_terms = int(input('Enter number of terms: '))

for i in range(num_terms):
    print(fibb(i), end=' ')
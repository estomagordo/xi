from collections import defaultdict
from itertools import product


def is_prime(n):
    for x in range(2, int(n**0.5) + 2):
        if n % x == 0:
            return False

for x in range(10000):
    if x % 100 == 0:
        print(x)
    s = str(x)
    
    if len(s) < 4:
        s = '0' * (4 - len(s)) + s

    for d in range(10):
        for p in product(range(7), repeat=4):
            t = [str(d)] * 6
            u = [[]] * 7

            for i, q in enumerate(p):
                u[q].append(s[i])

            w = []

            for j in range(11):
                if j % 2 == 0:
                    for cell in u[j // 2]:
                        w.append(cell)
                else:
                    w.append(t[j // 2])

            if w[0] == '0':
                continue

            num = int(''.join(w))

            if is_prime(num):
                print(num)
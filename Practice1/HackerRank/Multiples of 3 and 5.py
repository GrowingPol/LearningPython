from functools import lru_cache

t = int(input().strip())
if t <= 10 ** 5:

    for a0 in range(t):
        n = int(input().strip())
        if n <= 10 ** 9:

            numSum = 0
            for i in range(0, n, 5):
                numSum += i

            for i in range(0,n, 3):
                if i % 5 != 0:
                    numSum += i

            print(numSum)
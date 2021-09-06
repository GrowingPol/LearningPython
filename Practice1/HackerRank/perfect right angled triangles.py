import math

#Not accomplished yet
def noSuperPerfect(query, bound):
    a = 7
    b = 24
    c = 1
    superp = 0

    for i in range(1, n + 1):
        c = i
        squareC = math.sqrt(c)
        area = a * b * c
        print(c % squareC)

        if c % squareC == 0 and math.gcd(a,b) == 1 and math.gcd(b,c) == 1:
            if area % 6 == 0 and area % 28 == 0:
                superp += 1

    print(n - superp)


if __name__ == "__main__":
    q = int(input())
    n = int(input())
    noSuperPerfect(q, n)
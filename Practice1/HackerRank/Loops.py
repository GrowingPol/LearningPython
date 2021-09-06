def squareIntNum(number):
    num = 0
    while num < number:
        print(num**2)
        num += 1

if __name__ == '__main__':
    n = int(input())
    squareIntNum(n)

print
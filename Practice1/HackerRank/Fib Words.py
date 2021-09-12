#Do not support long numbers calculation :c

import sys
sys.setrecursionlimit(5000)

def fib(n):
    if n == 1:
        return 'B'
    elif n == 0:
        return 'A'
    else:
        return str(fib(n-2)) + str(fib(n-1))

if __name__ == "__main__":

    triples = []
    fibList= []
    A = 'A'
    B = 'B'

    #input data
    for i in range(int(input())):

        triples = list(input().split(' '))
        A2 = str(triples[0])
        B2 = str(triples[1])
        n = int(triples[2])

        fibList.append(A)
        fibList.append(B)
        counter = 2
        fibListLen =len(A2) + len(B2)

        #declare variables
        fibString = ''
        counterA = 0
        counterB = 0
        totalLen = 0
        totalLenTemp = 0
        finalWord = ''
        print(f"lenA: {len(A2)}, lenB: {len(B2)}")


        #append fibonnaci words to list until len of the last column exceed n
        if len(A2) <= 100 and len(B2) <= 100 and n <= 2**100:
            for i in range((n//max(len(A2),len(B2))),n,1):
                fibListLen = 0
                fibString = fib(i)
                for char in fibString:
                    if char == 'A':
                        fibListLen = fibListLen + len(A2)
                    elif char == 'B':
                        fibListLen = fibListLen + len(B2)
                if fibListLen > n:
                    break

            print(f"fibString {fibString}")
            #Obtain word and position of word where n position is situated
            for char in fibString:
                if char == 'A':
                    totalLenTemp = totalLenTemp + len(A2)
                    if totalLenTemp < n:
                        totalLen = totalLen + len(A2)
                    else:
                        finalWord = A
                elif char == 'B':
                    totalLenTemp = totalLenTemp + len(B2)
                    if totalLenTemp < n:
                        totalLen = totalLen + len(B2)
                    else:
                        finalWord = B

            print(f"totalLen: {totalLen}, finalWord: {finalWord}")
            #Find n position and get value
            if finalWord == A:
                for char in A2:
                    totalLen += 1
                    if totalLen == n-1:
                        fibResult = char
            elif finalWord == B:
                for char in B2:
                    totalLen += 1
                    if totalLen == n-1:
                        fibResult = char
            #Print Result
            print(fibResult)






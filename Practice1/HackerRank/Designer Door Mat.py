# Enter your code here. Read input from STDIN. Print output to STDOUT
matrix = input().split(' ')
N = int(matrix[0])
M = int(matrix[1])


#Top figures
figCount = 3
for i in range((int((N-1)/2))):
    if i == 0:
        print(('.|.'*(i+1)).center(M,'-'))
    else:
        print(('.|.' * figCount).center(M, '-'))
        figCount += 2
#Center Message
print('WELCOME'.center(M,'-'))
#Bottom figures
figCount -= 2
for i in range((int((N-1)/2)),0,-1):
    if i == int((N-1)/2):
        print(('.|.'*figCount).center(M,'-'))
    else:
        figCount -= 2
        print(('.|.' * figCount).center(M, '-'))

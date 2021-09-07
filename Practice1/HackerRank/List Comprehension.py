# Print a list of all possible coordinates given by i,j,k  on a 3D grid where the sum
# of i+j+k is not equal to n. Here, 0>=i<=x, 0>=j<=y, 0>=k<=z,. Please use list comprehensions
# rather than multiple loops, as a learning exercise.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # This is a list comprehension: [[expression] iterations condition]

    list1 = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k != n]
    print(list1)

    #Another example
# saludos = ['hola', 'saludos', 'hi']
# nombres = ['j2logo', 'antonio', 'vega']
# frases = ['[{} {}]'.format(saludo.title(), nombre.title()) for saludo in saludos for nombre in nombres]
# print(frases)
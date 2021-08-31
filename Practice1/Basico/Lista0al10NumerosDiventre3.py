variable = [0,0,0,0,0,0,0,0,0,0,0]

for i in range(0,11,1):
    variable[i] = i
    if (variable[i] % 3) != 0:
        continue
    print(variable[i])
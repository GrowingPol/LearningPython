def solve(s):
    newString = ''
    charCount = 0
    spaceChar = 0

    for char in s:
        if charCount == 0:
            newString += char.upper()
            charCount = 1
            continue
        if char == ' ':
            spaceChar = 1
            newString += char
            continue
        if spaceChar == 1:
            newString += char.upper()
            spaceChar = 0
            continue
        newString += char

    return newString


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)



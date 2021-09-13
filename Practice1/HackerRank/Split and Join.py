def split_and_join(line):
    list1 = line.split(' ')
    list1 = '-'.join(list1)
    return list1

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
def mutate_string(string, position, character):
    string_list = [char for char in string]
    string_list[position] = character
    string_list = "".join(string_list)
    return string_list

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
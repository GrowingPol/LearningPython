def swap_case(s):
    swap_string = ""
    for char in s:
        if char.isupper():
            swap_string += char.lower()
        else:
            swap_string += char.upper()
    return swap_string


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
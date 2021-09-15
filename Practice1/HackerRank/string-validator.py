if __name__ == "__main__":
    s = str(input())
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))


#-------------------------------------First attempt
# if __name__ == '__main__':
#     s = str(input())
#     alnum = False
#     alpha = False
#     digit = False
#     lower = False
#     upper = False
#     for char in s:
#         alnum = True if char.isalnum() else alnum
#         alpha = True if char.isalpha() else alpha
#         digit = True if char.isdigit() else digit
#         lower = True if char.islower() else lower
#         upper = True if char.isupper() else upper
#
#     print(alnum)
#     print(alpha)
#     print(digit)
#     print(lower)
#     print(upper)
def count_substring(string, sub_string):

    if sub_string in string:
        sub_string_found = 0
        i = 0
        last_index_found = -1

        while i <= len(string):
            substring_index = string.find(sub_string,i,len(string))
            if substring_index >= 0 and substring_index != last_index_found:
                sub_string_found += 1
                last_index_found = substring_index
                i += 1
            else:
                i += 1
        return sub_string_found
    else:
        return 0

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
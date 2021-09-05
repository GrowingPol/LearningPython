if __name__ == '__main__':
    while True:
        try:
            #input values for numbers
            a = int(input("Input an integer number for a: "))
            b = int(input("Input an integer number for b: "))
            break
        except Exception as e:
            print(f"Input a valid number. Error: {e}")

    #print integer division
    print(a//b)
    #Print float Division
    print(a/b)






# Task
# The provided code stub reads two integers,  and , from STDIN.
#
# Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .
#
# No rounding or formatting is necessary.
#
# Example
#
#
# The result of the integer division .
# The result of the float division is .
# Print:
#
# 0
# 0.6
# Input Format
#
# The first line contains the first integer, .
# The second line contains the second integer, .
#
# Output Format
#
# Print the two lines as described above.
#
# Sample Input 0
#
# 4
# 3
# Sample Output 0
#
# 1
# 1.33333333333
if __name__ == '__main__':
    while True:
        try:
            #Input values for a and b
            a = int(input("Enter an integer number for a: "))
            b = int(input("Enter an integer number for b: "))

            if a >= 1 and a <= 10 ** 10 and b >= 1 and b <= 10 ** 10:
            # If values are within the range (1>= n <=10^10) exit loop
                break
            else:
            # If values are not within the range, indicate which one is wrong
                if a < 1 or a > 10 ** 10:
                    print("a number is not within the admisible range")
                if b < 1 or b > 10 ** 10:
                    print("b number is not within the admisible range")
        except Exception as e:
            print(f"Please, input a valid number. Error: {e}")

    #Print results: Sum, Rest and Product
    print(a + b)
    print(a - b)
    print(a * b)

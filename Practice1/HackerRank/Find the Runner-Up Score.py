


if __name__ == "__main__":
    #Initialize list
    list1 = []

    #ask for number of participants
    n = int(input("Participants: "))
    if n <=10 and n>=2:

        #Ask for score of participants and convert data to int
        list1 = input().split(" ")
        list1 = list(map(int,list1))

        #Sort list and print last(upper score)
        list1.sort(reverse=True)
        bestScore = list1[0]
        for score in list1:
            if score < bestScore:
                runnerUp = score
                break
        else:
            runnerUp = bestScore

        print(runnerUp)

    else:
        print("Limit n exceeded")


# Estructura de map() -----> map(Fuction,Which variable is going to be affected)
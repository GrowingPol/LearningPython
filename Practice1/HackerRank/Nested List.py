# Given the names and grades for each student in a class of n  students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically
# and print each name on a new line.

if __name__ == '__main__':
    studentsList = []
    #Input data and create studentsList
    for _ in range(int(input())):
        tempList = []
        name = input()
        score = float(input())
        tempList.append(name)
        tempList.append(score)
        studentsList.append(tempList)

    # Find out the second lowest grade
    firstScore = ['',999]
    secondScore = ['',999]
    for i in range(1,3):
        if i==1:
            #Find the lowest grade
            for student in studentsList:
                if student[1] < firstScore[1]:
                    firstScore = student
        elif i==2:
            #find lowest second grade
            for student in studentsList:
                if student[1] > firstScore[1] and student[1] < secondScore[1]:
                    secondScore = student

    #sort and print results
    studentsList = sorted(studentsList)
    for student in studentsList:
        if student[1] == secondScore[1]:
            print(student[0])


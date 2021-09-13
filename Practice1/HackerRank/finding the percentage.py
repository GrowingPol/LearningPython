# if __name__ == "__main__":
#     dict1 = {}
#     markAverage = {}
#     #Ask for number of students
#     n = int(input())
#     #input scores of each student
#     for inputs in range(n):
#         list1 = input().split(" ")
#         dict1[list1[0]] = list1[1:]
#     query_name = input()
#     #assign student keys to another dict
#     markAverage = dict1
#     for item in markAverage:
#         numberOfScores = len(markAverage[item])
#         scoreSum = 0
#         #update item values with average score
#         for score in markAverage[item]:
#             scoreSum = scoreSum + float(score)
#
#         average = float(scoreSum)/float(numberOfScores)
#         markAverage[item] = format(average,'.2f')
#
#
#     print(markAverage[query_name])

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    student_averages = {}
    for _ in range(n):
        name, *line = input().split(' ')
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    #Assign Average of each student
    student_averages = student_marks
    for item in student_marks:
        numberOfScores = len(student_marks[item])
        scoreSum = 0
        #update item values with average score
        for score in student_marks[item]:
            scoreSum = scoreSum + float(score)
        average = float(scoreSum)/float(numberOfScores)
        student_marks[item] = format(average,'.2f')


    print(student_marks[query_name])
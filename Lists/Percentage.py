def sub_jects(points):
    sum_of_points=sum(points)
    total_subjects=len(points)
    total_points=int(60)
    average_points = sum_of_points / total_points * 100
    roundednumber = round(average_points, 2)
    print("Your Average-points are=",roundednumber)

points=[9,10,7,10,10,9]
sub_jects(points)


points=10

'''Grades of Subjects '''
def Grades_010():
    if points >= 10:
        print("Grade A1  ")
    elif points >= 9:
        print("Grade A2  ")
    elif points >= 8:
        print("Grade B1  ")
    elif points >= 7:
        print("Grade B2  ")
    elif points >= 6:
        print("Grade C1 ")
    elif points >= 5:
        print("Grade C2 ")
    else:
        print("Grade F   ")

Grades_010()









def sub_jects(points):
    sum_of_points=sum(points)
    total_subjects=len(points)
    total_points=int(60)
    average_points = sum_of_points / total_points * 100
    roundednumber = round(average_points, 2)
    print("Your Average-points are=",roundednumber)

points=[9,10,7,10,10,9]
sub_jects(points)


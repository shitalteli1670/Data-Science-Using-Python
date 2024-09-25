points = [(1,2),(3,4),(5,6),(7,8)]
sum_of_distances=0

for i in range(len(points)):
    for j in range(i+1,len(points)):

        distance = 0
        for k in range(len(points[0])):
            distance += abs(points[i][k] - points[j][k])

            sum_of_distances += distance
print("\n Sum of Manhatten Distance between all pairs of points :-",sum_of_distances)

    
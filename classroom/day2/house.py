town = "Chon-Aryk"
build_mat = "Bricks"
area = "350m2"
cost = "45.000$ "

town1 = "Baitik"
build_mat1 = "Sand Block"
area1 = "500m2"
cost1 = "38.000$"

town2 = "Orto-Sai"
build_mat2 = "Bricks"
area2 = "200m2"
cost2 = "50.000$"

house1 = [town, build_mat, area, cost]
house2 = [town1, build_mat, area1, cost1]
house3 = [town2, build_mat2, area2, cost2]

print (",".join(house1))
user = int(input("Would you like to see more houses? Ans:1 or 0  "))

if user == 1:
    print(",".join(house2))
    print(",".join(house3))
else:
    print("bye!")

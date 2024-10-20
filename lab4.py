import data

# Write your functions for each part in the space below.

# Part 1
def first_element(list_og: list)-> list:
   list_b = []
   for i in range(len(list_og)):
       a = list_og[i][0]
       list_b.append(a)
   return list_b

# Part 2
def x_coordinates(lista: list) -> list:
    list_new = []
    for i in range(len(lista)):
      list_new.append(lista[i].x)
    return list_new


# Part 3
def are_in_positive_quadrant(oglist: list) -> list:
    list_new = []
    for i in range(len(oglist)):
        if oglist[i].x > 0 and oglist[i].y > 0:
            list_new.append([oglist[i].x, oglist[i].y])
    return list_new

# Part 4
def distance(point1: float, point2: float) -> float:
    from math import sqrt
    x2 = (point1.x-point2.x)**2
    y2 = (point1.y-point2.y)**2
    Euclidean_distance = sqrt(x2+y2)
    return Euclidean_distance


# Part 5
def manhattan_distance(parameters: list) -> float:
    h = parameters[0].x-parameters[1].x
    j = parameters[0].y-parameters[1].y
    manhattan = abs(h) + abs(j)
    return manhattan

# Part 6
def distance_all(predistance: list) -> list:
    list_of_distances = []
    point1 = data.Point(0,0)
    for point in predistance:
        distances = distance(point, point1)
        list_of_distances.append(distances)
    return list_of_distances

point1 = data.Point(0, 0)
point2 = data.Point(1, 1)
point3 = data.Point(6, 8)
point4 = data.Point(8, 10)

print(distance_all([point1, point2, point3, point4]))







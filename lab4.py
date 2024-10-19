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
def distance(parameters: list) -> float:
    from math import sqrt
    x2 = parameters.x**2
    y2 = parameters.y**2
    Euclidean_distance = sqrt(x2+y2)
    return Euclidean_distance

# Part 5
def manhattan_distance(parameters: list) -> float:
    h = parameters[0].x-parameters[1].x
    j = parameters[0].y-parameters[1].y
    manhattan = abs(h) + abs(j)
    return manhattan

# Part 6
def distance_all(parameters: list) -> list:
   all_distances = []
   origin = data.Point(0,0)
   for i in range(len(parameters)):
        origin_distance = distance([parameters[i], origin])
        all_distances.append(origin_distance)
   return all_distances

point1 = data.Point(3, 4)
point2 = data.Point(1,1)
point3 = data.Point(0,0)

print(distance_all([point1, point2, point3]))







import data

# Write your functions for each part in the space below.

# Part 1
def first_element(list_og: list)-> list:
#the purpose of this function is to return the first element of each nested list, and to create a new list.
#input = the original embedded list.
#output = list_b, which is the new list that has the first element of each nested list.
   list_b = []
   for i in range(len(list_og)):
       a = list_og[i][0]
       list_b.append(a)
   return list_b

# Part 2
def x_coordinates(lista: list) -> list:
#purpose: create a list with all of the x-coordinates from the input list.
#input = original list of the points
#output = the new list with only the x-coordinates of the input.
    list_new = []
    for i in range(len(lista)):
      list_new.append(lista[i].x)
    return list_new


# Part 3
def are_in_positive_quadrant(oglist: list) -> list:
#purpose: to return the points in a new list that are in the positive quadrant.
#input = original list that has points
#output = the points (in a list) from the original list that are in positive quadrant.
    list_new = []
    for i in range(len(oglist)):
        if oglist[i].x > 0 and oglist[i].y > 0:
            list_new.append([oglist[i].x, oglist[i].y])
    return list_new

# Part 4
def distance(point1: float, point2: float) -> float:
#purpose: finding Euclidean distance between two points
#input =  two points.
#output = the euclidean distance as a float.
    from math import sqrt
    x2 = (point1.x-point2.x)**2
    y2 = (point1.y-point2.y)**2
    Euclidean_distance = sqrt(x2+y2)
    return Euclidean_distance


# Part 5
def manhattan_distance(parameters: list) -> float:
#purpose: finding manhattan distance between two points
#input: two points in a list
#output: the manhattan distance as a float.
    if len(parameters)>2:
        return "enter only two points."
    else:
        h = parameters[0].x-parameters[1].x
        j = parameters[0].y-parameters[1].y
        manhattan = abs(h) + abs(j)
        return manhattan

# Part 6
def distance_all(predistance: list) -> list:
#purpose: find the distance of points in a list from the origin, using our distance function
#input: list of points
#output: a list of the distances of inputted points from (0,0).
    list_of_distances = []
    point1 = data.Point(0,0)
    for point in predistance:
        distances = distance(point, point1)
        list_of_distances.append(distances)
    return list_of_distances








import data
import lab4
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        input = [[4, 5, 6], [6, 8,], [7, 8], [8, 9, 100]]
        result = lab4.first_element(input)
        expected = [4, 6, 7, 8]
        self.assertEqual(expected, result)

    # Part 2
    def test_x_coordinates(self):
        point1 = data.Point(1, 3)
        point2 = data.Point(4, 3)
        input = [point1, point2]
        result = lab4.x_coordinates(input)
        expected = [1, 4]
        self.assertEqual(expected, result)

    def test_x_coordinates_2(self):
        point1 = data.Point(4, 5)
        point2 = data.Point(77, 4)
        point3 = data.Point(3, 5)
        input = [point1, point2, point3]
        result = lab4.x_coordinates(input)
        expected = [4, 77, 3]
        self.assertEqual(expected, result)

    # Part 3
    def test_are_in_positive_quadrant(self):
        point1 = data.Point(4, 5)
        point2 = data.Point(77, 4)
        point3 = data.Point(3, 5)
        input = [point1, point2, point3]
        result = lab4.are_in_positive_quadrant(input)
        expected = [[4, 5], [77, 4], [3, 5]]
        self.assertEqual(expected, result)

    def test_are_in_positive_quadrant_2(self):
        point1 = data.Point(-4, -6)
        point2 = data.Point(3, 7)
        point3 = data.Point(-1, 4)
        point4 = data.Point(4, -66)
        point5 = data.Point(3, 5)
        expected = [[3, 7], [3, 5]]
        result = lab4.are_in_positive_quadrant([point1, point2, point3, point4, point5])
        self.assertEqual(expected, result)

    # Part 4
    def test_distance(self):
        point1 = data.Point(3, 4)
        point2 = data.Point(3, 4)
        expected = 0
        result = lab4.distance(point1, point2)
        self.assertEqual(expected, result)

    def test_distance2(self):
        point1 = data.Point(7, 8)
        point2 = data.Point(3, 4)
        expected = 5.6568542494
        result = lab4.distance(point1, point2)
        self.assertAlmostEqual(expected, result)


    # Part 5
    def test_manhattan_distance(self):
        point1 = data.Point(4, 3)
        point2 = data.Point(5, 6)
        expected = 4
        result = lab4.manhattan_distance([point1, point2])
        self.assertEqual(expected, result)

    def test_manhattan_distance2(self):
        point1 = data.Point(-5, 7)
        point2 = data.Point(4, -8)
        expected = 24
        result = lab4.manhattan_distance([point1, point2])
        self.assertEqual(expected, result)

    # Part 6
    def test_distance_all(self):
        point1 = data.Point(3, 2)
        point2 = data.Point(7, 6)
        point3 = data.Point(5, 4)
        expected = [3.605551275463989, 9.219544457292887, 6.4031242374328485]
        result = lab4.distance_all([point1, point2, point3])
        self.assertAlmostEqual(expected, result)

    def test_distance_all2(self):
        point1 = data.Point(0, 0)
        point2 = data.Point(1, 1)
        point3 = data.Point(6, 8)
        point4 = data.Point(8, 10)
        expected = [0.0, 1.4142135623730951, 10.0, 12.806248474865697]
        result = lab4.distance_all([point1, point2, point3, point4])
        self.assertAlmostEqual(expected, result)



if __name__ == '__main__':
    unittest.main()

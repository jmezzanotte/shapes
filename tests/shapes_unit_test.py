import unittest
from shapes.shapes import Triangle


class EquilateralTriangleTestCase(unittest.TestCase):

    """
    Tests for Triangle class in shapes.pt
    """

    def setUp(self):
        """
        Instantiates a Triangle object to be used for testing.
        :return: 
        """
        print "Running setup"

        self.test_triange = Triangle(hypotenuse=3, opposite=3, adjacent=3)

    def test_is_scalene(self):
        """
        Tests whether or not the test object correctly identifies a scalene triangle.
        :return: Returns True if test passes
        """

        self.assertFalse(self.test_triange.is_scalene())

    def test_is_equilateral(self):
        """
        Tests whether or not the test object correctly identifies an equilateral triangle.
        :return: Returns True if test passes, False otherwise
        """
        self.assertTrue(self.test_triange.is_equilateral())

    def test_is_isosceles(self):
        """
        Tests whether or not the test object correctly identifies an isosceles triangle.
        :return: 
        """
        self.assertFalse(self.test_triange.is_isosceles())

    def test_perimeter(self):
        """
        Tests whether or not our perimeter property is functioning correctly.
        :return: 
        """
        self.assertEqual(self.test_triange.perimeter, 9)

if __name__ == "__main__":
    unittest.main()


class Triangle(object):

    SINE = "Opposite / Hypotenuse"
    COSINE = "Adjacent / Hypotenuse"
    TANGENT = "Opposite / Adjacent"

    def __init__(self, *args, **kwargs):
        self.args = list(args)
        self.hypotenuse = args.pop() if len(self.args) > 0 else kwargs.get('hypotenuse', None)
        self.adjacent = args.pop() if len(self.args) > 0 else kwargs.get('adjacent', None)
        self.opposite = args.pop() if len(self.args) > 0 else kwargs.get('opposite', None)
        self.triangle = [self.hypotenuse, self.adjacent, self.opposite]

    @property
    def hypotenuse(self):
        return self._hypotenuse

    @hypotenuse.setter
    def hypotenuse(self, value):
        try:
            int(value)
        except ValueError:
            raise ValueError("Value must be an integer.")
        if value < 0:
            raise ValueError("Hypotenuse cannot be less than 0.")
        self._hypotenuse = value

    @property
    def adjacent(self):
        return self._adjacent

    @adjacent.setter
    def adjacent(self, value):
        try:
            int(value)
        except ValueError:
            raise ValueError("Value must be an integer.")
        if value < 0:
            raise ValueError("Adjacent side cannot be less than 0")
        self._adjacent = value

    @property
    def opposite(self):
        return self._opposite

    @opposite.setter
    def opposite(self, value):
        try:
            int(value)
        except ValueError:
            raise ValueError("Value must be an integer.")
        if value < 0:
            raise ValueError("Opposite side cannot be less than 0.")
        self._opposite = value

    def is_scalene(self):

        """
        Determines if this triangle object is scalene
        :return: Returns True if this triangle is scalene, False otherwise
        """

        return len(list(set(self.triangle))) == 3

    def is_equilateral(self):

        """
        Determines if this triangle object is equilateral.
        :return: Returns True if this triangle is equilateral, False otherwise
        """

        return len(list(set(self.triangle))) == 1

    def is_isosceles(self):

        """
        Determines if this triangle object is isosceles. 
        :return: Returns True if this triange is isosceles, False otherwise.
        """

        return len(list(set(self.triangle))) == 2

    def is_right(self):
        """
        Determines if this triangle object is a right triangle
        :return: Returns True if this triangle is a right triangle, False otherwise
        """
        return self.adjacent**2 + self.opposite**2 == self.hypotenuse**2

    @property
    def sine(self):
        return self.opposite / self.hypotenuse

    @property
    def cosine(self):
        return self.adjacent / self.hypotenuse

    @property
    def tangent(self):
        return self.opposite / self.adjacent

    @property
    def perimeter(self):
        return self.hypotenuse + self.adjacent + self.opposite

    @property
    def area(self):
        return (self.base * self.opposite) * 0.5

    @property
    def base(self):
        return self.adjacent


if __name__ == "__main__":

    # Quick unit tests of the module.
    t = Triangle(hypotenuse=55, adjacent=24, opposite=32)
    print t.is_equilateral()
    print t.is_isosceles()
    print t.is_scalene()
    print t.hypotenuse
    print t.sine
    print t.area
    print "This triangle is has a right angle:{0}".format(t.is_right())
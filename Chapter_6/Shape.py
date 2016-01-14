#!/usr/bin/env python3
# Copyright (c) 2008-11 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""
This module provides the Point and Circle classes.

>>> point = Point()
>>> point
Point(0, 0)
>>> point.x = 12
>>> str(point)
'(12, 0)'
>>> a = Point(3, 4)
>>> b = Point(3, 4)
>>> a == b
True
>>> a == point
False
>>> a != point
True

>>> circle = Circle(2)
>>> circle
Circle(2, 0, 0)
>>> circle.radius = 3
>>> circle.x = 12
>>> circle
Circle(3, 12, 0)
>>> a = Circle(4, 5, 6)
>>> b = Circle(4, 5, 6)
>>> a == b
True
>>> a == circle
False
>>> a != circle
True
"""

import math


class Point:

    def __init__(self, x=0, y=0):
        """A 2D cartesian coordinate

        >>> point = Point()
        >>> point
        Point(0, 0)
        """
        self.x = x
        self.y = y


    def distance_from_origin(self):
        """Returns the distance of the point from the origin

        >>> point = Point(3, 4)
        >>> point.distance_from_origin()
        5.0
        """
        return math.hypot(self.x, self.y)


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __repr__(self):
        return "Point({0.x!r}, {0.y!r})".format(self)


    def __str__(self):
        return "Point({0.x!r}, {0.y!r})".format(self)
    
    # +， += support 
    def __add__(self, point):
        """Returns a new Point whose coordinate are the sum of this
        one's and the other one's

        >>> p = Point(2, 4)
        >>> q = p + Point(3, 5)
        >>> q
        Point(5, 9)
        """
        return Point(self.x + point.x, self.y + point.y)
    
    # -, -= support
    def __sub__(self, point):
        """Return the result of one point minus the other
    
        >>> a = Point(3, 4)
        >>> b = Point(2, 5)
        >>> a - b
        Point(1, -1)
        >>> a -= b
        >>> a
        Point(1, -1)
        """
        return Point(self.x - point.x, self.y - point.y)

    # *, *= support
    def __mul__(self, other):
        """Returns a new Point whose coordinate is this one's multiplied
        by the other number

        >>> p = Point(2, 4)
        >>> q = p * 3
        >>> q
        Point(6, 12)
        """
        return Point(self.x * other, self.y * other)
    
    # /, /= support
    def __truediv__(self, other):
        """Returns a new Point whose coordinate is this one's divided
        by the other number

        >>> p = Point(2, 4)
        >>> q = p / 2
        >>> q
        Point(1.0, 2.0)
        >>> q = p / 0
        assert
        """
        assert other != 0
        return Point(self.x / other, self.y / other)

    # //, //= support
    def __floordiv__(self, other):
        """Returns this Point with its coordinate set to this one's
        floor divided by the other number

        >>> p = Point(2, 4)
        >>> p // 2
        Point(1, 2)
        >>> p // 0
        assert
        """
        assert not other == 0
        return Point(self.x // other, self.y // other)
 
class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        """A Circle

        >>> circle = Circle(2)
        >>> circle
        Circle(2, 0, 0)
        """
        super().__init__(x, y)
        self.radius = radius


    def edge_distance_from_origin(self):
        """The distance of the circle's edge from the origin

        >>> circle = Circle(2, 3, 4)
        >>> circle.edge_distance_from_origin()
        3.0
        """
        return abs(self.distance_from_origin() - self.radius)


    def area(self):
        """The circle's area

        >>> circle = Circle(3)
        >>> a = circle.area()
        >>> int(a)
        28
        """
        return math.pi * (self.radius ** 2)


    def circumference(self):
        """The circle's circumference

        >>> circle = Circle(3)
        >>> d = circle.circumference()
        >>> int(d)
        18
        """
        return 2 * math.pi * self.radius


    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)


    def __repr__(self):
        return "Circle({0.radius!r}, {0.x!r}, {0.y!r})".format(self)


    def __str__(self):
        return repr(self)
        

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

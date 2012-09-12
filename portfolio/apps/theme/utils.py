from collections import namedtuple
import math
import sys

"""
A simple Point.
e.g. 
p = Point(4, 5)
p.x -> 4
"""
Point = namedtuple('Point', 'x y')

def get_point_on_circle(origin, radius, radian):
    """
    origin: origin of circle. e.g. (0, 0)
    radius: radius in radians e.g. math.pi
    radian: radian at which the point will be returned
    
    Returns the Point of the radian along the radius from the origin.
    This adjust for monitor coordinate system.
    """
    x = origin + radius * math.cos(radian)
    y = origin + radius * math.sin(radian)
    return Point(x, y) 

def get_slope(p1, p2):
    """
    Return the slope of the two points.
    Uses sys.maxint for vertical infinite slope.
    """    
    run = p2.x - p1.x    
    return (p2.y - p1.y) / run if run != 0 else sys.maxint

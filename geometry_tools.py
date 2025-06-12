from manim import *
import sympy as sy
from changing_point_representation import MakeManimView, MakeSympyView


def CircleTangentToCircleAndPointOnLine(circle_point, line_point, line):
    """
    Finds a circle tangent to another circle and passing through a point on a line.

    :param circle_point: Center point of the original circle (Manim Dot)
    :param line_point: Point on the target line (Manim Dot)
    :param line: SymPy Line object representing the tangent line
    :return: Tuple of (center, radius) in Manim Point coordinates
    :raises ValueError: If circle_point and line_point coincide
    """
    circle_point = MakeSympyView(circle_point)
    line_point = MakeSympyView(line_point)

    if circle_point == line_point:
        return circle_point

    line_cl = sy.Segment(circle_point, line_point)
    perp_to_line = line.perpendicular_line(line_point)
    seg_bis = line_cl.perpendicular_bisector()

    center = seg_bis.intersection(perp_to_line)[0]
    radius = center.y - line_point.y

    return MakeManimView(center), radius


def CorrectTangentFromPoint(center, radius, point):
    """
    Calculates the correct tangent point from an external point to a circle.

    :param center: Center of the circle (Manim Point)
    :param radius: Radius of the circle (float)
    :param point: External point (Manim Dot)
    :return: Correct tangent point in  Manim Point coordinates
    :raises: ValueError if no tangents exist (point inside circle)

    Note: Automatically selects the appropriate tangent based on point's x-position:
          - For points with x < 0, returns the leftmost tangent
          - For points with x >= 0, returns the rightmost tangent
    """
    center = MakeSympyView(Dot(center))
    point = MakeSympyView(point)

    circle = sy.Circle(center, radius)
    tangents = circle.tangent_lines(point)

    tang_point_0 = tangents[0].intersection(tangents[0].perpendicular_line(center))[0]
    tang_point_1 = tangents[1].intersection(tangents[1].perpendicular_line(center))[0]

    if point.x < 0:
        if tang_point_0.x > tang_point_1.x:
            tang_point_0 = tang_point_1
    else:
        if tang_point_0.x < tang_point_1.x:
            tang_point_0 = tang_point_1

    return MakeManimView(tang_point_0)


def TwoPointsTangsIntersection(tangent_point_1, tangent_point_2, omega_1, omega_2):
    """
    Calculates the intersection point of tangent lines from two points to two circles.

    :param tangent_point_1: First tangent point (Manim Dot)
    :param tangent_point_2: Second tangent point (Manim Dot)
    :param omega_1: First circle (Manim Circle)
    :param omega_2: Second circle (Manim Circle)
    :return: Intersection point in Manim Point coordinates (np.array[x,y,0])
    """
    tangent_point_1 = MakeSympyView(tangent_point_1)
    tangent_point_2 = MakeSympyView(tangent_point_2)
    center_1 = MakeSympyView(omega_1)
    center_2 = MakeSympyView(omega_2)

    line1 = sy.Line(tangent_point_1, center_1)
    line2 = sy.Line(tangent_point_2, center_2)

    tangent1 = line1.perpendicular_line(tangent_point_1)
    tangent2 = line2.perpendicular_line(tangent_point_2)

    return MakeManimView(tangent1.intersection(tangent2)[0])

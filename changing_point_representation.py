import sympy as sy


def MakeManimView(point):
    """
    Converts a SymPy Point to Manim Point

    :param point: SymPy Point or Point2D object to convert
    :return: Manim Point
    """
    x = sy.Point2D(point).coordinates
    return float(x[0]), float(x[1]), float(0)


def MakeSympyView(point):
    """
        Converts a Manim Dot to Sumpy Point

        :param point: Manim Dot to convert
        :return: Sympy Point
        """
    point = point.get_center()
    return sy.Point(point[0], point[1])

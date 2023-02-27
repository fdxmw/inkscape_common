class Point:
    '''(x, y) pair.'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

def midpoint(p0: Point, p1: Point) -> Point:
    '''Returns the midpoint between two points.'''
    x_diff = p1.x - p0.x
    y_diff = p1.y - p0.y
    return Point(p0.x + x_diff / 2, p0.y + y_diff / 2)

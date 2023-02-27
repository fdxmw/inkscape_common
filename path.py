import inkex
from lxml import etree

from enum import IntEnum
from common.point import Point

def path(parent, stroke_width, stroke_color, fill_color, commands):
    '''Create a SVG path.

    The other functions in this file help with generating the 'commands'
    argument.

    See https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths

    '''
    style = {
        'stroke-width' : stroke_width,
        'stroke': stroke_color,
        'fill': fill_color,
        'fill-rule': 'evenodd',
    }
    attributes = {
        'style': str(inkex.Style(style)),
        'd': commands,
    }
    etree.SubElement(parent, inkex.addNS('path', 'svg'), attributes)

def move_abs(p: Point):
    '''Move to absolute position (p.x, p.y).'''
    return 'M %.4f %.4f ' % (p.x, p.y)

def move_rel(dx, dy):
    '''Move relative to current position (+dx,+dy).'''
    return 'm %.4f %.4f ' % (dx, dy)

def hline_abs(x):
    '''Draw a horizontal line from current position to absolute x-position.'''
    return 'H %.4f ' % x

def hline_rel(width):
    '''Draw a horizontal line with length 'width' from current position.'''
    return 'h %.4f ' % width

def vline_abs(y):
    '''Draw a vertical line from current position to absolute y-position.'''
    return 'V %.4f ' % y

def vline_rel(height):
    '''Draw a vertical line with length 'height' from current position.'''
    return 'v %.4f ' % height

def line_abs(p: Point):
    '''Draw a line from current position to absolute (p.x,p.y) position.'''
    return 'L %.4f %.4f ' % (p.x, p.y)

class Size(IntEnum):
    SMALL = 0
    LARGE = 1
class Winding(IntEnum):
    CCW = 0  # Counterclockwise
    CW = 1   # Clockwise
def arc_abs(radius_x, radius_y, small_large, winding, p: Point):
    '''# Draw an arc from current position to absolute (p.x, p.y) position.

    See https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths#arcs

    '''
    # The '0' hard-coded in the middle of this string indicates no rotation.
    return ('A %.4f %.4f 0 %d %d %.4f %.4f ' %
            (radius_x, radius_y, int(small_large), int(winding), p.x, p.y))

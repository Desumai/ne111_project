   
def tupleAdd(t1, t2) -> tuple:
    """
    (tuple, tuple) -> tuple

    adds the corresponding values in each tuple together. Tuples must be of the same length


    tupleAdd(t1 = (1, 2, 3), t2 = (3, 2, 3))
        >>> (4, 4, 6)
    """

    if(len(t1) != len(t2)):
        raise Exception()
        
    list = []
    for i in range(0, len(t1)):
        list.append(t1[i] + t2[i])
    return tuple(i for i in list)

def tupleFloatToInt(t) -> tuple:
    """
    (tuple(float, float, ...)) -> tuple(int, int, ...)

    converts a tuple of floats to a tuple of integers. Floats are rounded to the nearest integer
    """

    list = []
    for i in t:
        list.append(round(i))

    return list

def calculateDistanceFromMouse(point):
    from States import State as STATES
    import math
    """
    (tuple(float, float)) -> float

    calculates the distance from the current/last mouse position to [point]. Returns the distance as a float
    """
    x = point[0] - STATES.MOUSE_POS[0]
    y = point[1] - STATES.MOUSE_POS[1]

    return math.sqrt((x**2)+(y**2))

def createThrowableObjectFromMsg(msg):
    from Constants import Constants
    from ThrowableItems.BasicItem import BasicItem
    from ThrowableItems.BounceItem import BounceItem
    from ThrowableItems.GravityItem import GravityItem
    from ThrowableItems.AvoidItem import AvoidItem

    vals = msg[2:].split(seperator=" ")
    
    type = int(vals[0])
    size = tuple(int, vals[1].split(','))
    xVal = float(vals[2])
    vel = tuple(float, vals[3].split(','))

    if(type == 0):
        return BasicItem(postition=(xVal, Constants.THROW_OVER_HEIGHT), velocity=vel, size=size, sprite=None)
    elif(type == 1):
        return GravityItem(postition=(xVal, Constants.THROW_OVER_HEIGHT), velocity=vel, size=size, sprite=None)
    elif(type == 2):
        return BounceItem(postition=(xVal, Constants.THROW_OVER_HEIGHT), velocity=vel, size=size, sprite=None)
    elif(type == 3):
        return AvoidItem(postition=(xVal, Constants.THROW_OVER_HEIGHT), velocity=vel, size=size, sprite=None)
    else:
        raise Exception

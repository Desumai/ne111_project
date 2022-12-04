import math
from States import State as STATES

class ExtraFunctions():
    
    @staticmethod
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

    @staticmethod
    def tupleFloatToInt(t) -> tuple:
        """
        (tuple(float, float, ...)) -> tuple(int, int, ...)

        converts a tuple of floats to a tuple of integers. Floats are rounded to the nearest integer
        """

        list = []
        for i in t:
            list.append(round(i))

        return list

    @staticmethod
    def calculateDistanceFromMouse(point):
        """
        (tuple(float, float)) -> float

        calculates the distance from the current/last mouse position to [point]. Returns the distance as a float
        """
        x = point[0] - STATES.MOUSE_POS[0]
        y = point[1] - STATES.MOUSE_POS[1]

        return math.sqrt((x**2)+(y**2))

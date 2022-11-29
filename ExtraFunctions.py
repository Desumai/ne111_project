import math

class ExtraFunctions():
    
    @classmethod
    def tupleAdd(self, t1, t2) -> tuple:
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

    @classmethod
    def tupleFloatToInt(self, t) -> tuple:
        """
        (tuple(float, float, ...)) -> tuple(int, int, ...)

        converts a tuple of floats to a tuple of integers. Floats are rounded to the nearest integer
        """

        list = []
        for i in t:
            list.append(round(i))

        return list

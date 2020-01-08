# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        can = [i for i in range(n)]

        for i in range(n):
            if (i in can):
                for j in range(n):
                    if (i == j):
                        continue
                    if (knows(i, j) == 1):
                        can.remove(i)
                        break
                    else:
                        if (j in can):
                            can.remove(j)

        if (len(can) != 0):
            for i in range(n):
                if (i != can[0]):
                    if (knows(i, can[0]) != 1):
                        return -1

            return can[0]
        return -1





class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1;
        while (i*i <= x):
            i *= 2
        i /= 2
        while (i*i <= x):
            i += 1
        return int(i - 1)
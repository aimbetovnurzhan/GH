class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if 9 == digits[-1]:
            s = 0
            for i, dig in enumerate(digits[::-1]):
                s += dig*10**i
            return [int(d) for d in str(s + 1)]
        else:
            return digits[:len(digits[:-1])] + [digits[-1] + 1]
            # return digits[-1] + 1
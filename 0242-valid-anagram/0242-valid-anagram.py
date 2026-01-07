class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            """dict = {}
            for char in s:
                if char not in dict:
                    dict[char] = 1
                else:
                    dict[char] += 1"""
            dict = Counter(s)
            for key, value in dict.items():
                if t.count(key) != value:
                    return False
        else:
            return False
        return True

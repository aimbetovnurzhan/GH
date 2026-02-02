class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        if len(strs) == 1:
            res = strs[0]
        else:
            for i, char in enumerate(list(strs[0])):
                x = False
                for j in range(1, len(strs)):
                    if len(strs[j]) >= i+1 and strs[j][i] == char:
                        x = True
                    else:
                        x = False
                        break
                if x:
                    res += char
                else:
                    break
        return res

class Solution:
    def isValid(self, s: str) -> bool:
        br = {"(":1,")":-1,"[":2,"]":-2,"{":3,"}":-3}
        inp = list(s)
        stack = []
        res = True
        for chr in inp:
            if br.get(chr) > 0:
                stack.append(chr)
            elif stack:
                dl = stack.pop()
                if br.get(dl) + br.get(chr) != 0:
                    res = False
            elif len(stack) == 0:
                stack.append(chr)
        if stack:
            res = False
        return res

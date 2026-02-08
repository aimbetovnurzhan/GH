class Solution(object):
    def addBinary(self, a, b):
        mx, mn = list(a[::-1]), list(b[::-1])
        if len(b) >= len(a):
            mx, mn = mn, mx
        for k in range(len(mx)):
            if k < len(mn):
                if k+1 < len(mx):
                    mx[k + 1] = (int(mx[k + 1]) + (int(mx[k]) + int(mn[k])) // 2)
                else:
                    if (int(mx[k]) + int(mn[k])) // 2 > 0:
                        mx.append((int(mx[k]) + int(mn[k])) // 2)
                mx[k] = (int(mx[k]) + int(mn[k])) % 2
            else:
                if int(mx[k]) // 2 > 0:
                    if k+1 < len(mx):
                        mx[k + 1] = int(mx[k + 1]) + int(mx[k]) // 2
                    else:
                        mx.append(int(mx[k]) // 2)
                mx[k] = int(mx[k]) % 2
        if len(mx) == k + 2 and int(mx[k+1]) // 2 > 0:
            mx.append(int(mx[k + 1]) // 2)
            mx[k + 1] = int(mx[k + 1]) % 2
        return "".join(map(str,mx[::-1]))
class Solution:
    def romanToInt(self, s: str) -> int:
        arr = list(s)
        x = 0
        for i, char in enumerate(arr):
            if char == 'I':
                if i+1 < len(arr) and (arr[i+1] == 'V' or arr[i+1] == 'X'):
                    continue
                else:
                    x += 1
            elif char == 'V':
                if i-1 >= 0 and arr[i-1] == 'I':
                    x += 4
                else:
                    x += 5
            elif char == 'X':
                if i+1 < len(arr) and (arr[i+1] == 'L' or arr[i+1] == 'C'):
                    continue
                elif i-1 >= 0 and arr[i-1] == 'I':
                    x += 9
                else:
                    x += 10
            elif char == 'L':
                if i-1 >= 0 and arr[i-1] == 'X':
                    x += 40
                else:
                    x += 50
            elif char == 'C':
                if i+1 < len(arr) and (arr[i+1] == 'D' or arr[i+1] == 'M'):
                    continue
                elif i-1 >= 0 and arr[i-1] == 'X':
                    x += 90
                else:
                    x += 100
            elif char == 'D':
                if i-1 >= 0 and arr[i-1] == 'C':
                    x += 400
                else:
                    x += 500
            elif char == 'M':
                if i-1 >= 0 and arr[i-1] == 'C':
                    x += 900
                else:
                    x += 1000
        return x
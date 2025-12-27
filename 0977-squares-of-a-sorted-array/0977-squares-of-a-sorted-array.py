class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_abs_nums = sorted(list(map(abs, nums)))
        squared = list(map(lambda x: x**2, sorted_abs_nums))
        return squared
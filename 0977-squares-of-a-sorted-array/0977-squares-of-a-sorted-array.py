class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        abs_nums = list(map(abs, nums))
        abs_nums.sort()
        squared = list(map(lambda x: x**2, abs_nums))
        return squared
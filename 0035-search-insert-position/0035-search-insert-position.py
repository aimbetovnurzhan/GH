class Solution(object):
    def searchInsert(self, nums, target):
        j = 0
        if target in nums:
            return nums.index(target)
        else:
            for i, num in enumerate(nums):
                if num > target:
                    return i
            return i + 1
        
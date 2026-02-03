class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while True:
            if i + 1 < len(nums):
                if nums[i] == nums[i + 1]:
                    nums.remove(nums[i])
                else:
                    i += 1
            else:
                break
        return len(nums)
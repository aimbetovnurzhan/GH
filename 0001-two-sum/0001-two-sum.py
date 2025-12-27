class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
            # for j in range(i+1,len(nums)):
                # if nums[i] + nums[j] == target:
                    # return [i, j]
        i=0
        while i < len(nums):
            try:
                j = nums.index(target - nums[i])
                if j != i:
                    return [i,j]
            except ValueError:
                pass
            i +=1

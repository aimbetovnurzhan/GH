class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1:
            if nums[0] == val:
                return 0
        else:
            i = 0
            j = 1
            while True:
                if i + 1 < len(nums):
                    if j < len(nums):
                        if nums[i] == val:
                            if nums[j] != "_":
                                if nums[j] != val:
                                    nums[i], nums[j] = nums[j], "_"
                                    i += 1
                                    j += 1
                                else:
                                    nums[j] = "_"
                                    if j + 1 < len(nums):
                                        j += 1
                                    else:
                                        nums[i] = "_"
                            else:
                                j += 1
                        elif nums[i] == "_":
                            if nums[j] != "_":
                                if nums[j] != val:
                                    nums[i], nums[j] = nums[j], "_"
                                    i += 1
                                    j += 1
                                else:
                                    nums[j] = "_"
                                    j += 1
                            else:
                                j += 1
                        else:
                            if nums[j] == val:
                                nums[j] = "_"
                            i += 1
                            j += 1
                    else:
                        break
                else:
                    break
        return len([x for x in nums if x is not "_"])
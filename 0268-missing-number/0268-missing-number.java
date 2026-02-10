class Solution {
    public int missingNumber(int[] nums) {
        // Set<Integer> numSet = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        Arrays.sort(nums);
        if (nums[0] != 0) {
            return 0;
        } else {
            for (int i = 1; i < nums.length; i++) {
                if (nums[i] != nums[i - 1] + 1) {
                    return nums[i] - 1;
                }
            }
        }
        return nums[nums.length - 1] + 1;
    }
}
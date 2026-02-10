class Solution {
    public void moveZeroes(int[] nums) {
        if (nums.length > 1) {
            int temp;
            outerLoop:
            for (int i = 0; i < nums.length - 1; i++) {
                for (int j = i + 1; j < nums.length; j++) {
                    if (nums[i] == 0 && nums[j] != 0) {
                        temp = nums[i];
                        nums[i] = nums[j];
                        nums[j] = temp;
                        continue outerLoop;
                    }
                }
            }
        }
    }
}
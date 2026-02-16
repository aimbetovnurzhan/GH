class Solution {
    public int removeDuplicates(int[] nums) {
        int k = 0;
        int i = 1;
        while (k < nums.length && i < nums.length && nums[k] != 101) {
            if (nums[i] == nums[k]) {
                nums[i] = 101;
            } else if (nums[i] != 101 && nums[i] != nums[k]) {
                if (i != k + 1) {
                    nums[k + 1] = nums[i];
                    nums[i] = 101;
                }
                k ++;
            }
            i ++;
        }
        return k + 1;
    }
}
class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0;
        int i = 1;
        while (k < nums.length) {
            if (nums[k] != val && nums[k] >= 0) {
                k ++;
                i = k + 1;
            } else if (i < nums.length) {
                nums[k] = nums[i];
                nums[i] = -1;
                i ++;
            } else if (i == nums.length) {
                nums[k] = -1;
                break;
            }
        }
        return k;
    }
}
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 1) {
            return 1;
        } else {
            int k = 0;
            while (k < nums.length && nums[k] != -101) {
                for (int j = k + 1; j < nums.length; j++) {
                    if (nums[j] == nums[k]) {
                        nums[j] = -101;
                    } else if (nums[j] != -101 && nums[j] != nums[k]) {
                        if (j == k + 1) {
                            break;
                        } else {
                            nums[k + 1] = nums[j];
                            nums[j] = -101;
                            break;
                        }
                    } 
                }
                k++;
            }
            return k;
        }
    }
}
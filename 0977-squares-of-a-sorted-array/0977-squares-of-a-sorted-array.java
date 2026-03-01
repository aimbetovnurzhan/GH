class Solution {
    public int[] sortedSquares(int[] nums) {
        int i = 0, j = nums.length - 1;
        if (j == 0) {
            nums[i] = nums[i] * nums[i];
            return nums;
        }
        int[] a = nums.clone();
        while (i <= j) {
            if (Math.abs(a[i]) > Math.abs(a[j])) {
                nums[j - i] = a[i] * a[i];
                i ++;
            } else {
                nums[j - i] = a[j] * a[j];
                j --;
            }
        }
        return nums;
    }
}
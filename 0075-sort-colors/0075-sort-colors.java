class Solution {
    public void sortColors(int[] nums) {
        int n = nums.length;
        if (n == 1) return;
        int[] a = nums.clone();
        Arrays.fill(nums, 1);
        int j = 0, k = n - 1;
        for (int i = 0; i < n; i++) {
            if (a[i] == 0) {
                nums[j] = 0;
                j++;
            } else if (a[i] == 2) {
                nums[k] = 2;
                k --;
            }
        }
        return;
    }
}
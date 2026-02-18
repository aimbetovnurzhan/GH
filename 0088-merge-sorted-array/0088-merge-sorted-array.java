class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m, j = n;
        while (i + j > 0) {
            if (j > 0) {
                if (i > 0) {
                    if (nums1[i - 1] >= nums2[j - 1]) {
                        nums1[i + j - 1] = nums1[i - 1];
                        if (i == 1 && j == 1 && m == 1) {
                            nums1[i - 1] = nums2[j - 1];
                            return;
                        }
                        i--;
                    } else {
                        nums1[i + j - 1] = nums2[j - 1];
                        j --;
                    }
                } else {
                    nums1[j - 1] = nums2[j - 1];
                    j --;
                }
            } else {
                return;
            }
        }
        return;
    }
}
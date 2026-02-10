class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet < Integer> dct = new HashSet<>();
        for (int n: nums) {
            if (dct.contains(n)) {
                return true;
            } else {
                dct.add(n);
            }
            // int index = Arrays.binarySearch(Arrays.copyOfRange(nums, i + 1, nums.length), nums[i]);
            // System.out.println(Arrays.toString(Arrays.copyOfRange(nums, i + 1, nums.length)));
            // System.out.println(index);
            // System.out.println(nums[i]);
            // if (index >= 0) {
            //     flag = true;
            // }
        }
        return false;
    }
}
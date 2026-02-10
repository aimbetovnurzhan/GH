class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map < Integer, Integer> dct = new HashMap<>();
        boolean flag = false;
        for (int n: nums) {
            if (dct.getOrDefault(n, 0) > 0) {
                flag = true;
            } else {
                dct.put(n, 1);
            }
            // int index = Arrays.binarySearch(Arrays.copyOfRange(nums, i + 1, nums.length), nums[i]);
            // System.out.println(Arrays.toString(Arrays.copyOfRange(nums, i + 1, nums.length)));
            // System.out.println(index);
            // System.out.println(nums[i]);
            // if (index >= 0) {
            //     flag = true;
            // }
        }
        return flag;
    }
}
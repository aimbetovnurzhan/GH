class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        HashMap <Integer, Integer> cntr = new HashMap<>();
        for (int i = 0; i < nums.length; i ++) {
            cntr.putIfAbsent(i + 1, 0);
            cntr.merge(nums[i], 1, Integer::sum);
        }
        // List<Integer> missed = new ArrayList<>();
        return cntr.entrySet().stream().filter(e -> e.getValue() == 0).map(e -> e.getKey()).collect(Collectors.toList());
    }
}
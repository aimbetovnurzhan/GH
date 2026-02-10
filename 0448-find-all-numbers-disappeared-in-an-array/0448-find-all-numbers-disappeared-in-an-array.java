class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        boolean[] chkr = new boolean[nums.length + 1];
        // HashMap <Integer, Integer> cntr = new HashMap<>();
        // for (int i = 0; i < nums.length; i ++) {
        //     cntr.putIfAbsent(i + 1, 0);
        //     cntr.merge(nums[i], 1, Integer::sum);
        // }
        for (int n:nums) {
            chkr[n] = true;
        }
        List<Integer> missed = new ArrayList<>();
        for (int i = 1; i < chkr.length; i++){
            if (!chkr[i]) {
                missed.add(i);
            }
        }
        return missed;
        // return cntr.entrySet().stream().filter(e -> e.getValue() == 0).map(e -> e.getKey()).collect(Collectors.toList());
    }
}
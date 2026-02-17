class Solution {
    public int climbStairs(int n) {
        int cur = 1, prev = 0, sum = 0;
        for (int i = 1; i <= n; i++) {
            sum = cur + prev;
            prev = cur;
            cur = sum;
        }
        return sum;
    }
}
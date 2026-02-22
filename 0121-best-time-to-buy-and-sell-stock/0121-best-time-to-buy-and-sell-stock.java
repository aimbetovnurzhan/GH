class Solution {
    public int maxProfit(int[] prices) {
        int dif = 0;
        for (int i = 1; i < prices.length; i++) {
            dif = Math.max(0,Math.max(dif,prices[i] - prices[i - 1]));
            if (prices[i - 1] < prices[i]) {
                prices[i] = prices[i - 1];
            }
        }
        return dif;
    }
}
class Solution {
    public int hammingWeight(int n) {
        // String bynStr = Integer.toBinaryString(n);
        // System.out.println(bynStr);
        // for (int i = 0; i < bynStr.length(); i++) {}
        int rslt = 0;
        while (n > 0) {
            rslt += n % 2;
            n = n / 2;
        }
        return rslt;
    }
}
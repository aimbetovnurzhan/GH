class Solution {
    public int reverseBits(int n) {
        if (n == 0) return 0;
        String res = "";
        for (int i = 0; i < 32; i ++) {//while (n > 0) {
            res += String.valueOf(n % 2);
            n /= 2;
        }
        System.out.println(res);
        n = Integer.parseInt(res, 2);
        return n;
    }
}
class Solution {
    public int mySqrt(int x) {
        if (x > 1) {
        long bgn = 0; 
        long end = x;
        // for (int i = 0; i < (String.valueOf(x).length() + 1) / 2; i++) {
        //     if (i < (String.valueOf(x).length() - 1) / 2) {
        //         end /= 10;
        //     }
        //     bgn /= 10;
        // }
        long mdl = (bgn+end) / 2;
        System.out.println("bgn " + bgn + ", mdl " + mdl + ", end " + end);

        while (mdl*mdl > x || (mdl + 1) * (mdl + 1) <= x) {
            if (mdl*mdl > x) {
                end = mdl;
            } else {
                bgn = mdl;
            }
            mdl = (bgn+end) / 2;
        }
        return (int) mdl;
        } else {
            return x;
        }
    }
}
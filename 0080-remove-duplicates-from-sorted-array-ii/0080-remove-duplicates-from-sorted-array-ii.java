class Solution {
    public int removeDuplicates(int[] a) {
        int n = a.length;
        if (n < 3) return n;
        int i = 0;
        for (int j = 1; j < n;) {
            if (a[i] == a[j]) {
                if (j != i + 1) {
                    if (a[i + 1] != a[i]) {
                        a[i + 1] = a[j];
                    }
                    a[j] = 10001;
                }
                j ++;
            } else {
                if (j - i == 1) {
                    i ++;
                } else {
                    if (a[i + 1] != a[i]) {
                        a[i + 1] = a[j];
                        a[j] = 10001;
                        i ++;
                    } else {
                        if (j - i > 2) {
                            if (a[i + 2] == 10001) {
                                a[i + 2] = a[j];
                                a[j] = 10001;
                            }
                        }
                        i += 2;
                    }
                }
                j ++;
            }
        }
        if (i + 1 == n) {
            return i + 1;
        } else if (a[i] == a[i + 1]) {
            return i + 2;
        } else {
            return i + 1;
        }
    }
}
class Solution {
    public boolean backspaceCompare(String s, String t) {
        StringBuilder sb1 = new StringBuilder(s);
        StringBuilder sb2 = new StringBuilder(t);
        int n1 = s.length() - s.replace("#","").length();
        int n2 = t.length() - t.replace("#","").length();
        for (int i = 0; i < n1; i++) {
            int j = sb1.indexOf("#");
            sb1.deleteCharAt(j);
            if (j - 1 >= 0) {
                sb1.deleteCharAt(j-1);
            }
        }
        for (int i = 0; i < n2; i++) {
            int j = sb2.indexOf("#");
            sb2.deleteCharAt(j);
            if (j - 1 >= 0) {
                sb2.deleteCharAt(j-1);
            }
        }
        if (sb1.compareTo(sb2) == 0) {
            return true;
        } else {
            return false;
        }
    }
}
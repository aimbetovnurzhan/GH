class Solution {
    public void reverseString(char[] s) {
        if (s.length == 1) return;
        for (int i = 0; i < s.length / 2; i ++) {
            char tmp;
            tmp = s[i];
            s[i] = s[s.length - 1 - i];
            s[s.length - 1 - i] = tmp;
        }
        return;
    }
}
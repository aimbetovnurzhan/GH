class Solution {
    public String longestCommonPrefix(String[] strs) {
        String s = "";
        if (strs.length == 1) {
            s = strs[0];
        } else if (strs.length > 1) {
            Arrays.sort(strs);
            // System.out.println(Arrays.toString(strs));
            if (!strs[0].isEmpty()) {
                int i = 0;
                while (true) {
                    if (i < strs[0].length() && strs[0].charAt(i) == strs[strs.length - 1].charAt(i)) {
                        s += strs[0].charAt(i);
                        i ++;
                    } else {
                        break;
                    }
                }
            }
        }
        return s;
    }
}
class Solution {
    public int strStr(String haystack, String needle) {
        int pstn = 0; //haystack.indexOf(needle); 
        while (pstn + needle.length() <= haystack.length()) {
            // System.out.println(haystack.substring(pstn, pstn + needle.length()));
            if (haystack.substring(pstn, pstn + needle.length()).equals(needle)) {
                return pstn;
            }
            pstn ++;
        }
        return -1;
    }
}
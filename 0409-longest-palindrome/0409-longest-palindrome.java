class Solution {
    public int longestPalindrome(String s) {
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i),0) + 1);
        }
        int sum = 0;
        int odd = 0;
        for (Integer value : map.values()) {
            odd += value % 2;
            sum += value / 2;
        }
        if (odd > 0) {
            return sum * 2 + 1;
        } else {
            return sum * 2;
        }
    }
}
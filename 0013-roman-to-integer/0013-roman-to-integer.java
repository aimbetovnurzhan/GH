class Solution {
    public int romanToInt(String s) {
    Map<Character, Integer> dgts = Map.of('I',1,'V',5,'X',10,'L',50,'C',100,'D',500,'M',1000);
        int sum = 0;
        for (int i = 0; i < s.length(); i++) {
            // System.out.println("Ищу ключ: '" + s.charAt(i) + "'");
            if (i + 1 < s.length() && dgts.get(s.charAt(i)) < dgts.get(s.charAt(i + 1))) {
                sum -= dgts.get(s.charAt(i));
            } else {
                sum += dgts.get(s.charAt(i));
            }
        }
        return sum;
    }
}
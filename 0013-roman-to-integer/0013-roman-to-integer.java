import java.util.HashMap;
import static java.util.Map.entry;

class Solution {
    public int romanToInt(String s) {
    Map<String, Integer> dgts = Map.ofEntries(
        entry("I", 1),
        entry("V", 5),
        entry("X", 10),
        entry("L", 50),
        entry("C", 100),
        entry("D", 500),
        entry("M", 1000),
        entry("IV", 4),
        entry("IX", 9),
        entry("XL", 40),
        entry("XC", 90),
        entry("CD", 400),
        entry("CM", 900)
    );

        int i = 0;
        int sum = 0;
        String[] ltrs = s.split("");
        while (i < ltrs.length) {
            // System.out.println("Ищу ключ: '" + ltrs[i] + "'");
            if ((i + 1 < ltrs.length) && (dgts.get(ltrs[i] + ltrs[i + 1]) != null)) {
                sum = sum + dgts.get(ltrs[i] + ltrs[i + 1]);
                i += 2;
            } else {
                sum = sum + dgts.get(ltrs[i]);
                i ++;
            }
        }
        return sum;
    }
}
class Solution {
    public int[] plusOne(int[] digits) {
        int add = 1;
        int mod = 0;
        for (int i = digits.length - 1; i >= 0; i --){
            mod = (digits[i] + add) % 10;
            add = ((int) ((digits[i] + add) / 10));
            digits[i] = mod;
        }
        if (add > 0) {
            int[] newDigits = new int[digits.length + 1];
            newDigits[0] = add;
            System.arraycopy(digits, 0, newDigits, 1, digits.length);
            digits = newDigits;
            // digits.append(add);
        }
        return digits;
    }
}
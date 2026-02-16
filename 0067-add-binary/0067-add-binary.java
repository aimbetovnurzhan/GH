class Solution {
    public String addBinary(String a, String b) {
        List<Integer> lng = a.chars().map(Character::getNumericValue).boxed().collect(Collectors.toList());
        List<Integer> srt = b.chars().map(Character::getNumericValue).boxed().collect(Collectors.toList());
        List<Integer> tm;
        int add = 0;
        int tmp = 0;
        int i = 1;
        if (a.length() < b.length()) {
            tm = lng;
            lng = srt;
            srt = tm;
        }
        while (i <= lng.size()) {
            if (i <= srt.size()) {
                tmp = lng.get(lng.size() - i) + srt.get(srt.size() - i);
                lng.set(lng.size() - i, (tmp + add) % 2);
                add = (tmp + add) / 2;
            } else {
                tmp = lng.get(lng.size() - i);
                lng.set(lng.size() - i, (tmp + add) % 2);
                add = (tmp + add) / 2;
            }
            i ++;
        }
        if (add > 0) {
            lng.add(0, add % 2);
            if (add > 1) {
                lng.add(0, add / 2);
            }
        }
        return lng.stream().map(String::valueOf).collect(Collectors.joining(""));
    }
}
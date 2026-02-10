class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> map = Map.of('(',')','{','}','[',']');
        ArrayList<Character> list = new ArrayList<>();
        if (s.length() % 2 == 0) {
            for (char c : s.toCharArray()) {
                // System.out.println(c);
                if (map.containsKey(c)) {
                    list.add(map.get(c));
                    // System.out.println("added" + map.get(c));
                } else if (list.size() > 0 && c == list.get(list.size() - 1)) {
                    // System.out.println("deleted" + list.get(list.size() - 1));
                    list.remove(list.size() - 1);
                } else {
                    return false;
                }
            }
        } else {
            return false;
        }
        if (list.size() == 0){
            return true;
        } else {
            return false;
        }
    }
}
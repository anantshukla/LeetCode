class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> hm1 = new HashMap<Character, Integer>();

        for (Character c: s.toCharArray()) {
            hm1.put(c, hm1.getOrDefault(c, 0) + 1);
        }

        for (Character c: t.toCharArray()) {
            if(hm1.containsKey(c)) {
                int count = hm1.get(c) - 1;
                if (count == 0) {
                    hm1.remove(c);
                }
                else {
                    hm1.put(c, count);
                }
            }
            else {
                return false;
            }
        }
        return hm1.isEmpty();
    }
}
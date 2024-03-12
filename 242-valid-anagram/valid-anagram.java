class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int [] arr1 = new int[26];

        for (Character c: s.toCharArray()) {
            arr1[c - 'a']++;
        }

        for (Character c: t.toCharArray()) {
            arr1[c - 'a']--;
        }
        for (int val : arr1) {
            if (val != 0) {
                return false;
            }
        }
        return true;
    }
}
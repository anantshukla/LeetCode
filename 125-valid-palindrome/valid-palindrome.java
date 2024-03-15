class Solution {
public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        int l = 0, r = s.length() - 1;

        while(l < r) {
            while(l < r && !isLowerAlphaNumeric(s.charAt(l))) {
                l += 1;
            }
            while(l < r && !isLowerAlphaNumeric(s.charAt(r))) {
                r -= 1;
            }
            if(s.charAt(l) != s.charAt(r)) {
                return false;
            }
            l += 1;
            r -= 1;
        }
        return true;
    }
    
    public boolean isLowerAlphaNumeric(char c) {
        return (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9');
    }
}
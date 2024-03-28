public class Solution {
    public int NumberOfEmployeesWhoMetTarget(int[] hours, int target) {
        int n = 0;
        foreach(int hour in hours) {
            if (hour >= target) {
                n += 1;
            }
        }
        return n;
    }
}
public class Solution {
    public int NumberOfEmployeesWhoMetTarget(int[] hours, int target) {
        return hours.Where(s => s >= target).Count();
    }
}
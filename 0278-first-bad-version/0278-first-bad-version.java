/* The isBadVersion API is defined in the parent class VersionControl.
   boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int left = 1;
        int right = n;
        
        while (left < right) {
            // Prevents integer overflow condition: (left + right) / 2
            int mid = left + (right - left) / 2;
            
            if (isBadVersion(mid)) {
                // If mid is a bad version, the first bad version is either mid or to its left
                right = mid;
            } else {
                // If mid is a good version, the first bad version must be strictly to its right
                left = mid + 1;
            }
        }
        
        // When left == right, we have narrowed down to the first bad version
        return left;
    }
}

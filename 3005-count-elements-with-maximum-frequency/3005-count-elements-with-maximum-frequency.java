class Solution {
    public int maxFrequencyElements(int[] nums) {
        int[] frequencies = new int[101];
        int maxFrequency = 0;

        for(int num : nums) {
            frequencies[num]++;
            maxFrequency = Math.max(maxFrequency, frequencies[num]);
        } 
        int totalElements = 0;
        for(int freq : frequencies) {
            if(freq == maxFrequency) {
                totalElements += freq;
            }
        }
        return totalElements;
    }
}
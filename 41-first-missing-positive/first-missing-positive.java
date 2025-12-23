class Solution {
    public int firstMissingPositive(int[] nums) {
        Set<Integer> n = new HashSet<>();
        for(int i = 0; i < nums.length; i++) {
            n.add(nums[i]);
        }
        for(Integer j = 1; ; j++) {
            if(!n.contains(j)) {
                return j;
            }
        }
    }
}
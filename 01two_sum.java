/*****************************************
*Source: Leetcode Algorithm Challenger #1*
*Title: Two Sum 						 *
*Language: Java							 *
*Program Description: Given an array of  *
*integers, return indices of the two 	 *
*numbers that add up to a specific 		 *
*target.								 *
*Run time: 24ms							 *
******************************************/

class Solution {
    public int[] twoSum(int[] nums, int target) {
		int b[] = {0,0};
		for (int i = 0; i<nums.length-1; i++) {
			for (int j = i+1; j<nums.length; j++) { 
				if (nums[i] + nums[j] == target) {
					int c[] = {i,j};
					return c;
				}
			}
		}
		return b;
    }
}
# // Time Complexity :O(N)
# // Space Complexity :O(1)
# // Did this code successfully run on Leetcode :yes
# // Any problem you faced while coding this :NO
# https://leetcode.com/problems/sort-colors/description/

# // Your code here along with comments explaining your approach
# Here start with brute force , then count sort then use 3 pointers

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)-1
        l,m,h=0,0,n
        while(m<=h):
            if nums[m]==0:
                nums[m],nums[l]=nums[l],nums[m]
                m+=1
                l+=1
            elif nums[m]==2:
                nums[m],nums[h]=nums[h],nums[m]
                
                h-=1
            else:
                m+=1
                

                

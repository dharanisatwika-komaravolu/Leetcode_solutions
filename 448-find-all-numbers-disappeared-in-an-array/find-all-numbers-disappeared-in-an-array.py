class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
     
        # s = set(nums)
        # return [i for i in range(1, len(nums) + 1) if i not in s]
        
        a = []
        for c in nums:
            nums[abs(c)-1] = -abs(nums[abs(c)-1])
        for i in range(len(nums)):
            if nums[i] > 0:
                a.append(i+1)
        return a    
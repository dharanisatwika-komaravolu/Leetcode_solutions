class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # v = [-1] * (n + 1)
        # for i in nums:
        #     v[i] = i
        # for i in range(len(v)):
        #     if v[i] == -1:
        #         return i
        # return 0

        n = len(nums)
        sum_of_n = (n * (n + 1)) // 2
        actual_sum = sum(nums)

        return sum_of_n - actual_sum
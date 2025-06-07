class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # temp = sorted(nums)
        # dic = {}
        # for i, n in enumerate(temp):
        #     if n not in dic:
        #         dic[n] = i
        # r = []
        # for i in nums:
        #     r.append(dic[i])
        # return r
        # o(nlogn)

        count = [0] * 102
        for i in nums:
            count[i+1] += 1
        for i in range(1,102):
            count[i] += count[i-1] 
        return [count[n] for n in nums]

        # o(N)
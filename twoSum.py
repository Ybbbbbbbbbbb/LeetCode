class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 求出nums得长度
        length = len(nums)
        for i in range(length):
            if (target - nums[i]) in nums[i+1:]:
                return [i, nums[i+1:].index(target- nums[i])+1+i]

if __name__ == "__main__":
    s = Solution()
    result = s.twoSum([3, 3], 6)
    print(result)

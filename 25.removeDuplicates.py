class Solution:
    def removeDuplicates(self, nums):
        nums_len = len(nums)
        number = 0
        for i in range(nums_len):
            if i == 0:
                number += 1
            else:
                if nums[i] != nums[i-1]:
                    number += 1
                    nums[number-1] = nums[i]

        return number
                    
if __name__ == "__main__":
    s = Solution()
    number = s.removeDuplicates([1, 1, 2])
    print(number)
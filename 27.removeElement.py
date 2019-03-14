class Solution:
    def removeElement(self, nums, val):
        number = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[number] = nums[i]
                number += 1
            else:
                continue

        return nums[:number]

if __name__ == "__main__":
    s = Solution()
    result = s.removeElement([3, 2, 2, 3], 3)
    print(result)
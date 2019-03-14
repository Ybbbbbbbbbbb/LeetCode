class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)-1
        mid = 0
        while left <= right:
            mid =  int((left + right) /2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return mid if nums[mid]>target else mid+1

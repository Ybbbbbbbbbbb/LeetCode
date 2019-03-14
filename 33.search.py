class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0, len(nums) -1
        while left <= right:
             middle = int((left + right) /2) 
             if nums[middle] == target:
                 return middle
            else:
                if nums[middle] < nums[right]:
                    if nums[middle] < target and nums[right] >= target:
                        left = middle + 1
                    else:
                        right = middle - 1 

                else:
                    if nums[left] <= target and nums[middle] > target:
                        right = middle - 1
                    else:
                        left = middle + 1      
        return -1
"""
二分搜索法的关键在于获得了中间数后，判断下面要搜索左半段还是右半段，
我们可以观察出规律，如果中间的数小于最右边的数，则右半段是有序的，若中间数大于最右边数，则左半段是有序的，
我们只要在有序的半段里用首尾两个数组来判断目标值是否在这一区域内，这样就可以确定保留哪半边了，
"""
class Solution:
    def searchRange(self, nums, target):
        left, right = 0, len(nums)-1
        res = [-1, -1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        else:

            while left <= right:
                mid = int((left + right)/2)
                if nums[mid] == target:
                    if nums[mid-1] < target or mid -1 == -1:
                        res[0] = mid
                        break
                    else:
                        right = mid-1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid -1
            
            left, right = 0, len(nums)-1
            while left <= right:
                mid = int( (left + right) /2)
                if nums[mid] == target:
                    if mid+1 >= len(nums):
                        res[1] = mid
                        break
                    elif nums[mid+1] >  target:
                        res[1] = mid
                        break
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid -1

        return res

if __name__ == "__main__":
    s = Solution()
    result = s.searchRange([5,7,7,8,8,10], 8)
    print(result)

    
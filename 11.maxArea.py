class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxContain =temp =  0
        left , right = 0, len(height)-1
        while left < right:
            xx, yy = height[right], height[left]
            if yy < xx:
                temp = (right - left) * height[left]
                while height[left] <= yy:
                    left += 1
            else:
                temp = (right - left) * height[right]
                while height[right] <= xx and right:
                    right -= 1
            if temp > maxContain:
                maxContain = temp
        return maxContain
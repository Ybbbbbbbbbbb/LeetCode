class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        start, max_value = 0, 0
        substring = {}
        for key,value in enumerate(s):
            if  value in substring and  start <= substring[value]:
                start = substring[value] + 1
            else:
                max_value = max(max_value, key-start+1)
            substring[value] = key
        return max_value



if __name__ == "__main__":
    s = Solution()
    max_len = s.lengthOfLongestSubstring("abcabcbb")
    print(max_len)
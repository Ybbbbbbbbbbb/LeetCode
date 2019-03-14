class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = list(str(x))
        temp.reverse()
        new_temp = ''.join(temp)
        if str(x) == new_temp:
            return True
        else:
            return False           


if __name__ == "__main__":
    s = Solution()
    result = s.isPalindrome(121)
    print(result)
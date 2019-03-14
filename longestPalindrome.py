class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen = len(s)
        final_len = 0
        flag = False
        for i in range(maxlen, 0, -1):
            for j in range(maxlen):
                if j + i - 1 >= maxlen:
                    break
                else:
                    flag = self.isHuiWen(s, j, j+i-1)
                    if flag == True:
                        final_len = i
                        return s[j:j+i]
                    else:
                        continue
        if maxlen == 0:
            return ''
        else:
            return 'no solution'


    def isHuiWen(self, s, m, n):
        flag = True
        while m < n:
            if s[m] != s[n]:
                flag = False
                break
            else:
                m = m + 1
                n = n - 1
        return flag

if __name__ == "__main__":
    s = Solution()
    x = s.longestPalindrome('babad')
    print(x)
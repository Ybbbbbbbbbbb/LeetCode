class Solution:
    def longestCommonPrefix(self, strs) -> str:
        length = len(strs)
        if strs:
            length = min(map(len, strs))
        else:
            return ''
        flag = True
        max = 0
        for i in range(1, length+1):
            for j in range(1, len(strs)):
                if strs[0][:i] != strs[j][:i]:
                    flag = False
                    continue
            if flag == True and i > max:
                max = i
        return strs[0][:max]

if __name__ == "__main__":
    s = Solution()
    result = s.longestCommonPrefix(["flower","flow","flight"])
    print(result)
        
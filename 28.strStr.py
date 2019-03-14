class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack==needle:
            return 0
        needle_len = len(needle)
        for i in range(len(haystack)):
            x = haystack[i:i+needle_len]
            if haystack[i:i+needle_len] == needle and i + needle_len <= len(haystack) :
                return i
            else:
                continue
        return -1   

if __name__ == "__main__":
    s = Solution()
    result = s.strStr("mississippi","pi")
    print(result)
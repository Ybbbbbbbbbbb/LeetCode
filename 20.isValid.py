class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s == '':
            return True
        if len(s) % 2 == 1:
            return False
        dic = {
            '(':')',
            '{':'}',
            '[':']',
        }

        for i in range(len(s)):
            if stack:
                if s[i] != stack[-1]:
                    if s[i] not in dic:
                        return False
                    else:
                        stack.append(dic[s[i]])
                else:
                    stack.pop()
            else:
                if s[i] not in dic:
                    return False
                else:
                    stack.append(dic[s[i]])

        if stack:
            return False
        else:
            return True
"""
利用栈得原理即可得到
"""


if __name__ == "__main__":
    s = Solution()
    result = s.isValid("()[]{}")
    print(result)
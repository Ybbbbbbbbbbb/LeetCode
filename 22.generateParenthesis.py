class Solution:
    def generateParenthesis(self, n):
        return self.dfs(n, n, '', [])

    def dfs(self, l, r, s, res):
        if l :
            self.dfs(l-1, r, s + '(', res)
        if r and l < r :
            self.dfs(l, r-1, s+')', res)
        if not r :
            res.append(s)
        return res

"""
采用深度优先遍历dfs即可
"""

if __name__ == "__main__":
    
    s = Solution()
    result = s.generateParenthesis(4)
    print(result)
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        '''
        采用递归得思想求解此问题
        '''             
        # 若p为空时，只需要判断s是否为空                                                                                                                                                                                                  
        if p == '':
            return s == ''
        # 若p得长度为1，则只需要判断第一个值
        if len(p) == 1:
            return len(s) == 1 and (p[0] == s[0] or p[1] == '.')

        # 若p不为空时，判断p得第二个值是否为*，若不为*得话，就可以继续往后判断
        if p[1] != '*':
            if s == '':
                return False
            return (p[0] == s[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
        # 接下来就是判断p得第二个值为*得情况
        while s and (s[0] == p[0] or p[0] == '.'):
            if self.isMatch(s, p[2:]):
                return True
            s = s[1:]
        return self.isMatch(s, p[2:])


if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("aa", "a"))  # false
    print(s.isMatch("aa", "aa"))  # true
    print(s.isMatch("aaa", "aa"))  # false
    print(s.isMatch("aa", "a*"))  # true
    print(s.isMatch("aa", ".*"))  # true
    print(s.isMatch("ab", ".*"))  # true
    print(s.isMatch("aab", "c*a*b"))  # true
    print(s.isMatch("mississippi","mis*is*ip*."))


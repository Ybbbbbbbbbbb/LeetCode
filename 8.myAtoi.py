"""
使用正则表达式解决这道问题。因为数字前面不能够有其他字符，那么正则表达式可以从字符串得头开始检索，使用^。接着采用[\+\-]*匹配
正号和负号得数目，接着是\d+,也就是数字得数目，最少是1个，所以采用+号。
"""
import re
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        result = re.findall('^([\+\-]*\d+)', str)
        result = ''.join(result)
        try:
            result = int(result)
            if result > 2**31 -1:
                return 2**31 - 1
            elif result < -2 ** 31:
                return -2 ** 31
            else: 
                return result
        except:
            return 0 



if __name__ == "__main__":
    s =Solution()
    result = s.myAtoi("987and word")
    print(result)    
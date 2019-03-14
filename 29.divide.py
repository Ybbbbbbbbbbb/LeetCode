class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        output = 0
        flag = (dividend > 0 )  is (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, count = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += count

                count = count << 1
                temp = temp << 1
        if not flag:
            res = -res
        
        return min(max(-2147483648,res), 2147483647)

if __name__ == "__main__":
    s = Solution()
    result = s.divide(-1, -1)
    print(result)

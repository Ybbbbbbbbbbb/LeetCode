class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x >= 0:
            temp = list(str(x))
            temp.reverse()
            result = int(''.join(temp))
        else:
            x = -x 
            temp = list(str(x))
            temp.reverse()
            result = int(''.join(temp))
        return 0 if int(result) < -2** 31 or int(result) > 2**31 -1 else result


if __name__ == "__main__":
    s = Solution()
    result = s.reverse(-233)
    print(result)

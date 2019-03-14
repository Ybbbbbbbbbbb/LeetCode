import numpy as np
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        direction = 1 # to control row# movement
        rowIndex = 0 # indicate which lane to add element
        result = ['' for _ in range(numRows)] # declare a nested list in which each row is a list
        
        for i in range(len(s)):
            result[rowIndex] += (s[i])
            rowIndex += direction
            if rowIndex == 0 or rowIndex == numRows -1:
                direction *= -1
        return ''.join(result)    




if __name__ == "__main__":
    s = Solution()
    result = s.convert('PAYPALISHIRING', 3)
    print(result)
    ture_result = 'PAHNAPLSIIGYIR'
    if ture_result == result:
        print(True)
    else:
        print(False)   
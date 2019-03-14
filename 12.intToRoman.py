class Solution:
    def intToRoman(self, num: int) -> str:
        temp = list(str(num))
        result = ''.join(temp)
        middle = 1
        for i in range(len(result)-1, -1, -1):
            roman_number = result[i] * middle
            

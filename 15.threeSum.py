import itertools
import time
class Solution:
    def threeSum(self, nums):
        s = []
        q = []
        result = list(itertools.combinations(nums, 3))
        for i in range(len(result)):
            if result[i][0] + result[i][1] + result[i][2 ]== 0:
                temp = sorted(result[i])
                if temp not in q:
                    q.append(temp)
                    s.append(result[i])

        return s

if __name__ == "__main__":
    s = Solution()
    t1 = time.time()
    print(t1)
    result = s.threeSum()
    t2 = time.time()
    print(t2 - t1)



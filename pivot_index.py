# Find the middle number from the following list
class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        left = 0
        
        for i,v in enumerate(nums):
            # print(total)
            # print(left)
            # print(v)
            # print()
            # print()
            if left == (total-left-v):
                return i
            left += v
        return -1
            
s = Solution()
print(s.pivotIndex([1,7,3,6,5,6]))
print(s.pivotIndex([1,2,3]))
print(s.pivotIndex([2,1,-1]))
class Solution(object):
    def containsDuplicate(self, nums):
        s=set()
        for ele in nums:
            if ele in s:
                return True
            else:
                s.add(ele)
        

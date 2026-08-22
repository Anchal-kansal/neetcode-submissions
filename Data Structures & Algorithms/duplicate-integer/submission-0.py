class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = []
        for i in range(0,len(nums)):
            if nums[i] not in nums2:
                nums2.append(nums[i])
            else:
                return True
        return False

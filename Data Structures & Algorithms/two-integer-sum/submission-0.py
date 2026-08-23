class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        nums2={}
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    output.append(i)
                    output.append(j)
                else:
                    j=j+1
        return output
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force - 

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        # return 0

        #optimized -

        seen={}
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in seen:
                return [seen[comp],i]
            seen[nums[i]]=i
        return 0
            
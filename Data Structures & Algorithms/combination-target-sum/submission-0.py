class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ds=[]
        ans=[]

        def findcomb(ind:int , target:int):
            if ind==len(nums):
                if target==0:
                    ans.append(ds[:])
                return 
            if nums[ind]<=target:
                ds.append(nums[ind])
                findcomb(ind,target-nums[ind])
                ds.pop()
            findcomb(ind+1,target)
        findcomb(0,target)
        return ans
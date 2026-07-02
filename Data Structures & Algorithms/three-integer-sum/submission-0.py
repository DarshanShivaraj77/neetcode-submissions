class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        x=sorted(nums)
        for i in range(len(x)):
            if i > 0 and x[i] == x[i - 1]:
                continue
            l=i+1
            r=len(x)-1
            while l<r:
                s=x[i]+x[l]+x[r]
                if s==0:
                    res.append([x[i],x[l],x[r]])
                    l += 1
                    r -= 1
                    
                    # Skip duplicates for second and third elements
                    while l < r and x[l] == x[l - 1]:
                        l += 1
                    while l < r and x[r] == x[r + 1]:
                        r -= 1
                elif s<0:
                    l+=1
                else:
                    r-=1
        return res
                    
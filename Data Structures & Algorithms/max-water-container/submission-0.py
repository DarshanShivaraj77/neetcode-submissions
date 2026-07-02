class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        res=0
        r=len(heights)-1
        while(l<r):
            h=min(heights[r],heights[l])
            w=r-l
            area=h*w
            res=max(res,area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return res
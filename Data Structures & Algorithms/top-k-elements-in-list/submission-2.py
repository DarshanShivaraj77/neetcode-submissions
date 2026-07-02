class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countS={}
        for i in nums:
            countS[i]=1+countS.get(i,0)
        sorted_items=sorted(countS,key=countS.get,reverse=True)
        return sorted_items[:k]
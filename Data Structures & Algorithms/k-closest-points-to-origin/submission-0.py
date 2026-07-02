class Solution:
    def Dis(self,point):
        return point[0]*point[0]+point[1]*point[1]
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap=[]
        for i in range(len(points)):
            dist=self.Dis(points[i])
            if len(maxHeap)<k:
                heapq.heappush(maxHeap,(-dist,points[i]))
            else:
                if dist < -maxHeap[0][0]:
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap,(-dist,points[i]))
        res=[]
        while maxHeap:
            res.append(heapq.heappop(maxHeap)[1])
        return res

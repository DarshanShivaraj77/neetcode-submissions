"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        start=node
        otn={}
        visited=set()
        visited.add(start)
        stk=[start]

        while stk:
            node=stk.pop()
            otn[node]=Node(val=node.val)
            for n in node.neighbors:
                if n not in visited:
                    visited.add(n)
                    stk.append(n)
        for onode,nnode in otn.items():
            for n in onode.neighbors:
                newn=otn[n]
                nnode.neighbors.append(newn)
        return otn[start]
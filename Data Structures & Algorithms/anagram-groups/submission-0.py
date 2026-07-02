class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp=defaultdict(list)
        for word in strs:
            key=''.join(sorted(word))
            grp[key].append(word)
        return list(grp.values())
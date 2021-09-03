class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for s in strs:
            srt = ''.join(sorted(s))
            if srt not in d:
                d[srt] = []
            d[srt].append(s)
        
        return [d[k] for k in d]
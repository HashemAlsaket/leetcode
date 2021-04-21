# Link to video: https://youtu.be/b2fugW2gRzE

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        n = len(strs)
        com = []
        
        min_len = min(map(len, strs))
        
        for i in range(min_len):
            if len(set([s[i] for s in strs])) == 1:
                com.append(strs[0][i])
            else:
                break
        
        return ''.join(com)
        
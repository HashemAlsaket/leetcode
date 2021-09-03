class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size(), i = 0, j = 0, mx = 0;
        
        unordered_map<char, int> m;
        
        while (j < n){
            mx = max(mx, j - i);
            
            if (m.find(s[j]) != m.end()){
                if (m[s[j]] > 0){
                    while (m[s[j]] > 0){
                        m[s[i]] = m[s[i]] - 1;
                        i ++;
                    }
                }
            }
            if (m.find(s[j]) == m.end()){
                m[s[j]] = 1;
            } else{
                m[s[j]] = m[s[j]] + 1;
            }
            j ++;
        }
        mx = max(mx, j - i);
        return mx;
    }
};
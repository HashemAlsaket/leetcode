func lengthOfLongestSubstring(s string) int {
    n := len(s)
    i := 0
    j := 0
    mx := 0
    m := make(map[string]int)
    
    for j < n{
        if mx < j - i{
            mx = j - i
        }
        if _, ok := m[string(s[j])]; ok{
            if m[string(s[j])] > 0{
                for m[string(s[j])] > 0{
                    m[string(s[i])] = m[string(s[i])] - 1
                    i = i + 1
                }
            }
        }
        m[string(s[j])] = m[string(s[j])] + 1
        j = j + 1
    }
    if mx > j - i{
            mx = mx
        } else{
            mx = j - i
        }
    return mx
}
func groupAnagrams(strs []string) [][]string {
    m := make(map[string][]string)
    var res [][]string
    
    for i := 0; i < len(strs); i++{
        s := sorted(strs[i])
        if _, ok := m[s]; ok{
            m[s] = append(m[s], string(strs[i]))
        } else{
            m[s] = []string{strs[i]}
        }
    }
    
    for key, _ := range m{
        res = append(res, m[key])
    }
    return res
}

func sorted(str string) string {
    s := strings.Split(str, "")
    sort.Strings(s)
    return strings.Join(s, "")
}
import "sort"

func merge(intervals [][]int) [][]int {
    sort.Slice(intervals[:], func(i, j int) bool {
        return intervals[i][0] < intervals[j][0]
    })
    
    var res [][]int
    var mn int
    var mx int
    var arr []int
    
    arr = intervals[0]
    intervals = intervals[1:]
    
    for i := 0; i < len(intervals); i ++{
        if arr[1] >= intervals[i][0]{
            if arr[0] < intervals[i][0]{
                mn = arr[0]
            } else{
                mn = intervals[i][0]
            }
            if arr[1] > intervals[i][1]{
                mx = arr[1]
            } else{
                mx = intervals[i][1]
            }
            arr = []int{mn, mx}
        } else{
            res = append(res, arr)
            arr = intervals[i]
        }
    }
    res = append(res, arr)
    return res
}
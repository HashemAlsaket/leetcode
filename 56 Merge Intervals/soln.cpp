class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        
        vector<vector<int>> res;
        
        vector<int> arr;
        arr = intervals[0];
        
        for (int i = 1; i < intervals.size(); i++){
            if (arr[1] >= intervals[i][0]){
                arr = {min(arr[0], intervals[i][0]), max(arr[1], intervals[i][1])};
            } else{
                res.push_back(arr);
                arr = intervals[i];
            }
        }
        res.push_back(arr);
        return res;
    }
};
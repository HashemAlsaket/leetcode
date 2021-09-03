class Solution {
public:
    bool isValid(string s) {
        vector<char> Stack;
        
        for (int i = 0; i < s.size(); i++){
            string l;
            l = s[i];
            if (l == "(" || l == "{" || l == "["){
                Stack.push_back(s[i]);
                continue;
            }
            if (Stack.size() == 0){
                return false;
            }
            string p;
            p = Stack[Stack.size() - 1];
            Stack.pop_back();
            
            if (l == ")" && p != "("){
                return false;
            }
            if (l == "]" && p != "["){
                return false;
            }
            if (l == "}" && p != "{"){
                return false;
            }
        }
        return Stack.size() == 0;
    }
};
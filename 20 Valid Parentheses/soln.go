func isValid(s string) bool {
    var stack []string
    
    for i := 0; i < len(s); i++{
        l := string(s[i])
        if l == "(" || l == "[" || l == "{"{
            stack = append(stack, l)
            continue;
        } 
        if len(stack) == 0{
            return false;
        }
        p := stack[len(stack) - 1]
        stack = stack[:len(stack) - 1]
        
        if l == ")" && p != "("{
            return false
        }
        if l == "]" && p != "["{
            return false
        }
        if l == "}" && p != "{"{
            return false
        }
    }
    return len(stack) == 0
}
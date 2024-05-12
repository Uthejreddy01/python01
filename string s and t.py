def isomorphic(s, t):
    s_to_t = {}
    t_to_s = {}
    if len(s) != len(t):
        return False
    for char_s, char_t in zip(s, t):
        if char_s in s_to_t and s_to_t[char_s] != char_t:
            return False
        if char_t in t_to_s and t_to_s[char_t] != char_s:
            return False
        s_to_t[char_s] = char_t
        t_to_s[char_t] = char_s
    return True
print(isomorphic("egg", "add"))  
print(isomorphic("foo", "bar"))  
print(isomorphic("paper", "title"))  
print(isomorphic("fry", "sky"))  
print(isomorphic("apples", "apple"))  
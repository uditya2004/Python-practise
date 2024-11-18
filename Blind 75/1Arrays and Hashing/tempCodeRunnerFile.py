def isAnagram(s, t):
    dict_s = {}
    dict_t = {}

    #Case - 1
    if len(s) != len(t):
        return False

    #Case - 2
    for i in s:
        if i not in t:
            return False

    #Finding the count of character in "s"
    for i in range(0,len(s)):
        if s[i] in dict_s:
            dict_s[s[i]] +=1
        else:
            dict_s[s[i]] =1

    #Finding the count of character in "t"
    for i in range(0,len(t)):
        if t[i] in dict_t:
            dict_t[t[i]] +=1
        else:
            dict_t[t[i]] =1
    
    if dict_s == dict_t:
        return True
    
    else:
        return False



s = "anagram" 
t = "naggram"

print(isAnagram(s, t))
def minWindow(s, t) :

    if t == "":      # Edge case
        return ""

    countT = {}
    window = {}

    for i in t:
        countT[i] = 1 + countT.get(i, 0)     # storing the frequency of all elements in t
     
    
    have = 0                    # no. of characters of t we currently have in s
    need = len(countT)          # Why we need unique? we need these many characters in our possible substring

    res = [-1,-1]               # result stores the start and end index of possible answer (substring)
    resLen = float("inf")       # length of possible answer substring, as we need length to be minimum so we initialize it with inf
    l = 0                       # Left pointer, initialize at the start of string
    
    for r in range(len(s)):     # right pointer 
        c = s[r]
        window[c] = 1 + window.get(c, 0)             # storing the frequency of char where pointer is at.

        if c in countT and window[c] == countT[c]:   # we don't care about the char which are not in countT
            have +=1
        
        while have == need:
            #update our result
            if (r-l+1) < resLen:
                res = [l, r]       
                resLen = (r-l+1)
            
            #pop from the left of our window
            window[s[l]] -=1                                     # decrementing the frequency as we move the "l" pointer
            if s[l] in countT and window[s[l]] < countT[s[l]]:   # if the removed elemnent from back was a part of "t" , then we decrement the "have", as now we will be in need of that 1 removed character
                have -=1

            l +=1     # moving the left pointer forward
    
    l,r = res

    if resLen != float("inf"):
        return s[l:r+1]
    else:
        return ""

s = "aaaaaaaaaaaabbbbbcdd"
t = "abcdd"
print(minWindow(s, t))
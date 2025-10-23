"""
Given a string s, find the length of the longest substring without repeating characters.

A substring is a contiguous non-empty sequence of characters within a string.
"""

#Using 2 pointers and a list :- Brute Force
#TC: O(N^2)
#SC: O(N)

def lengthOfLongestSubstring(s):
    
    length = 0
    for i in range(0, len(s)):
        temp_seq = []       # SC: O(N)

        for j in range(i, len(s)):
            
            if s[j] not in temp_seq:
                temp_seq.append(s[j])
                length = max(length, len(temp_seq)) #Update the length
            else:
                break

    return length



s = "pwwkew"  #Expected output :- 1
print(lengthOfLongestSubstring(s))

#=========================
#Using 2 pointers and a hash array + ascii of character :- Brute Force (optimized brute force)
#TC: O(N^2)
#SC: O(255) = O(1)

def lengthOfLongestSubstring(s):
    
    length = 0
    

    for i in range(0, len(s)):
        hash = [0]*255         # Total possible characters are 255

        for j in range(i, len(s)):
            
            if hash[ord(s[j])] == 1:
                break
            
            else:
                length = max(length, j-i+1) #Update the length
                hash[ord(s[j])] = 1

    return length


s = "pwwkew"  #Expected output :- 1
print(lengthOfLongestSubstring(s))


#=========================
#Using 2 pointers Sliding window :- Best Solution
#TC: O(N)
#SC: O(N)

def lengthOfLongestSubstring(s):
    
    max_len = 0
    dict1= {}     #SC: O(N)

    i=0
    j=i
    while i<len(s) and j < len(s):

        if s[j] in dict1:
            if dict1[s[j]] >= i:     # if the character is already present in the dictionary and is between i and j , then current element (s[j]) is a duplicate and is present already in the previous subarray length. So shrink window by moving the i to next next of character to remove the duplicate from the wimdow. 
                i = dict1[s[j]] + 1 # move the i to the next index of of the duplicate element already in the subarray.
        
        max_len = max(max_len, j-i+1)   # update the max_len
        dict1[s[j]] = j                 # update the index of character in dictionary
        j +=1                           # move the pointer j

    return max_len

s = "pwwkew"  
print(lengthOfLongestSubstring(s))
"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

#Using sort()
#TC: O(NlogN + N) = O(NLogN)
#SC: O(N)

# def longestConsecutive(nums):
#     lst = sorted(nums)            #TC: O(NLogN), SC: O(N)
#     max_count = float("-inf")
#     current_count = 1

#     for i in range(1, len(lst)):
#         if lst[i] == lst[i-1] +1 :
#             current_count +=1
#             max_count = max(max_count, current_count)
        
#         else:
#             current_count = 1
    
#     return max_count


# nums = [100,4,200,1,3,2]
# print(longestConsecutive(nums))

#===================================
#element-1 not in nums, then it's the first element of the sequence, check element+1 in nums until it's not found, increasing count on the way 
#TC: O(N) 
#SC: O(N)

def longestConsecutive(nums):
    if len(nums) == 0:
        return 0

    longest = 1
    new_arr = set(nums)   #TC: O(N)  , put all the array elements into set (Use a Set for Fast Lookups)

    # Find the longest sequence
    for element in nums:                 #TC: O(N)
        """
        - List Lookup:- Searching for an item in a list has a time complexity of O(n).
        - Set Lookup:- Searching for an item in a set has an average time complexity of O(1). Sets use a hash table, which allows for near-instantaneous lookups.
        """
        if element-1 not in new_arr:        #then it's the first element of the sequence
            
            # find next consecutive numbers from the current element
            x=element
            count = 1
            while x+1 in new_arr:  
                count +=1
                x +=1
            
            longest = max(longest, count)    #Updating the longest
    
    return longest



nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))
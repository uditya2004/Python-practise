"""
Problem Statement: You are given an array of 'N' integers. You need to find the length of the longest sequence which contains the consecutive elements.
"""
#Method 1:- For every element x , we find x+1 , x+2 and so on , using linear search. And we take the max length from all possible sequences. (Brute Force)
# TC: O(N^2)
# SC: O(1)
# def linearSearch(arr, key):
#     result = False
#     for i in arr:
#         if i == key:
#             return True
    
#     return False


# def longestSequence(arr,n):
#     max_count = 1  # 

#     for i in range(0,n):
#         x = arr[i]  # 
#         count = 1
#         while linearSearch(arr, x+1) == True:  #
#             x +=1
#             count +=1
#         max_count = max(max_count, count)
        
#     return max_count



# arr = [100, 200, 1, 3, 2, 4]      #Output:  4   consecutive subsequence is 1, 2, 3, and 4.
# print("The longest consecutive sequence is:-",longestSequence(arr,len(arr)))

#=========================================
#Method 2:- (Better Solution)
# TC: O(NlogN) + O(N)
# SC: O(1)

def longestSuccessiveElements(arr):
    n = len(arr)
    if n == 0:
        return 0

    # sort the array
    arr.sort()        # O(Nlog N). As it use merge sort algo.
    lastSmaller = float('-inf')
    cnt = 0     
    longest = 1

    # find longest sequence
    for i in range(n):
        if arr[i] - 1 == lastSmaller:   # a[i] is the next element of the current sequence         
            cnt += 1  
            lastSmaller = arr[i]

        elif arr[i] == lastSmaller:        #  If the current element, arr[i], matches the lastSmaller , we can skip it since we have already included it before.
            pass

        elif arr[i] != lastSmaller:
            cnt = 1         # We reset the count to 1 (starting a new sequence)
            lastSmaller = arr[i]
            
        longest = max(longest, cnt)
    return longest

a = [100, 200, 1, 2, 3, 4]
ans = longestSuccessiveElements(a) 
print("The longest consecutive sequence is", ans)


#============================
#Method 3:- Using Set Data Structure (Optimal Solution)

def longestSuccessiveElements(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    longest = 1
    new_arr = set(arr)   # put all the array elements into set

    # Find the longest sequence
    for element in new_arr:
        if element-1 not in new_arr:    #if element-1 is not in set , then this element will be the starting element of the sequence
            
            # find consecutive numbers
            count = 1
            x = element
            while x+1 in new_arr:
                x +=1
                count +=1

            longest = max(longest, count)  #Updating the longest
            
    return longest




a = [100, 200, 1, 2, 3, 4]
ans = longestSuccessiveElements(a) 
print("The longest consecutive sequence is", ans)
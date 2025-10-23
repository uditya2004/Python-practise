"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""
# Using dictionary for count + Reverse sort
# TC: O(N + N + NLogN + K) = O(NLogN)
# SC: O(N + N + K) = O(N)
def topKFrequent(nums, k):

    #Storing the frequency of each element in dictionary
    dict1 = {}
    for i in nums:
        dict1[i] = 1 + dict1.get(i,0)
    
    #Storing in an array so we can reverse sort it
    arr = []
    for num,cnt in dict1.items():
        arr.append([cnt,num])
    arr.sort(reverse=True)    #Reverse sorting (sort by cnt [cnt,num], but if two element have same cnt, then sort by num)

    # taking k elements from starting of "arr"
    result = []
    for j in range(0,k):
        result.append(arr[j][1])
    
    return result


nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))


#========================================
# Using dictionary for count + array with count as indexes (BUCKET SORT) - Best Solutions
#TC: O(N + N + N + N*K) = O(N), as k is smaller than N
#SC: O(N + N + K) = O(N)
def topKFrequent(nums, k):

    #Storing the frequency of each element in dictionary
    dict1 = {}
    for i in nums:
        dict1[i] = 1 + dict1.get(i,0)
    
    # Creating an array with frequency as it's index and storing all the element having same frequency at the same index in list container
    # arr = [[]] * (len(nums)+1)                  #Incorrect way :- all elements in arr will point to the same list. Modifying one of these lists will affect all of them because they are all references to the same object.
    arr = [[] for i in range(len(nums) + 1)]      # Correct way
    for num,cnt in dict1.items():
        arr[cnt].append(num)
    
    #Printing the result by traving from right to left in arr to get the top K frequent 
    result = []
    for i in range(len(arr)-1,0,-1):

        for j in range(0, len(arr[i])):    #As each element is a list , so traving that single element at index i
            result.append(arr[i][j])       # appending all the element of list stored at index i to result

            if len(result) == k:           # To get only k elements , we stop appending when the size of result reaches k
                return result
    

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))





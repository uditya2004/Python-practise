"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


# Using 3 pointers, check all combinations:- Brute Force
#TC: O(N^3)
#SC: O(2T) = O(T), T is number of triplets
# def threeSum(nums):
#     res = set()  #SC: O(N),      We used res = set() , so we can avoid addition of duplicate triplets

#     for i in range(0,len(nums)):                #1st number loop

#         for j in range(i+1, len(nums)):         #2nd number loop
#             for k in range(j+1, len(nums)):     #3rd number loop

#                 if nums[i] + nums[j] + nums[k] == 0:
#                     res.add(tuple( sorted([nums[i], nums[j], nums[k]]) ))    
#                     """
#                     - we sort the array "sorted([nums[i], nums[j], nums[k]])", so we can make same tripplet look alike (if they both are not in same order initially)
#                     - we converted list to tuple "tuple([nums[i], nums[j], nums[k]])", as each element of a set should be immutable
#                     """
    
#     #Converting result back to list
#     res2 = []   #SC: O(N)
#     for i in res:
#         res2.append(list(i))
    
#     return res2

# nums = [-1,0,1,2,-1,-4]
# print(threeSum(nums))

#=========================================
# Using 2 pointers + hashing:- Better Solution
#TC: O(N + N^2) = O(N^2)
#SC: O(N + T + T) = O(N) , where T is number of unique triplet 
def threeSum(nums):
    result = set()       #SC: O(T)

    # Putting elements with index in dictionary for fast searching
    dict1 = {}           #SC: O(N)
    for index, element in enumerate(nums):
        dict1[element] = index
    
    
    for i in range(0,len(nums)):    #1st num loop
        for j in range(i+1, len(nums)):    # 2nd num lop  &  1st + 2nd + 3rd = 0   -> 3rd = -(1st + 2nd)
            
            # Calculate the 3rd element:
            num_3 = -(nums[i] + nums[j])        #If we found 3rd element in the dict, then we don't need to check 1st + 2nd + 3rd == 0 , as we have calculated 3rd in a way it will make sum zero

            # Find the element in the set:
            if num_3 in dict1 and dict1[num_3]>j:       # "dict1[num_3]>j" make sure 3rd element is of diffent indexes than i and j
                result.add( tuple( sorted([nums[i], nums[j], num_3]) ))
                
    #Converting result back to list
    res2 = []   #SC: O(T)
    for i in result:
        res2.append(list(i))
    
    return res2


nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

#============================
# Fix one number and then solve like 2 SUM
#TC: 
#SC: 
# def threeSum(nums):
#     nums.sort()
#     result = []
#     for i,a in enumerate(nums):       

#         low = i+1
#         high = len(nums)-1

#         if i>0 and nums[i] == nums[i-1]:   # to avoid duplicate triplets  . "i>0" so checking i-1 doesn't case error
#             continue

#         while low<high:
#             if a + nums[low] + nums[high]> 0:
#                 high -=1
#             elif a + nums[low] + nums[high]< 0:
#                 low +=1
#             else:
#                 result.append([a, nums[low], nums[high]])
            
#             low +=1
#             while nums[low]  == nums[low-1] and low<high:
#                 low +=1


# nums = [-1,0,1,2,-1,-4]
# print(threeSum(nums))
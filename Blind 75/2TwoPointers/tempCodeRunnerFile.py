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
                
                # Sorted :- to avoid duplicate triplet, duplicate triplet looks same when sorted.
                # made Tuple because:- Lists are mutable, and Python does not allow mutable objects inside a set (because elements in a set must be hashable).
                result.add(( sorted([nums[i], nums[j], num_3]) ))         
                
                
                
    #Converting result back to list
    return [list(i) for i in result]   #SC: O(T)
    

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
def threeSum(nums):
    result = set()   #SC: O(T)

    for i in range (len(nums)):
        hashmap = set()           # SC: O(N), We clear hashmap before moving to next num[i] and we use set data structure as we don't need to store indexes corresponding to element like in dictionary
        for j in range(i+1, len(nums)):

            # Calculate the 3rd element:
            num_3 = -(nums[i] + nums[j])

            # Find the element in the set:
            if num_3 in hashmap:
                result.add(tuple(sorted([nums[i], nums[j], num_3])))
            else:
                hashmap.add(nums[j])   # before moving add the current element to hashmap

    return [list(i) for i in result]


nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
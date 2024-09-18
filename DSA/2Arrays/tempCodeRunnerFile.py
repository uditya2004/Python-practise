def findsum (n, arr, target) :
    nums = sorted(arr) 
    left = 0
    right = n-1

    while left<right:
        if nums[left] + nums[right] > target:
            right -=1

        elif nums[left] + nums[right] == target:
            return "YES"

        else:
            left +=1
    
    return "NO", [-1,-1]


print(findsum(n = 5, arr= [2,6,5,8,11], target = 1))
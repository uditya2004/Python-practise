"""
Note: Subarray means , contiguous part of an array , (array mein se kahi se bhi pick krke subarray nhi bna skte, all collected elements should be next to each other.)
"""
#Method
def getLongestSubarray(a, k):
    n = len(a) # size of the array.

    left, right = 0, 0 # 2 pointers
    Sum = a[0]
    maxLen = 0
    while right < n:
        # if sum > k, reduce the subarray from left
        # until sum becomes less or equal to k:
        while left <= right and Sum > k:
            Sum -= a[left]
            left += 1

        # if sum = k, update the maxLen i.e. answer:
        if Sum == k:
            maxLen = max(maxLen, right - left + 1)

        # Move forward the right pointer:
        right += 1
        if right < n: 
            Sum += a[right]

    return maxLen


if __name__ == "__main__":
	a = [2, 3, 5, 1, 9]
	k = 10

	length = getLongestSubarray(a, k)
	print(f"The length of the longest subarray is: {length}")

#===================
#Method
def longSubArray(array, N, k):
    maxLength = 0
    sum = 0
    for i in range(0, N):

        for j in range(i, N):
            if sum <k:
                sum += array[j]
            
            if sum == k:
                maxLength = max(maxLength, j-i + 1 )

            if sum>= k:
                sum = 0
                break     
    
    return maxLength

 
array = [2,3,5]
N = 3     #Length of array
k = 5     #Sum

print("Final Answer:- ", longSubArray(array, N, k))


#===================

def getLongestSubarray(a, k):
    i=0
    j=0
    sum = a[0]
    length = 0


a = [2, 3, 5, 1, 9]
k = 10

length = getLongestSubarray(a, k)
print(f"The length of the longest subarray is: {length}")









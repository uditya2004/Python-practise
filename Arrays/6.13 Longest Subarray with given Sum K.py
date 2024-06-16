"""
Note: Subarray means , contiguous part of an array , (array mein se kahi se bhi pick krke subarray nhi bna skte, all collected elements should be next to each other.)
"""
# Method 1 - Using 2 pointers. One Traversal solution. Time Complexity O(N)
# def subarr(lst,sum):
#     sum2=0        # sum of subarray
#     all_len = []   # storage of length of all possible subarray having sum = k
#     i=0
#     for j in range(i,len(lst)):
#         sum2 += lst[j]

#         if sum2==sum:
#             if j==len(lst):
#                 all_len.append((j-i)+1)  #if j reaches last index , we don't do those extra 2 steps. We just add the length
#                 break
#             else:
#                 all_len.append((j-i)+1)
#                 i = j+1    #Once sum2==sum , move the index i to the next index of j (i.e j+1) 
#                 sum2=0     #Reset the sum2 to be 0
    
#     return max(all_len)


# # a = [2, 3, 5, 1, 9]
# a2=[1,2,3,1,1,1,1,3,3]
# k = 6
# print(subarr(a2,k))
# # print(subarr(a,k))
#========================

# Method 1 - Using 2 pointers. One Traversal solution. Time Complexity O(N) and Space complexity O(1)
def subarr(lst,sum):
    sum2=0        # sum of subarray
    length=0
    i=0
    j=0
    # for j in range(i,len(lst)):
    while j>=i and j<len(lst):
        sum2 += lst[j]

        if sum2==sum:
            if j==len(lst):
                length=max(length,(j-i)+1)  #if j reaches last index , we don't do those extra 2 steps. We just add the length
                break
            else:
                length=max(length,(j-i)+1)
                i = j           #Once sum2==sum , move the index i to the index of j.
                sum2=lst[j]     #Reset the sum2 to be the number were j is currently
                
        j +=1
    return length


a1 = [2, 3, 5, 1, 9]
k1 = 10
print(subarr(a1,k1))

a2=[1,2,3,1,1,1,1,3,3]
k2= 6
print(subarr(a2,k2))







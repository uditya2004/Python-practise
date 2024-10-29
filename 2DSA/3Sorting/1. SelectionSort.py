#selection sort Algorithm

#method 1
# lst=[1,5,6,7]
# i=0
# maxel_ind=0

# print("original list:- ", lst)

# while i< (len(lst)-1):
#     #finding max element
#     for k in range(i,len(lst)):
#        if lst[k] >lst[maxel_ind]:
#           maxel_ind=k
#     print("index of max element:", maxel_ind)
  
#     #swap elementnpostions
#     lst[i],lst[maxel_ind]= lst[maxel_ind],lst[i]
#     print("new list:-",lst)
#     i+=1
#     print("new i postion:",i,"\n")

#============================================

#Method 2- Better Method
#Selection sort
def Sorted(arr):
    n = len(arr)
    for i in range(0,n-1):
        minInd = i

        for j in range(i+1, n):
            if arr[minInd] > arr[j]:
                minInd = j

        arr[i], arr[minInd] = arr[minInd], arr[i]   #Swapping
    
    return arr


arr = [13,46,24,50,20,9]
print("Original Array: ", arr)
print("Sorted array: ", Sorted(arr))

#Output : [9, 13, 46, 24, 50, 20]
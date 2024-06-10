
"""
1. We can create an array using "array module"
2. List in python is a dynamic array, which can change it's size as per needs , whereas size of an array can't be changed once declared.
"""
import array

#CREATING AN ARRAY USING ARRAY MODULE
a= array.array("i",[2,1,4,3])
# print(type(a))


#INSERTING VALUES
# a.insert(1,5)  # inserting 5 in index 1
# print(a)

#REMOVE AN ELEMENT
# a.remove(3)  # removing the element 3
# print(a)

# TRAVERSAL
# for i in a:
#     print(i)

# SEARCHING THE INDEX OF AN ELEMENT
# print(a.index(3)) #finding the index of element 3

#SORT
# As "sort()" is for array , we need to convert array into list first.
# lst= list(a)
# lst.sort()
# print(lst)

#---------------
#LIST COMPREHENSION

#Method 1 - Basic method to add all the elements of list smaller than a
# def separate(lst,a):
#     result = []
#     for i in lst:
#         if i < a:
#             result.append(i)
#     return result

# print(separate([1,2,3,4],3))

#Method 2 - shortcut (list comprehension method)
def separate(lst,a):
    result = [i for i in lst if i<a]
    return result

print(separate([1,2,3,4],3))
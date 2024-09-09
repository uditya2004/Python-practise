#Method 1: Using Temporary Array
# TC: O(N)
# SC: O(N)  {Using temp array "temp"}

# def check_pal(str):
#     temp = ""
#     for i in range(len(str)-1, -1, -1):
#         temp = temp + str[i]

#     if temp == str:
#         print("True")
#     else:
#         print("False")


# str1 = "ABCDCBA"
# check_pal(str1)

#============================
#Method 2: Using 2 Pointer (Run a for loop till half the length of the string in order to check the first and last character of the string.)
# TC: O(N/2) = O(N)
# SC: O(1)  {Using temp array "temp"}

# def check_pal(str, low , high):
#     mid = (low + high) // 2

#     while low<mid or high>mid:
#         if str[low] != str[high]:
#             return False
#         else:
#             low = low + 1
#             high =high - 1
    
#     return True        


# str1 = "ABCDCBA"
# print(check_pal(str1, 0, len(str1) - 1))

#===========================================
# Method 3: Functional Recursion

def check_pal(str, low , high):
    if low>=high:
        return True
    else:
        if str[low] != str[high]:
            return False
        
        return check_pal(str, low + 1 , high - 1)


str1 = "ABCDCBA"
print(check_pal(str1, 0, len(str1) - 1))
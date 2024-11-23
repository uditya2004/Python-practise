"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

#Using 2 pointers loops: Brute force
# TC: O(N^2)
# SC: (1)

# def maxArea(height):
#     max_vol = 0

#     for i in range(0, len(height)):

#         for j in range(i+1, len(height)):
#             length_container = min(height[i], height[j])
#             width_container = j-i

#             temp_vol = length_container *width_container

#             max_vol = max(max_vol, temp_vol)
    
#     return max_vol


# height = [1,1]
# print(maxArea(height))

#========================
# 2 pointer and move the pointer having the smallest line because smallest line control the volume ,  if we move the biggest line pointer, water level height will remains the same but the width will decrease which will always decrease the volume.
#TC: O(N) , as each element in the list is considered at most once.
#SC: O(1) 
def maxArea(height):
    max_vol = 0

    low = 0
    high = len(height)-1

    while low<high:
        temp_vol = min(height[low], height[high]) * (high-low)

        max_vol = max(max_vol, temp_vol)

        if height[low] < height[high]:
            low +=1
        elif height[low] > height[high]:
            high -=1
        else:
            low +=1

    return max_vol



height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
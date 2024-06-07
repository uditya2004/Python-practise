"""
RULES FOR PRINTING PATTERNS
1. Use Nested loops
2. For the outer loop, StarCount the no. of rows.
3. For inner loop, StarCount the no. of columns and connect them somehow to the rows.
4. Print * in the inner FOR loop
5. Observe symmytry (optional)

"""

#========================
"""
****
****
****
****
"""

# for i in range (4): #rows
#     for j in range (4): #columns
#         print("*",end="")
    
#     print() #print() function automatically adds a newline character (\n) to the end of the string it prints.

#========================
"""
*
**
***
****
"""

# for i in range (1,5): #rows
#     for j in range (i):
#         print("*",end=" ")
#     print()

#========================
"""
1
12
123
1234
12345
"""

# for i in range (1,6):
#     for j in range (1,i+1):
#         print(j, end = " ")
#     print()

#========================
"""
1
22
333
4444
55555
"""
#NOT THE BEST SOLUTION
# n=5
# for i in range (1,n+1):
#     for j in range (i):
#         print(i, end= " ")
#     print()

#========================
"""
*****
****
***
**
*
"""
# n=5
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*", end= " ")
#     print()

#========================
"""
12345
1234
123
12
1
"""
# n=5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j, end= " ")
#     print()

#========================
"""
  *     2 times space before start , 2 times space after star
 ***    1 times space before start , 1 times space after star
*****   0  times space before start , 1 times space after star

n   * freq.
3   1
2   3
1   5

"""

# n=3
# StarCount = 1
# for i in range (n,0,-1):
#         #for printing spaces
#         for j in range (i-1):
#             print(" ", end="")
        
#         #once spaces are printed , another loop to print * now
#         for k in range (0,StarCount):
#             print("*",end="")
#         StarCount +=2

#         #for printing spaces
#         for l in range (i-1):
#             print(" ", end="")
#         print()

#========================
"""
*****   0 space before, 0 space after
 ***    1 space before, 1 space after
  *     2 space before, 2 space after

n  *freq
0   5
1   3
2   1
"""

# n=4
# StarCount = (2*n)-1
# for i in range(n+1):

#     #for spaces
#     for j in range(0,i):
#         print(" ", end="")
    
#     #for printing *
#     for k in range(0,StarCount):
#         print("*",end="")
#     StarCount -=2

#     #for spaces
#     for j in range(0,i):
#         print(" ", end="")
#     print()

#ALTERNATE SOLUTION
# n=4
# for i in range(0,n+1):

#     #printing space
#     for j in range(0,i):
#         print(" ",end="")
    
#     #printing star
#     for k in range(0,((2*n) - (2*i-1))):  #formula to relate stars with "n" and "i" = 2n-(2i-1)
#         print("*",end="")
    
#     #printing space
#     for j in range(0,i):
#         print(" ",end="")
#     print()


     


#========================
"""
  *     2 space both side , 1 star
 ***    1 space both side , 3 star
*****   0 space both side , 5 star
------------
*****   0 space both side , 5 star
 ***    1 space both side , 3 star
  *     2 space both side , 1 star

n=3

"""
#NOT THE BEST SOLUTION
#CONCEPT: SOMEHOW RELATE EQUATION OF FOR LOOP BY "n" and outer loop "i"
# n=5
# for i in range(0,n):
        
#     #print space in same row
#     for j in range(0,n-1-i):
#         print(" ",end="")
    
#     #printing stars in same row
#     for k in range(0,2*i+1):
#         print("*",end="")
    
#     #print space in same row
#     for l in range(0,n-1-i):
#         print(" ",end="")
#     print() #end line before we move to next row

# for p in range(1,n+1): 

#     #print space in same row
#     for q in range(0,p-1):
#         print(" ",end="")
    
#     #printing stars in same row
#     for r in range(0,(2*n - 2*p) + 1):
#         print("*",end="")
    
#     #print space in same row
#     for s in range(0,p-1):
#         print(" ",end="")
#     print()


#BEST SOLUTION

# Initialise 'gap' and 'stars'.
# n=5
# gap = n-1
# stars = 1
# for i in range(n):
#     for j in range(gap):
#         print(' ', end="")
#     for j in range(gap, gap+stars):
#         print('*', end="")

#     # End the current row of the pattern.
#     print()

#     gap -= 1
#     stars += 2

# gap = 0
# stars = 2 * n - 1
# for i in range(n, 2*n):
#     for j in range(gap):
#         print(' ', end="")
#     for j in range(gap, gap+stars):
#         print('*', end="")

#     # End the current row of the pattern.
#     print()

#     gap += 1
#     stars -= 2
#=============

"""
*     1star
**    2star
***   3star
****  4star
-------
***   3star
**    2star
*     1

n=4
"""
#CONCEPT: SOMEHOW RELATE EQUATION OF FOR LOOP BY "n" and outer loop "i"
# n=1
# for i in range(1,n+1):

#     #printing stars
#     for j in range(i):
#         print("*", end="")
#     print()


# for p in range(0,n-1):

#     #printing stars
#     for q in range(0,(n-1)-p):
#         print("*",end="")
#     print()

#============================
"""
1         1st row
0 1       2nd row , starts with 0
1 0 1     3rd row
0 1 0 1   4th row, starts with 0
1 0 1 0 1 

n=5
"""
# n=4
# for i in range(1,n+1):
#     #even rows starts with 0
#     if i%2 == 0:
#         for j in range(1,i+1):

#             #even columns will have 1
#             if j%2 == 0:
#                 print(1,end=" ")

#             #odd columns will have 0
#             else:
#                 print(0,end=" ")
#         print()

#     #odd row starts with 1
#     else:
#         for j in range(1,i+1):
#             if j%2 == 0:
#                 print(0,end=" ")
#             else:
#                 print(1,end=" ")
#         print()

#================================
"""
1             1  , 12 spaces
1 2         2 1  , 8 spaces
1 2 3     3 2 1  ,4 spaces
1 2 3 4 4 3 2 1  , 0 spaces

breakdown:-
1      , 6 space
1 2    , 4 space
1 2 3  , 2 space
1 2 3 4, 0 space

      1  , 6 space
    2 1  , 4 space
  3 2 1  , 2space
4 3 2 1  , 0  space
n=4
"""
# n=4
# for i in range(1,n+1):

#     #printing number
#     for j in range(1,i+1):
#         print(j, end=" ")
    
#     # #printing spaces
#     for q in range(0, 4*(n -i) ):
#         print(" ",end="")
    
#     # #printing numbers
#     for r in range(i,0,-1):
#         print(r,end=" ")
#     print()

#================================
"""
1
2 3
4 5 6 
7 8 9 10

n=4
"""
# n=4
# count = 0
# for i in range(1,n+1):
#     for j in range(i):
#       count +=1
#       print(count, end= " ")
#     print()

#================================

"""
A
A B
A B C 
A B C D

n= 4
"""
# n=4
# num = 1
# for i in range(n):      #This loop iterates through the rows of the pattern
#     currentCharacter = 65      # This sets the ASCII value of 'A'
#     for j in range(1, num+1):      #This loop iterates through the characters in a row
#         print(chr(currentCharacter), end=" ")   # This line prints the character 
#         currentCharacter += 1 # This moves to the next character in the sequence
#     num += 1     #This moves to the next row, increasing the number of characters to print
#     print()      #This moves to the next line for the next row

#-------------
# print(ord("A"))
# print(chr("A"))
#-------------

# n=5
# for i in range(1,n+1):
#     character = 65
#     for j in range(0,i):
#       print(chr(character), end= " ")
#       character +=1
#     character =65
#     print()

#ALTERNATE METHOD
# str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for i in range(1,n+1):
#     for j in range(0,i):
#       print(str1[j], end= " ")
#     print()

#======================================
"""

Sample Output 2 :
A B C D
A B C
A B
A

n=4
"""

# n=4
# for i in range(n,0,-1):
#     character = 65
#     for j in range(i):
#       print(chr(character), end = " ")
#       character += 1
#     print()

#ALTERNATE CODE
# n=4
# for i in range(n,0,-1):
#     character = 65
#     for j in range(0,i):
#       print(chr(65+j), end = " ")
#     print()


#================================

"""
Input: ‘N’ = 3

Output: 
A
B B
C C C
"""
# n=3
# for i in range(0,n):
#     for j in range(i+1):
#         print(chr(65 +i), end= " ")
#     print()


        
    
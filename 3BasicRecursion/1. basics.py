"""
Way of Approach to recursion problem

Step 1 :- Find out the main task that the function does in one call first
Step 2 :- Then call the same function at the step you think -> Task repeats here after.
Step 3 :- Think if you have to return the function call line or not -> (Imagine: if you are asking the function for the answer then return.)
Step 4 :- Then Write the BASE CASE condition
Step 5 :- Check By doing a Dry Run of Test Cases
"""
#Printing 1 to 3 using recursive function
# def show(count):
#     if count == 4:    #BASE CASE
#         return
#     else:
#         print(count)
#         count +=1
#         show(count)


# count = 1
# show(count)


#==================
#Printing "uditya" n times

# def show(n):
#     if n == 0:         #BASE CASE
#         return
    
#     else:
#         print("Uditya")
#         show(n-1)

# n = int(input("Enter times:- "))
# show(n)

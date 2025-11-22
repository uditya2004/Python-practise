
# TC: O(N)
# SC: O(N)
def carFleet(
        target: int, 
        position: list[int], 
        speed: list[int]
    ) -> int:

    # Combining list position and speed in one list.
    pair = list(zip(position, speed))  # List containing tuples as elements like [(positionOfCar, speedOfCar)]
    
    # Sorting list in decending order by "position"
    pair.sort(reverse= True)                          # Sorts the list pair in descending order based on the first value of each tuple
    
    stack = []

    for p,s in pair:

        # getting the time for the particular car to reach the target
        time_to_reach_target = (target - p)/s

        stack.append(time_to_reach_target)

        #  start.....Car A ......Car B..........Car C....Destination
        # stack[-1] -> time taken by Car B to reach the target
        # stack[-2] -> time taken by Car C to reach the target
        if len(stack) >= 2 and stack[-1] <= stack[-2]:   # if time taken by Car B <= Car C , then Car B will catch Car C in the journey and will become a fleet and move with the speed of Car C for the rest of the journey.
            """
            - # we keep Car C for further car's comparision and removes Car B from the list:
                - as speed of car C didn't changed but speed of car B changed to the speed of C , 
                - so car C is better for comparision, so after removing the Car B , time taken by Car C is now the top
            """
            stack.pop()                                  
    
    return len(stack)   # At the end, no. of cars left in the stack = no. of fleet formed during the journey.


target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(carFleet(target, position, speed))
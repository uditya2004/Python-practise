
# TC: O(N)
# SC: O(N)
def carFleet(
        target: int, 
        position: list[int], 
        speed: list[int]
    ) -> int:

    pair = [(p, s) for p, s in zip(position, speed)]  # List containing tuples as elements like [(positionOfCar, speedOfCar)]
    
    pair.sort(reverse= True)                          # making list in decending order by "position" . Sorts the list pair in descending order based on the first value of each tuple
    
    stack = []

    for p,s in pair:
        time_to_reach_target = (target - p)/s     # getting the time for the particular car to reach the target

        stack.append(time_to_reach_target)

        #  Car A .........Car B..........Car C
        # stack[-1] -> time taken by Car B to reach the target
        # stack[-2] -> time taken by Car C to reach the target
        if len(stack) >= 2 and stack[-1] <= stack[-2]:   # if time taken by Car B <= Car C , then Car B will catch Car C in the journey and will become a fleet and move with the speed of Car C for the rest of the journey.
            stack.pop()                                  # we keep Car C for further car's comparision and removes Car B from the list, so after removing the Car B , time taken by Car C is now the top
    
    return len(stack)   # At the end the no. of cars left in the stack will be equal to the no. of fleet formed during the journey.


target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(carFleet(target, position, speed))
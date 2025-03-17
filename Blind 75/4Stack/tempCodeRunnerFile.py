def dailyTemperatures(temperatures: list[int]) -> list[int]:
    # Every element initialize it with 0
    result = [0] * len(temperatures)

    stack = []       # each element is a tuple : (temp, index)

    for indx, num in enumerate(temperatures):

        while stack and num > stack[-1][0]: 
            
            stackTop, stackTopIndx= stack.pop()

            result[stackTopIndx] = indx - stackTopIndx
        
        else:
            stack.append((num, indx))
    
    return result

temperatures = [30,60,90]
print(dailyTemperatures(temperatures))
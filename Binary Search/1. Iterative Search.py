
def search(lst, target):
    low_index=0
    high_index=len(lst)-1
    mid_index =int(abs((low_index + high_index)/2))

    while low_index>high_index:
        mid_index = int(abs((low_index + high_index)/2))

        if lst[mid_index] == target:
            return mid_index
        
        elif lst[mid_index] > target:
            high_index = mid_index -1
            
        else:
            low_index = mid_index + 1
    
    return None



      
lst=[3,4,6,7,9,12]
target = 5

if search(lst,target) != None:
    print("index of the target element is: ", search(lst,target))

else:
    print("Not found")
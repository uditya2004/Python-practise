"""
- As there can be multiple (value, timestamp) pair associated with same key, we make data-structure like this:-
    dict = {key: [(timestamp, value), (timestamp, value), (timestamp, value),]}

- As we have to find value with timestamp <= give_timestamp and timestamp is inserted in increasing order, hence we are doing searching in sorted array, so apply binary search.
"""

class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if the key not in "dict", it creates => dict = {key : []}
        if key not in self.dict:
            self.dict[key] = []

        # we append the (timestamp, value) pair in the list associated with the pair
        self.dict[key].append((timestamp, value))    # pair can be stored like (timestamp, value) or (value, timestamp) doesn't matter

    def get(self, key: str, timestamp: int) -> str:
        # if key not in dict, return "" as per question
        if key not in self.dict:
            return ""

        # if key present in dict => apply binary search in list associated with key, for getting nearest_timestamp to given_timestamp 
        value = self.dict[key]
        left = 0
        right = len(value) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2

            if value[mid][0] <= timestamp:   # value at mid is a possible answer
                result = value[mid][1]       # update result with new value
                left = mid + 1               # we aim for higher timestamp now, so move towards right portion       
            else:
                right = mid - 1              # if timestamp at mid is larger, we want to minimize it, hence move towards left portion.
        
        return result


obj = TimeMap()
obj.set("foo","bar", 1)  # (key, value, timestamp)
param_2 = obj.get("foo", 1)


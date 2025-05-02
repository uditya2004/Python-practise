class TimeMap:

    def __init__(self):
        self.store = {}        


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:   # if not already present in the dictionary , we create a key with empty list in which we can append
            self.store[key] = []  
        
        self.store[key].append([value, timestamp])   # append the new value to the list associated with a key


    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        # binary search  value = [[bar, 1], [bar, 4], [bar, 5]]   -> [value, timestamp]
        low = 0
        high = len(values) - 1

        while low <= high:
            mid = (low + high) // 2

            if values[mid][1] <= timestamp:
                res = values[mid][0]    # this value is a candidate 
                low = mid + 1           # try to find a better (larger) candidate to the right, as it's in sorted order

            else:
                high = mid - 1          # if timestamp at mid is larger , we search towards the left for smaller timestamp, as it's in sorted order.
        
        return res


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo", "bar", 1)   # (key, value, timestamp)
param_2 = obj.get("foo", 1)
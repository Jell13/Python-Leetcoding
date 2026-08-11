from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key, value, timestamp):
        self.store[key].append((timestamp, value))
    def get(self, key, timestamp):
        currList = self.store[key]

        low, high = 0, len(currList) - 1
        result = ""
        while low <= high:
            mid = low + (high - low) // 2
            if currList[mid][0] == timestamp:
                return currList[mid][1]
            elif currList[mid][0] < timestamp:
                result = currList[mid][1]
                low = mid + 1
            else:
                high = mid - 1

        return result


timeMap = TimeMap()
timeMap.set("alice", "happy", 1)
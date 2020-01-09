class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.drum = {}
        self.cap = capacity
        self.latest = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # print key,self.drum
        if (key in self.drum):
            val = self.drum[key]
            self.drum.pop(key)
            self.drum[key] = val
            if (key not in self.latest):
                self.latest.append(key)
            else:
                self.latest.remove(key)
                self.latest.append(key)
            return val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # self.latest = key
        # print "PUT",key,self.latest,self.drum
        if (key in self.drum):
            self.drum[key] = value
        else:
            if (len(self.drum.keys()) == self.cap):
                self.drum.pop(self.latest[0])
                self.latest.remove(self.latest[0])
                self.drum[key] = value
            else:
                self.drum[key] = value
        if (key not in self.latest):
            self.latest.append(key)
        else:
            self.latest.remove(key)
            self.latest.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
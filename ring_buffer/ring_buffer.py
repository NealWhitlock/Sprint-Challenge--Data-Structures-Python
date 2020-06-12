class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity  # Size of the buffer
        self.storage = []  # list to store items
        self.counter = 0  # counter set to 0

    def append(self, item):
        loc = (self.counter % self.capacity)  # index location for new item
        if len(self.storage) == self.capacity:  # if the list is full
            self.storage.pop(loc)  # remove item in the index location
            self.storage.insert(loc, item)  # put new item in that spot
        else:
            self.storage.append(item)
        self.counter += 1  # increment counter

    def get(self):
        return self.storage

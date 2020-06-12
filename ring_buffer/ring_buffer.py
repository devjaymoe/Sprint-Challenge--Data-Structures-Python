class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        self.eldest = 0

    def append(self, item):
        if len(self.storage) == self.capacity:
            # overwrite at the eldest index
            # if the eldest is at the end restart the eldest
            if self.eldest == self.capacity:
                self.eldest = 0
            self.storage[self.eldest] = item
            # increment the eldest index
            self.eldest += 1
        # have not reached full storage
        else:
            self.storage.append(item)

    def get(self):
        return self.storage

# buffer = RingBuffer(5)

# for i in range(20):
#     # print(i)
#     buffer.append(i)
#     print(buffer.get())

# print(buffer.get())
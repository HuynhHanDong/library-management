class MyArray:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.data[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.data[index] = value

    def len(self):
        return self.size

    def __str__(self):
        return str(self.data[:self.size])

    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def append(self, value):
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        self.data[self.size] = value
        self.size += 1

    def remove(self, value):
        index = None
        for i in range(self.size):
            if self.data[i] == value:
                index = i
                break
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1
        if self.size < self.capacity // 4:
            self.resize(self.capacity // 2)

    def index(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return i
        raise ValueError("Element not found in array")

    def count(self, value):
        count = 0
        for i in range(self.size):
            if self.data[i] == value:
                count += 1
        return count

    def clear(self):
        self.size = 0
        self.data = [None] * self.capacity

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < self.size:
            value = self.data[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration

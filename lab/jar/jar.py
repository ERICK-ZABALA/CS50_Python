class Jar:
    def __init__(self, capacity=12, size=0):

        if capacity < 0:
            raise ValueError
        elif size > 12:
            raise ValueError

        # Num of cookies
        self.size = size
        # Max num of cookies
        self.capacity = capacity

    def __str__(self):
        result_cookies = ""
        for _ in range(self.size):
            result_cookies = "🍪"
        return result_cookies*self.size

    def deposit(self, n):
        self.capacity = self.capacity - n
        self.size = self.size + n

        if self.capacity < 0:
            raise ValueError
        elif self.size > 12:
            raise ValueError

        return self.capacity

    def withdraw (self, n):
        self.capacity = self.capacity + n
        self.size = self.size - n

        if self.capacity < 1:
            raise ValueError
        elif self.capacity > 12:
            raise ValueError

        return self.capacity

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = size


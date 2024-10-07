# Cookie Jar 🍪

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("capacity must be non-negative.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return int(self.size) * "🍪"

    def deposit(self, n):
        if n < 0:
            raise ValueError("only non-negative numbers allowed.")
        elif (n + self.size) > self.capacity:
            raise ValueError("deposit does not fit into jar.")
        self.size = self.size + n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("only non-negative numbers allowed.")
        elif self.size < n:
            raise ValueError("not enough cookies!")
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("capacity must be non-negative.")
        self._capacity = capacity

    @property
    def size(self):
        return self._size 
    @size.setter
    def size(self, size):
        if self.capacity < size:
            raise ValueError("size over limit set by capacity.")
        self._size = size

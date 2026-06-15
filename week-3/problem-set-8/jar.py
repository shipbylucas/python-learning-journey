class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._deposited = 0
        self._withdrawn = 0

    def __str__(self):
        return (f"{"🍪" * self.size}")

    def deposit(self, n):
        if n + self._deposited - self._withdrawn > self.capacity:
            raise ValueError("Exceed capacity")
        self._deposited += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Don't have that much cookies to withdraw")
        self._withdrawn += n

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._deposited - self._withdrawn

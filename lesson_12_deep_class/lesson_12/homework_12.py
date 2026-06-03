class Safe:
    def __init__(self, password: str):
        self.password = password
        self.items = []
        self.locked = True
        self.max_items = 5

    def __str__(self):
        if self.locked:
            status = "locked"
        else:
            status = "unlocked"
        return f"Safe with {len(self.items)}/{self.max_items} items ({status})"

    def __repr__(self):
        return self.__str__()

    def unlock(self, password: str):
        if password == self.password:
            self.locked = False
        else:
            raise ValueError("Wrong password")

    def lock(self):
        self.locked = True

    def __getitem__(self, index: int):
        if not 0 <= index < len(self.items):
            raise IndexError("Index out of range")
        return self.items[index]

    def __setitem__(self, index: int, value):
        if self.locked:
            raise PermissionError("Safe is locked")

        if index < 0 or index > len(self.items):
            raise IndexError("Invalid index")

        if index == len(self.items):
            if len(self.items) >= self.max_items:
                raise OverflowError(f"Cannot add more than {self.max_items} items")
            self.items.append(value)
        else:
            self.items[index] = value

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items
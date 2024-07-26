class LRUCache:

    def __init__(self, capacity: int):
        # Capacity of the cache
        self.capacity = capacity
        # Size or total number of entries in the cache
        self.size = 0
        # Dictionary to store key and entry nodes
        self.entries = {}
        # Head and tail of the list to store entries
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        # If the cache already contains the key
        if key in self.entries:
            # Get the entry corresponding to the key
            entry = self.entries[key]
            # Delete node from the current position and add it to head
            self.delete_entry(entry)
            self.update_head(entry)
            return entry.value
        return -1

    def put(self, key: int, value: int) -> None:
        # If the key is already in the cache
        if key in self.entries:
            # Update the value corresponding to the node
            entry = self.entries[key]
            entry.value = value
            # Delete node from its current position and update head
            self.delete_entry(entry)
            self.update_head(entry)
        else:
            # Create new entry
            entry = self.Entry(key, value)
            if self.size >= self.capacity:
                self.entries.pop(self.tail.key)
                self.delete_entry(self.tail)
            self.update_head(entry)
            self.entries[key] = entry
            self.size += 1

    def delete_entry(self, entry):
        # If given entry is not the head
        if entry.previous is not None:
            entry.previous.next = entry.next
        else:
            self.head = entry.next
        # If given entry is not the tail
        if entry.next is not None:
            entry.next.previous = entry.previous
        else:
            self.tail = entry.previous

    def update_head(self, entry):
        # Make entry as the new node
        entry.next = self.head
        entry.previous = None
        if self.head is not None:
            self.head.previous = entry
        # Update the head
        self.head = entry
        # If there is only one node
        if self.tail is None:
            self.tail = entry

    class Entry:
        def __init__(self, key: int, value: int):
            self.key = key
            self.value = value
            self.previous = None
            self.next = None

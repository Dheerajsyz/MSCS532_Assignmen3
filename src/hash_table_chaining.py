"""
Hash Table with Chaining Implementation
MSCS532 Assignment 3 - Dheeraj Kumar
"""


class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.num_elements = 0
        self.collisions = 0
    
    def _hash(self, key):
        if isinstance(key, str):
            hash_value = 0
            for char in key:
                hash_value += ord(char)
            return hash_value % self.size
        else:
            return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        
        if self.table[index] is None:
            self.table[index] = HashNode(key, value)
            self.num_elements += 1
            return
        
        current = self.table[index]
        while current:
            if current.key == key:
                current.value = value
                return
            if current.next is None:
                break
            current = current.next
        
        current.next = HashNode(key, value)
        self.num_elements += 1
        self.collisions += 1
    
    def search(self, key):
        index = self._hash(key)
        current = self.table[index]
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
        
        return None
    
    def delete(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None
        
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                self.num_elements -= 1
                return True
            prev = current
            current = current.next
        
        return False
    
    def get_load_factor(self):
        return self.num_elements / self.size
    
    def get_chain_lengths(self):
        lengths = []
        for head in self.table:
            length = 0
            current = head
            while current:
                length += 1
                current = current.next
            lengths.append(length)
        return lengths
    
    def display(self):
        print(f"Hash Table (Size: {self.size})")
        print(f"Elements: {self.num_elements}")
        print(f"Load Factor: {self.get_load_factor():.2f}")
        print(f"Collisions: {self.collisions}")
        print("-" * 30)
        
        for i in range(self.size):
            print(f"Bucket {i}: ", end="")
            current = self.table[i]
            if current is None:
                print("Empty")
            else:
                while current:
                    print(f"({current.key}: {current.value})", end="")
                    if current.next:
                        print(" -> ", end="")
                    current = current.next
                print()


def test_hash_table():
    print("Testing Hash Table with Chaining")
    print("=" * 40)
    
    ht = HashTable(7)
    
    test_data = [
        ("apple", 1), ("banana", 2), ("cherry", 3),
        ("date", 4), ("elderberry", 5), ("fig", 6), ("grape", 7)
    ]
    
    print("Inserting test data...")
    for key, value in test_data:
        ht.insert(key, value)
        print(f"Inserted {key}: {value}")
    
    print("\nHash table after insertions:")
    ht.display()
    
    print("\nTesting search operations:")
    for key, expected_value in test_data[:3]:
        found_value = ht.search(key)
        print(f"Search '{key}': {found_value}")
    
    result = ht.search("orange")
    print(f"Search 'orange': {result}")
    
    print("\nTesting delete operations:")
    deleted = ht.delete("banana")
    print(f"Delete 'banana': {deleted}")
    
    print("\nHash table after deletions:")
    ht.display()
    
    print("\nPerformance Analysis:")
    chain_lengths = ht.get_chain_lengths()
    print(f"Chain lengths: {chain_lengths}")
    print(f"Max chain length: {max(chain_lengths)}")
    non_empty = [x for x in chain_lengths if x > 0]
    if non_empty:
        print(f"Average chain length: {sum(non_empty)/len(non_empty):.2f}")


if __name__ == "__main__":
    test_hash_table()

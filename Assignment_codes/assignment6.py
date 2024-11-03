import random

# Universal Hash Function Class
class UniversalHash:
    def __init__(self, table_size, prime=101):
        self.table_size = table_size
        self.prime = prime
        self.a = random.randint(1, prime - 1)  # 1 ≤ a < p
        self.b = random.randint(0, prime - 1)  # 0 ≤ b < p

    def hash(self, key):
        key_value = sum([ord(char) for char in key])
        return ((self.a * key_value + self.b) % self.prime) % self.table_size

# Hash Table with Chaining Class
class ChainedHashTable:
    def __init__(self, table_size):

        self.table_size = table_size
        self.hash_function = UniversalHash(table_size)
        self.table = [[] for _ in range(table_size)]  # Initialize empty chains

    def set(self, key, value):
    
        index = self.hash_function.hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:  
                self.table[index][i] = (key, value)
                return
       
        self.table[index].append((key, value))

    def get(self, key):
      
        index = self.hash_function.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Key not found

    def display(self):
        for i, chain in enumerate(self.table):
            print(f"Index {i}: {chain}")

# Testing the ChainedHashTable with a sample list of people and email addresses
def test_hash_table():
    
    people = [
        ("Alice", "alice@example.com"),
        ("Bob", "bob@example.com"),
        ("Charlie", "charlie@example.com"),
        ("David", "david@example.com"),
        ("Eve", "eve@example.com"),
        ("Frank", "frank@example.com"),
        ("Grace", "grace@example.com"),
        ("Heidi", "heidi@example.com"),
        ("Ivan", "ivan@example.com"),
        ("Judy", "judy@example.com")
    ]

    hash_table = ChainedHashTable(table_size=10)
   
    for name, email in people:
        hash_table.set(name, email)

    print("Hash Table Contents:")
    hash_table.display()

    print("\nRetrieving Existing Keys:")
    for name, _ in people:
        print(f"{name}: {hash_table.get(name)}")

    print("\nRetrieving Non-Existing Key:")
    print(f"Non-existent person: {hash_table.get('NonExistent')}")

if __name__ == "__main__":
    test_hash_table()

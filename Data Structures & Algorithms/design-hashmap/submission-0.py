class ListNode:
    # FIX 1: Added missing trailing underscores
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for i in range(1000)]

    def hash(self, key):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)]
        
        # FIX 2: Loop through the list to see if the key already exists
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value  # Update existing key
                return
            cur = cur.next
        
        # If we reach the end and didn't find it, append the new node
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        # FIX 3: Start looking from cur.next (skipping the dummy head)
        cur = self.map[self.hash(key)].next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        
        # This logic was already correct! It leverages the dummy node perfectly.
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """

class MyHashSet:

    def __init__(self,capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        self.head = None
        """
        :type capacity: int
        :rtype: None
        """

    def add(self, key):
        """
        :type key: str
        :rtype: None
        """
        code = int(MD5.new(key.encode("utf-8")).hexdigest(),16) 
        rest = code % self.capacity
        if not self.contains(key):
            x= ListNode(key)
            x.next = self.head
            self.head = x

    def remove(self, key):
        """
        :type key: str
        :rtype: None
        """
        code = int(MD5.new(key.encode("utf-8")).hexdigest(),16) 
        rest = code % self.capacity
        x = self.head

        if x and x.val == key:
            self.head = x.next
            return None

        while x and x.next:
            if x.next.val == key:
                x.next = x.next.next
                break

    def contains(self, key):
        """
        :type key: str
        :rtype: bool(True or False)
        """
        code = int(MD5.new(key.encode("utf-8")).hexdigest(),16) 
        rest = code % self.capacity
        x = self.head
        while x:
            if x.val == key:
                return True
            x = x.next
        return False

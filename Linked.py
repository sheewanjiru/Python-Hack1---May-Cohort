class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self):
        if self.head is None:
            return None  # Return None if the list is empty

        max_value = self.head.data
        current = self.head.next

        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next

        return max_value


ll = LinkedList()
ll.append(5)  
ll.append(3)  
ll.append(7)  
ll.append(1)  

print(ll.find_max())  

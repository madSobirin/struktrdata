class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_after(self, pos, data):
        if self.head is None:
            print("List kosong")
            return
        
        current = self.head
        while current is not None:
            if current.data == pos:
                break
            current = current.next
        
        if current is None:
            print(f"Data {pos} tidak ditemukan")
        else:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
    
    def delete(self, data):
        if self.head is None:
            print("List kosong")
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                break
            current = current.next
        
        if current.next is None:
            print(f"Data {data} tidak ditemukan")
        else:
            current.next = current.next.next
    
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

sll = SingleLinkedList()
sll.insert_at_beginning(10)
sll.insert_at_beginning(20)
sll.insert_after(20, 15)
sll.insert_after(10, 5)
sll.display()  
# Output: 20 -> 15 -> 10 -> 5 -> None

sll.delete(15)
sll.delete(5)
sll.display() 
# Output: 20 -> 10 -> None
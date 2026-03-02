class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def pop(self):
        if self.head is None:
            return None
        
        temp = self.head
        pre = self.head

        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self,value):
        temp = self.head
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = temp
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        
        return temp
    
    def get(self,index):
        if index > self.length-1 or index < 0:
            raise IndexError('out of index')
        temp = self.head
        current_index = 0
        while current_index != index:
            temp = temp.next
            current_index += 1
        
        return temp
    
    def set_value(self,index,value):
        node = self.get(index)
        node.value = value

        return node
    
    def insert(self,index,value):
        if index > self.length-1 or index < 0:
            raise IndexError('out of index')
        new_node = Node(value=value)
        if index == 0:
            return self.prepend(value)
        # if index == self.length:
        #     return self.append(value)

        pre = self.get(index-1)
        post = self.get(index)
        pre.next = new_node
        new_node.next = post
        self.length += 1

        return new_node
    
    def remove(self,index):
        if index > self.length-1 or index < 0:
            raise IndexError('out of index')
        
        if index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        
        temp = self.get(index)
        pre = self.get(index-1)

        pre.next = temp.next
        temp.next = None
        self.length -=1
        return temp
    
    def reverse(self):
    
        for _ in range(self.length):
            pre_tail = self.get(self.length-2)
            temp_head = self.head
            self.head = self.tail
            self.head.next = temp_head
            self.tail = pre_tail

        return True
    
linked_list = LinkedList(4)
linked_list.append(5)
linked_list.append(10)
linked_list.append(5)
linked_list.print_list()
print("After prepending and popping:")
linked_list.prepend(5)
linked_list.pop()
linked_list.pop_first()
linked_list.prepend(15)
linked_list.print_list()
print("getting value by index:")
print(linked_list.get(1).value)
print("setting value by index")
linked_list.set_value(1,14)
linked_list.print_list()


linked_list.print_list()
print("After inserting value by index:")
linked_list.insert(3, 4)
linked_list.set_value(1, 52)
linked_list.remove(1)
linked_list.print_list()


linked_list.reverse()
linked_list.print_list()
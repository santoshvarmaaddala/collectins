class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self) -> None:
        self.head: ListNode = None

    def append(self, val) -> None:
        if not self.head:
            self.head = ListNode(val)
            return 
     
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ListNode(val)

    def __str__(self):
        values = []
        temp = self.head
        while temp:
            values.append(str(temp.val))
            temp = temp.next
        return " -> ".join(values)

    def __len__(self) -> int:
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def __getitem__(self, val) -> ListNode:
        temp = self.head
        count = 0
        while temp:
            if count == val:
                return temp.val
            count += 1
            temp = temp.next
        raise IndexError("Index out of bound")
    
    def values(self):
        temp = self.head
        while temp:
            yield temp.val
            temp = temp.next

    def nodes(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next

    def __iter__(self):
        temp = self.head
        index = 0
        while temp:
            yield index, temp.val
            temp = temp.next
            index += 1

    def insert(self, index: int, value):
        new_node = ListNode(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        count = 0

        while temp:
            if count == index - 1:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
            count += 1

        raise IndexError("Index out of bound")

    def pop(self, index: int = -1):
        if self.head is None:
            raise IndexError("Pop from empty list")

        # If default -1 (last element), calculate length
        if index == -1:
            index = len(self) - 1

        if index == 0:
            popped = self.head
            self.head = self.head.next
            return popped.val

        temp = self.head
        count = 0
        while temp and temp.next:
            if count == index - 1:
                popped = temp.next
                temp.next = temp.next.next
                return popped.val
            temp = temp.next
            count += 1

        raise IndexError("Index out of bound")

    def __contains__(self, value):
        temp = self.head
        while temp:
            if temp.val == value:
                return True
            temp = temp.next
        return False

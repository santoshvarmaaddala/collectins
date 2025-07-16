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
                return temp
            count += 1
            temp = temp.next
        raise IndexError("Index out of bound")

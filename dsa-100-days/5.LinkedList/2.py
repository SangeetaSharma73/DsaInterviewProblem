Here's an example of how to reverse a linked list in Python:

```
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

Create a linked list
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)

Print the original list
print("Original List:")
llist.print_list()

Reverse the list
llist.reverse()

Print the reversed list
print("Reversed List:")
llist.print_list()

```

Output:

```
Original List:
1 2 3 4 5 
Reversed List:
5 4 3 2 1 
```

This implementation uses a simple iterative approach to reverse the linked list. Here's a step-by-step explanation:

1. Initialize three pointers: `prev`, `current`, and `next_node`.
2. Set `prev` to `None` and `current` to the head of the list.
3. Traverse the list until `current` becomes `None`.
4. In each iteration, do the following:
    - Store the next node in `next_node`.
    - Reverse the `next` pointer of the current node by setting `current.next` to `prev`.
    - Move `prev` and `current` one step forward.
5. After the loop, update the head of the list to point to the new first node, which is `prev`.

This implementation has a time complexity of O(n), where n is the number of nodes in the list, and a space complexity of O(1) since we only use a constant amount of space to store the pointers.

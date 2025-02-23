Problem Statement

Given two sorted linked lists, merge them into a single sorted linked list.

Example

Input:

List1: 1 -> 3 -> 5
List2: 2 -> 4 -> 6

Output:

Merged List: 1 -> 2 -> 3 -> 4 -> 5 -> 6

Solution

Here's a solution in Python:

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

def merge_sorted_lists(list1, list2):
    merged_list = LinkedList()
    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data < current2.data:
            merged_list.append(current1.data)
            current1 = current1.next
        else:
            merged_list.append(current2.data)
            current2 = current2.next

    while current1:
        merged_list.append(current1.data)
        current1 = current1.next

    while current2:
        merged_list.append(current2.data)
        current2 = current2.next

    return merged_list

Create two sorted linked lists
list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

Print the original lists
print("List 1:")
list1.print_list()
print("List 2:")
list2.print_list()

Merge the lists
merged_list = merge_sorted_lists(list1, list2)

Print the merged list
print("Merged List:")
merged_list.print_list()
```

Output:

```
List 1:
1 3 5 
List 2:
2 4 6 
Merged List:
1 2 3 4 5 6 
```

This solution iterates through both lists simultaneously, appending the smaller element to the merged list. Once one list is exhausted, it appends the remaining elements from the other list. The time complexity is O(n + m), where n and m are the lengths of the two lists.

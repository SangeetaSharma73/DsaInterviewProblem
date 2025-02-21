# 🚀 Day 52 of the 100 Days DSA Challenge 🎯
# Problem: Remove Duplicates from an Unsorted Linked List
# Problem Statement:
# Given an unsorted linked list, remove all the duplicate nodes such that each element appears only once.

# Example 1:
# Input:



# Linked List: 1 → 2 → 3 → 2 → 4 → 3 → 5
# Output:



# 1 → 2 → 3 → 4 → 5
# Explanation:
# The duplicates (2, 3) are removed, leaving only unique elements.
# Example 2:
# Input:



# Linked List: 10 → 20 → 20 → 30 → 40 → 40
# Output:



# 10 → 20 → 30 → 40
# Explanation:
# The duplicates (20, 40) are removed.
# Approaches:
# 1️⃣ Brute Force Approach (Nested Loops)
# Steps:
# Use two nested loops.
# For each node, traverse the rest of the list and remove duplicate occurrences.
# Time Complexity: O(N^2)
# Space Complexity: O(1)



# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def removeDuplicates(head):
#     current = head
#     while current:
#         runner = current
#         while runner.next:
#             if runner.next.val == current.val:
#                 runner.next = runner.next.next
#             else:
#                 runner = runner.next
#         current = current.next
#     return head

# # Helper function to print Linked List
# def printList(head):
#     while head:
#         print(head.val, end=" → ")
#         head = head.next
#     print("None")

# # Example Usage
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(4, ListNode(3, ListNode(5)))))))
# printList(removeDuplicates(head))  # Output: 1 → 2 → 3 → 4 → 5 → None
# 2️⃣ Better Approach (Using HashSet)
# Steps:
# Use a set to store unique values.
# Traverse the list and remove duplicates in a single pass.
# Time Complexity: O(N)
# Space Complexity: O(N)



# def removeDuplicates(head):
#     if not head:
#         return None
    
#     seen = set()
#     current = head
#     seen.add(current.val)
    
#     while current.next:
#         if current.next.val in seen:
#             current.next = current.next.next
#         else:
#             seen.add(current.next.val)
#             current = current.next
#     return head
# 3️⃣ Optimal Approach (Using Sorting + Two Pointers)
# Steps:
# Sort the linked list.
# Use two pointers to remove duplicates in O(N).
# Time Complexity: O(N log N) + O(N) ≈ O(N log N)
# Space Complexity: O(1)



# def removeDuplicates(head):
#     if not head or not head.next:
#         return head
    
#     # Step 1: Sort the linked list (convert to array, sort, then re-create the linked list)
#     nodes = []
#     current = head
#     while current:
#         nodes.append(current.val)
#         current = current.next
    
#     nodes.sort()
    
#     # Step 2: Create a new linked list from the sorted values
#     new_head = ListNode(nodes[0])
#     current = new_head
#     for i in range(1, len(nodes)):
#         if nodes[i] != nodes[i - 1]:  # Avoid duplicates
#             current.next = ListNode(nodes[i])
#             current = current.next
    
#     return new_head

# 📌 #DSAChallenge #100DaysOfDSA #DailyLearning #LinkedList #HashSet #TwoPointers # 🚀
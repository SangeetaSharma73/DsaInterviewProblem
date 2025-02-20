# 🚀 Day 50 of the 100 Days DSA Challenge 🎯
# Problem: Reverse a Queue 🏗️
# Problem Statement:
# Given a queue, reverse it using recursion or stack.

# Example 1:
# Input:



# Queue: [1, 2, 3, 4, 5]
# Output:



# Reversed Queue: [5, 4, 3, 2, 1]
# Example 2:
# Input:



# Queue: [10, 20, 30]
# Output:



# Reversed Queue: [30, 20, 10]
# Approaches:
# 1️⃣ Brute Force Approach (Using Extra List)
# Steps:
# Dequeue all elements from the queue and store them in a list.
# Reverse the list.
# Enqueue the elements back into the queue.
# Time Complexity: O(N)
# Space Complexity: O(N)



# from collections import deque

# def reverseQueue(queue):
#     temp = []
    
#     while queue:
#         temp.append(queue.popleft())  # Dequeue elements
    
#     while temp:
#         queue.append(temp.pop())  # Enqueue elements back in reverse order

# # Example Usage
# q = deque([1, 2, 3, 4, 5])
# reverseQueue(q)
# print(list(q))  # Output: [5, 4, 3, 2, 1]
# 2️⃣ Better Approach (Using Stack)
# Steps:
# Push all elements from the queue into a stack.
# Pop elements from the stack and enqueue them back into the queue.
# Time Complexity: O(N)
# Space Complexity: O(N)



# from collections import deque

# def reverseQueue(queue):
#     stack = []

#     while queue:
#         stack.append(queue.popleft())  # Push all elements to stack

#     while stack:
#         queue.append(stack.pop())  # Pop from stack and enqueue

# # Example Usage
# q = deque([1, 2, 3, 4, 5])
# reverseQueue(q)
# print(list(q))  # Output: [5, 4, 3, 2, 1]
# 3️⃣ Optimal Approach (Using Recursion)
# Steps:
# Remove (dequeue) the front element of the queue.
# Recursively call the function for the remaining queue.
# Append the removed element at the rear after recursion returns.
# Time Complexity: O(N)
# Space Complexity: O(N) (Recursive Stack)



# from collections import deque

# def reverseQueueRecursively(queue):
#     if not queue:
#         return
    
#     front = queue.popleft()  # Remove front element
#     reverseQueueRecursively(queue)  # Recursively reverse the rest
#     queue.append(front)  # Add the removed element at the rear

# # Example Usage
# q = deque([1, 2, 3, 4, 5])
# reverseQueueRecursively(q)
# print(list(q))  # Output: [5, 4, 3, 2, 1]

# 📌 #DSAChallenge #100DaysOfDSA #DailyLearning #Queue #Recursion #DataStructures # 🚀








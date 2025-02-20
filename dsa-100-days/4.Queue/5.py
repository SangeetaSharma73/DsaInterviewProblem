# 🚀 Day 51 of the 100 Days DSA Challenge 🎯
# Problem: First Non-Repeating Character in a Stream
# Problem Statement:
# You are given a stream of lowercase characters. Your task is to find the first non-repeating character at each point in the stream.

# Example 1:
# Input:
# plaintext
# 
# Edit
# Stream: "aabc"
# Output:
# plaintext
# 
# Edit
# ['a', 'a', 'b', 'b']
# Explanation:
# 'a' appears → First non-repeating: 'a'
# 'a' appears again → First non-repeating: 'a'
# 'b' appears → First non-repeating: 'b'
# 'c' appears → First non-repeating: 'b'
# Example 2:
# Input:
# plaintext
# 
# Edit
# Stream: "aac"
# Output:
# plaintext
# 
# Edit
# ['a', 'a', 'c']
# Explanation:
# 'a' appears → First non-repeating: 'a'
# 'a' appears again → First non-repeating: 'a'
# 'c' appears → First non-repeating: 'c'
# Approaches:
# 1️⃣ Brute Force Approach (Nested Loops)
# Steps:
# For each character in the stream, check all previous characters.
# Find the first character that has appeared only once.
# Time Complexity: O(N^2)
# Space Complexity: O(1)
# python
# 
# Edit
# def firstNonRepeating(stream):
#     result = []
    
#     for i in range(len(stream)):
#         found = False
#         for j in range(i + 1):
#             if stream[:j + 1].count(stream[j]) == 1:
#                 result.append(stream[j])
#                 found = True
#                 break
#         if not found:
#             result.append('#')
    
#     return result

# # Example Usage
# stream = "aabc"
# print(firstNonRepeating(stream))  # Output: ['a', 'a', 'b', 'b']
# 2️⃣ Better Approach (Using HashMap)
# Steps:
# Use a hashmap to store the frequency of characters.
# Use a list to maintain the order of non-repeating characters.
# For each character, update the hashmap and check the first non-repeating character.
# Time Complexity: O(N)
# Space Complexity: O(N)
# python
# 
# Edit
# from collections import OrderedDict

# def firstNonRepeating(stream):
#     freq = {}
#     order = []
#     result = []
    
#     for char in stream:
#         freq[char] = freq.get(char, 0) + 1
#         if freq[char] == 1:
#             order.append(char)
        
#         while order and freq[order[0]] > 1:
#             order.pop(0)
        
#         result.append(order[0] if order else '#')
    
#     return result

# # Example Usage
# stream = "aabc"
# print(firstNonRepeating(stream))  # Output: ['a', 'a', 'b', 'b']
# 3️⃣ Optimal Approach (Using Queue)
# Steps:
# Maintain a queue for non-repeating characters.
# Use a dictionary to store character frequencies.
# For each character, update its frequency and manage the queue.
# The first element in the queue is the first non-repeating character.
# Time Complexity: O(N)
# Space Complexity: O(N)
# python
# 
# Edit
# from collections import deque

# def firstNonRepeating(stream):
#     queue = deque()
#     freq = {}
#     result = []
    
#     for char in stream:
#         freq[char] = freq.get(char, 0) + 1
#         queue.append(char)
        
#         while queue and freq[queue[0]] > 1:
#             queue.popleft()
        
#         result.append(queue[0] if queue else '#')
    
#     return result

# # Example Usage
# stream = "aabc"
# print(firstNonRepeating(stream))  # Output: ['a', 'a', 'b', 'b']

# 📌 #DSAChallenge #100DaysOfDSA #DailyLearning #Queue #HashMap #DataStructures #Python 🚀








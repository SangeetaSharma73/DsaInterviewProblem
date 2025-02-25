# 🚀 Day 54 of the 100 Days DSA Challenge 🎯
# 🌸 Problem: Can Place Flowers 🌸
# Problem Statement:
# You have a flowerbed represented as an array containing 0s (empty plots) and 1s (occupied plots). Given a number n, determine if you can plant n flowers without violating the adjacency rule, meaning no two flowers can be planted next to each other.

# Example 1:
# Input:
# plaintext
# Copy
# Edit
# flowerbed = [1, 0, 0, 0, 1], n = 1
# Output:
# plaintext
# Copy
# Edit
# True
# Explanation:
# We can plant one flower at index 2 without violating the rule.
# Example 2:
# Input:
# plaintext
# Copy
# Edit
# flowerbed = [1, 0, 0, 0, 1], n = 2
# Output:
# plaintext
# Copy
# Edit
# False
# Explanation:
# There is only one valid place to plant a flower (index 2), so we cannot plant 2 flowers.
# Approaches:
# 1️⃣ Brute Force Approach (Check Each Position)
# Steps:
# Iterate through the array.
# Check if a flower can be planted at each position.
# If possible, plant the flower (set to 1) and move to the next non-adjacent index.
# Stop once n flowers are planted or return False if not possible.
# Time Complexity: O(N^2)
# Space Complexity: O(1)
# python
# Copy
# Edit
# def canPlaceFlowers(flowerbed, n):
#     length = len(flowerbed)
    
#     for i in range(length):
#         if flowerbed[i] == 0:  
#             # Check left and right positions
#             left = (i == 0 or flowerbed[i - 1] == 0)
#             right = (i == length - 1 or flowerbed[i + 1] == 0)
            
#             if left and right:  
#                 flowerbed[i] = 1  # Plant the flower
#                 n -= 1
#                 if n == 0:
#                     return True
                
#     return n == 0

# # Example Usage
# print(canPlaceFlowers([1, 0, 0, 0, 1], 1))  # Output: True
# print(canPlaceFlowers([1, 0, 0, 0, 1], 2))  # Output: False
# 2️⃣ Better Approach (Early Exit)
# Steps:
# Similar to brute force but exits early if n == 0.
# Avoids unnecessary iterations when all flowers are placed.
# Time Complexity: O(N)
# Space Complexity: O(1)
# python
# Copy
# Edit
# def canPlaceFlowers(flowerbed, n):
#     length = len(flowerbed)
    
#     for i in range(length):
#         if n == 0:  
#             return True  # Early exit if all flowers are placed
        
#         if flowerbed[i] == 0:
#             left = (i == 0 or flowerbed[i - 1] == 0)
#             right = (i == length - 1 or flowerbed[i + 1] == 0)
            
#             if left and right:
#                 flowerbed[i] = 1  # Plant the flower
#                 n -= 1
                
#     return n == 0

# # Example Usage
# print(canPlaceFlowers([1, 0, 0, 0, 1], 1))  # Output: True
# print(canPlaceFlowers([1, 0, 0, 0, 1], 2))  # Output: False
# 3️⃣ Optimal Approach (Single Pass)
# Steps:
# Iterate once and count available spots.
# Maintain a counter instead of modifying the flowerbed.
# If n flowers can be placed, return True immediately.
# Time Complexity: O(N)
# Space Complexity: O(1)
# python
# Copy
# Edit
# def canPlaceFlowers(flowerbed, n):
#     length = len(flowerbed)
#     count = 0

#     for i in range(length):
#         if flowerbed[i] == 0:
#             left = (i == 0 or flowerbed[i - 1] == 0)
#             right = (i == length - 1 or flowerbed[i + 1] == 0)

#             if left and right:
#                 flowerbed[i] = 1
#                 count += 1
#                 if count >= n:
#                     return True
    
#     return count >= n

# # Example Usage
# print(canPlaceFlowers([1, 0, 0, 0, 1], 1))  # Output: True
# print(canPlaceFlowers([1, 0, 0, 0, 1], 2))  # Output: False
# Hashtags for Your Journey:
# # 📌 #DSAChallenge #100DaysOfDSA #DailyLearning #Greedy #Array #Python #CodingInterview 🚀
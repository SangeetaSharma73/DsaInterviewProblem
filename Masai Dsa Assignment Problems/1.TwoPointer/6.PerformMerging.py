# Description
# You are given two sorted arrays each of length N. Your task is to write a program that merges both the arrays such that the final array formed after merging is sorted.
# Reset to default code definition
# Font Size: 18
# 1
# Note: You must not use sort() function in your entire code
# Input
# Input Format:
# First line contains N which is the number of integers present in both th e arrays.
# Second line contains N sorted integers which are elements of first arra y.
# Third line contains N sorted integers which are elements of second arr ay.


# Constraints:
# N < 1000
# Output the array formed after merging elements such that it is sorted
# Sample Input 1
# 4
arr1=[1, 5, 7, 9]
arr2=[2, 4, 6, 8]
# Sample Output 1
# 1 2 4 5 6 7 8 9


i=0
j=0
ans=[]
while i<len(arr1) and j<len(arr2):
    if arr1[i]<arr2[j]:
        ans.append(arr1[i])
        i+=1
    else:
        ans.append(arr2[j])
        j+=1
print(*ans)
#2. Non Vowel Substring 

# s=input()

# i=0
# j=0
# mxLen = 0
# while i<len(s) and j<len(s):
#     while i<len(s) and s[i] in 'aeiou':
#         i+=1
#     j=i
#     while j<len(s) and s[j] not in 'aeiou':
#         j+=1
    
#     if mxLen<j-i:
#         mxLen = j-i
#     i=j
# print(mxLen)
        
# Description
# Given a string str of length, find the length of the largest substring which contains only consonants.
# For example: str="abced", the sub-strings containing only cons onants are: "bc" and "d", largest among them is "bc", so the o utput will be 2, which is the length of largest sub-string containin g only consonant.
# Another example: str="bfgedauty", here "bfg" is the largest su bstring without vowels or containing only consonants, so the outp ut will be 3.
# Note: Input contains only the lowercase English alphabet.
# Input
# Input Format:
# First line of input contains the number N, denoting the length of the str ing.
# Second line of input contains the string.
# Constraints:
# 1<=N<=1000

# Output an integer which is the length of largest substring containing on ly consonant (non-vowels)
# Sample Input 1
# 5
s='abced'

 

# brute force
# tc = O(n^3)
# sc = O(n)
def const(s):
    for i in s:
        if i in "aeiou":
            return False
    return True

maxLen=0
for i in range(len(s)):
    st=""
    for  j in range(i,len(s)):
        st+=s[j]
        if const(st):
            maxLen = max(maxLen,len(st))
# print(maxLen)
            
            
#2 Better Solution
# tc = O(n^2)
# sc = O(n)
s='abced'
s="aetu"
s="bbbbii"
s="abbbba"
s="abbbbb"
s="brxrtqdxmghuczxsoziylaamtcuaceqfjiaftxk"
maxLen=0
for i in range(len(s)):
    st=""
    for  j in range(i,len(s)):
        if s[j]=='a' or s[j]=='e' or s[j]=='i' or s[j]=='o' or s[j]=='u':
            break
        else:
            st+=s[j]
            maxLen = max(maxLen,len(st))
print(maxLen)


# Optimal Approach 

# tc = O(n)
# sc = O(1)

# maxLen = 0
# curLen = 0

# for i in range(len(s)):
#     if s[i] in 'aeiou':
#         curLen =0
#     else:
#         curLen +=1
#         maxLen = max(maxLen,curLen)
        
# print(maxLen)


# i=0
# j=0
# mxLen = 0
# while i<len(s) and j<len(s):
#     while i<len(s) and s[i] in 'aeiou':
#         i+=1
#     j=i
#     while j<len(s) and s[j] not in 'aeiou':
#         j+=1
    
#     if mxLen<j-i:
#         mxLen = j-i
#     i=j
# print(mxLen)
# Spiral Traversal [Rectangular Matrix]

arr =[[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12]]

# ans =[1,5,9,10,11,12,8,4,3,2,6,7]

top = 0
bottom = len(arr)-1
left = 0
right = len(arr)-1
c = 0
while c<len(arr)*len(arr[0]):
    for i in range(top,bottom+1):
        print(arr[i][left],end=" ")
        c+=1
    left+=1
    
    for i in range(left,right+1):
        print(arr[bottom][i],end=" ")
        c+=1
    bottom-=1
    
    if bottom>top:
        for i in range(bottom,top-1,-1):
            print(arr[i][right],end=' ')
            c+=1
        right-=1
    if left<right:
        for i in range(right,left-1,-1):
            print(arr[top][i],end=' ')
            c+=1
        top-=1

import sys
def diagonalSum(mat,n):
    leftSum=0
    rightSum=0
    # print(mat)

    rows=len(mat)
    cols=len(mat[0])
    for i in range(0,rows):
        leftSum+=mat[i][i]
        rightSum+=mat[i][rows-i-1]
        

    # print(leftSum,rightSum)
    return abs(leftSum-rightSum)
        
    
dim = int(input())
print(dim)
mat=[[0]*dim for _ in  range(dim)]
 
for i in range(dim):
    nums=map(int,list(input().split(' ')))
    for idx,num in enumerate(nums):
        mat[i][idx]=num

print (diagonalSum(mat,dim))

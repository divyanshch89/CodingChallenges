#Link - https://leetcode.com/problems/rotate-image/
'''
Approach 1 - This can be solved by transposing the matrix and then reversing each row -  easiest
Approach 2 -  modifying in-place. Think of the 2D matrix as an image and then move elements in place
TC for both the appproaches is O(N^2)
'''
def rotate_image_app2(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        #as the layer increases, the last value will towards left (inner)
        last = n-1-layer
        for i in range(first,last):
            #now we will loop through the all the indexes in the current layer(row)
            #offset will help select the appropriate elem as we through the rows and columns and will also compensate for the layer we are
            #currently in
            offset = i-first
            #top value
            temp = matrix[first][i]

            #left->top
            matrix[first][i] = matrix[last-offset][first]

            #bottom ->left
            matrix[last-offset][first] = matrix[last][last-offset]
            #right->bottom
            matrix[last][last-offset] =matrix[i][last]
            matrix[i][last] = temp

def rotate_image_app1(matrix):
    def transpose(mat):
        row = len(mat)
        for i in range(row):
            for j in range(i+1,row):
                mat[j][i],mat[i][j]=mat[i][j],mat[j][i]
   
        """
        Do not return anything, modify matrix in-place instead.
        This problem can be solved by doing a transpose and then reversing the image
        """
    row = len(matrix)
    col = len(matrix[0])
    transpose(matrix)
        #reverse the rows
    c= 0
    for r in range(row):
        cur_row = matrix[r]
        left,right =0,col-1
        while left < right:
            cur_row[left],cur_row[right] = cur_row[right],cur_row[left]
            left,right=left+1,right-1

test_mat = [[1,2,3],[4,5,6],[7,8,9]]
# rotate_image_app2(test_mat)
rotate_image_app1(test_mat)
print(test_mat)
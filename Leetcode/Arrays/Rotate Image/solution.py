class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """/*
 i) reverse the matrix
 ii)transpose of the matrix
  1 2 3     7 8 9     7 4 1
  4 5 6  => 4 5 6  => 8 5 2
  7 8 9     1 2 3     9 6 3

        
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

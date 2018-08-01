class Solution:
    def rotate(self, matrix):
        length = len(matrix)
        for i in range(length):
            for j in range(i + 1, length):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]


r = Solution()
r.rotate([
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
])

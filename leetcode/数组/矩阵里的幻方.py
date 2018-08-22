class Solution:
    def numMagicSquaresInside(self, grid):
        """
        直接按照河图的规定去做就OK了。用到了一个结论：河图的中心数字是5.

        注意一个易忽略的点，就是所有的数字应该在1~9之间。测试用例里面出现了不在这个范围内的数字也能组成河图。

        另外，关于河图，其实有很多有用的结论，我并没有使用。

        河图记忆方法：偶角奇边坐心五.一线双角相对画.
        :param grid:
        :return:
        """
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        counter = 0
        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) - 2):
                sub_matrix = [[grid[row + i][col + j] for j in range(3)] for i in range(3)]
                if self.magic_square(sub_matrix):
                    counter += 1
        return counter

    def magic_square(self, matrix):
        is_number_right = all(1 <= matrix[i][j] <= 9 for i in range(3) for j in range(3))
        is_row_right = all(sum(row) == 15 for row in matrix)
        is_col_right = all(sum(col) == 15 for col in [[matrix[i][j] for i in range(3)] for j in range(3)])
        is_diagonal_right = matrix[1][1] == 5 and matrix[0][0] + matrix[-1][-1] == 10 and matrix[0][-1] + matrix[-1][
            0] == 10
        return is_number_right and is_row_right and is_col_right and is_diagonal_right

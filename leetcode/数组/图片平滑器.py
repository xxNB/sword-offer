class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(M)
        m = len(M[0])
        temp = [0 for x in range(m)]
        res = [temp[:] for x in range(n)]
        temp.append(0)
        for i in M:
            i.append(0)
        M.append(temp)

        for i in range(n):
            flag1 = False
            flag2 = False
            if i == 0:
                flag1 = True
            if i == n - 1:
                flag2 = True
            for j in range(m):
                div = 9 - flag1 * 3 - flag2 * 3
                if j == 0:
                    div -= 3
                    div += flag1 + flag2
                if j == m - 1:
                    div -= 3
                    div += flag1 + flag2
                sum = (M[i - 1][j - 1] + M[i - 1][j] + M[i - 1][j + 1] + M[i][j - 1] + M[i][j] + M[i][j + 1] + M[i + 1][
                    j - 1] + M[i + 1][j] + M[i + 1][j + 1])
                res[i][j] = sum // div
        return res

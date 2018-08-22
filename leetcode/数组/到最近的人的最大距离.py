class Solution:
    """
    能看出来有三种情况：

左边有连续n个空位，坐最左边，最近的人距离为n
右边有连续n个空位，坐最右边，最近的人距离为n
中间有连续n个空位，n小于等于2，必须挨着人坐，最近距离为0，n为奇数最近距离为
（n+1）/2, n为偶数最近距离为n/2
选出最大的一个就可以
    """
    def maxDistToClosest(self, seats):
        width = 0
        left = 0
        while seats[left] ==0:
            left+=1
        width = max(left,width)
        right = len(seats) -1
        zeros = 0
        while seats[right] ==0:
            right -=1
            zeros+=1
            width = max(zeros, width)

        prev = False
        current = 0
        for index, value in enumerate(seats):
            if value ==0:
                if prev:
                    current+=1
                else:
                    prev=True
                    current=1
            else:
                prev = False
                if current<=2:
                    width = max(width,1)
                elif current%2:
                    width  = max(width, current//2+1)
                else:
                    width=max(width, current//2)
        return width
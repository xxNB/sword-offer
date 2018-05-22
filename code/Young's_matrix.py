
def get_value(l,r,c):
    return l[r][c]

def find(l ,x):
    m = len(l) - 1    # 横列
    n = len(l[0]) - 1 # 纵列
    r = 0
    c= n
    while c>=0 and r<=m:
        value = get_value(l,r,c)
        if value == x:
            return True
        elif value >x:
            c = c - 1 # 自上向下递增，所以要减小和它比较
        elif value < x: 
            r = r+1 # 水平递增，所有要增大和它比较
    return False


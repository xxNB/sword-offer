import time

def cal_time(func): #装饰器
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("running time:",func.__name__, t2 - t1)
        return result
    return wrapper

@cal_time
def bin_search(data_set, val):
    low = 0
    high = len(data_set) -1 
    while low <= high:
        mid = (low+high)//2
        if data_set[mid] == val:
            return mid
        elif data_set[mid] > val:
            high = mid - 1
        else:
            low= mid+1
    return 

# data_set = list(range(10000000))

print(bin_search([1,3,5,6,7,10,13], 5))
def get_close_distance(x,y,w,h):
    r = w - x
    l = x
    u = h - y
    d = y
    arr = [r,l,u,d]
    
    min_ = 1000
    for i in arr:
        if i < min_:
            min_ = i
    return min_

x,y,w,h = map(int, input().split())
print(get_close_distance(x,y,w,h))
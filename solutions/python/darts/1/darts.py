import math
def score(x, y) -> int:
    res = math.sqrt(x**2+y**2)
    if res<=1:
        return 10
    elif res<=5:
        return 5
    elif res<=10:
        return 1
    else:
        return 0

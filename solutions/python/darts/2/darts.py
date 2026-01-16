import math
def score(x, y) -> int:
    # res = math.sqrt(x**2+y**2)
    # if res<=1:
    #     return 10
    # elif res<=5:
    #     return 5
    # elif res<=10:
    #     return 1
    # else:
    #     return 0
    res = (x**2+y**2)**0.5
    return (res<=1)*5+(res<=5)*4+(res<=10)*1

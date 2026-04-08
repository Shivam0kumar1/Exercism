#linear search
# def square_root(number):
#     i=1
#     while number>=i*i:
#         if number == i*i:
#             return i
#         i+=1

#Binary search
def square_root(number):
    left,right=1,number
    
    while left<=right:
        mid = (left+right)//2
        square = mid*mid
        if square == number:
            return mid
        elif square>number:
            right-=1
        else:
            left+=1
        
        
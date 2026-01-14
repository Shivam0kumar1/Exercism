def steps(number):
    if number<1:
        raise ValueError("Only positive integers are allowed")
    else:
        count = 0
        n=number
        while n!=1:
            if n%2==0:
                n//=2
            else:
                n=n*3+1
            count+=1
    return count

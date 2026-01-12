def equilateral(sides):
    a,b,c = sides
    return a+b+c>0 and (a+b>=c and a+c>=b and c+b>=a) and a==b==c
        
            


def isosceles(sides):
    a,b,c = sides
    return a+b+c>0 and (a+b>=c and a+c>=b and c+b>=a) and (a==b or b==c or a==c)


def scalene(sides):
    a,b,c = sides
    return a+b+c>0 and (a+b>=c and a+c>=b and c+b>=a) and a!=b!=c!=a

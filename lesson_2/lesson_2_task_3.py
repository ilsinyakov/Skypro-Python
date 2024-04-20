from math import ceil


def square(side):
    area = side * side
    if type(side) != int:
        return ceil(area)
    else: 
        return area
    
print(square(5.2))

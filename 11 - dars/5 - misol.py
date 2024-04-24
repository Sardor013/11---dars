def kvadratlar(a, b):
    squares = []
    for i in range(a+1, b):
        if (i**0.5).is_integer():
            squares.append(int(i**0.5))
    return squares if squares else None

a = int(input("-->"))
b = int(input("-->"))
print("Natija:", kvadratlar(a, b))  


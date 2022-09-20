def sum_squares(*angka) :
    x = [*angka]
    y = 0
    for z in x:
        y += z**2
    return y

print(sum_squares(1, 2, 3))

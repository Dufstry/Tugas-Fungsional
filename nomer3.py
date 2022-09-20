def square(a, b):
    c = a
    if a < 0 or b < 0:
        return "only accept positive number"
    if b == 0:
        return 1
    rekap = 0
    while rekap < b - 1:
        a = a * c
        rekap += 1
    return a

print(square(3, 2))
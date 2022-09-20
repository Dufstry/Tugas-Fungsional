def triangle(e):
    f = e
    if e < 0:
        return "only accept positive number"
    while e != 0:
        e -= 1
        f+=e
    return f

print(triangle(5))
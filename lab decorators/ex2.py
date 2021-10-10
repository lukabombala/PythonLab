def tetranacci(n):
    if n in {1, 2, 3}:
        return 0
    elif n == 4:
        return 1
    else:
        return tetranacci(n) + tetranacci(n-1) + tetranacci(n-2) + tetranacci(n-3)

print(tetranacci(5))

def get_real_floor(n: int) -> int:
    if n == 0:
        return 0
    elif n < 0:
        return n
    elif n <= 12:
        return n-1
    else:
        return n-2


print(get_real_floor(1))

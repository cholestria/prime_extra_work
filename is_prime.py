def is_prime(num):
    """check if an integer is prime"""
    assert type(num) == int

    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
        elif i ** 2 > num:
            break
    return True

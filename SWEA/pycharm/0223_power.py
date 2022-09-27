def Power(base, exponent):
    if exponent == 0 or base == 0:
        return 1

    if exponent % 2 == 0:
        Newbase = power(base, exponent/2)
        return 
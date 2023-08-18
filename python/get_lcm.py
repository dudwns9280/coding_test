
def get_lcm(a, b):
    return int(a * b / get_gcd(a, b))


def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


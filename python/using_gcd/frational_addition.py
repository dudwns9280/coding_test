
def add_two_fractions(numer1, denom1, numer2, denom2):
    max_numer = numer1 * denom2 + numer2 * denom1
    max_denom = denom1 * denom2
    gcd = get_gcd_from_two_number(max_numer, max_denom)
    return [max_numer/gcd, max_denom/gcd]


def get_gcd_from_two_number(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def get_gcd_from_two_number(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def get_gcd_from_array(array):
    gcd = array[0]
    for item in array:
        gcd = get_gcd_from_two_number(gcd, item)
    return gcd

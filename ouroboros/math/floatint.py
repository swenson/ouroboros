def float2int(f):
    """Convert the float argument to a 64-bit int representing the IEEE 754 bytes"""

    h = f.hex()
    i = 0
    if h[0] == '-':
        h = h[1:]
        i = 0x8000000000000000
    else:
        pass
    h = h[2:]
    mantissa = int(h[2:15], 16)
    exp = int(h[16:])
    return i | ((exp+1023) << 52) | mantissa

#!/usr/bin/python3
"""utf8 validation script"""


def validUTF8(data):
    """validUTF8 function

        args:
            data (str) - utf8 encoding
    """

    n_bytes = 0

    for n in data:
        if n_bytes == 0:
            mask = 1 << 7
            while n & mask:
                n_bytes += 1
                mask >>= 1

            if n_bytes == 1 or n_bytes > 4:
                return False

            if n_bytes > 0:
                n_bytes -= 1

        else:
            if n >> 6 != 2:
                return False

            n_bytes -= 1

    return n_bytes == 0

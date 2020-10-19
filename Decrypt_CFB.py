
def cfb_dec(ys):
    xs = []
    iv = int("0xAA", 16)
    key = int("0x08", 16)
    x0 = chr(((key + 11 * iv) % 256) ^ int(ys[0], 16))
    xs.append(x0)

    for i in range(1, len(ys)):
        xi = chr(int(ys[i], 16) ^ (key + 11 * (int(ys[i - 1], 16))) % 256)
        xs.append(xi)
    return xs


def main():
    cipher_cfb = ['0x26', '0xc5', '0x10', '0xdc', '0x10', '0xdd']
    ps_cfb = cfb_dec(cipher_cfb)
    print("\nCFB decryption ", ps_cfb)


main()

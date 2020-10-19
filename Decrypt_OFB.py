
def ofb_dec(ys):
    iv = int("0xAA", 16)
    key = int("0x08", 16)
    ss = []
    xs = []
    s0 = (key + 11 * iv) % 256
    x0 = chr(s0 ^ int(ys[0], 16))
    ss.append(s0)
    xs.append(x0)
    for i in range(1, len(ys)):
        si = (key + 11 * ss[i - 1]) % 256
        ss.append(si)
        xi = chr(int(ys[i], 16) ^ ss[i])
        xs.append(xi)
    return xs


def main():
    cipher_ofb = ['0x25', '0xd4', '0x69', '0x25', '0x42', '0x29']
    ps_ofb = ofb_dec(cipher_ofb)
    print("\nOFB decryption ", ps_ofb)


main()


def ctr_dec(ys):
    ss = ["10101000", "10101001", "10101010", "10101011", "10101100", "10101101"]
    key = int("0x08", 16)
    xs = []
    for i in range(len(ys)):
        ei = (key + 11 * int(ss[i], 2)) % 256
        xi = chr(int(ys[i], 16) ^ ei)
        xs.append(xi)
    return xs


def main():
    cipher_ctr = ['0x2e', '0x24', '0x39', '0x05', '0x00', '0x12']
    ps_ctr = ctr_dec(cipher_ctr)
    print("\nCTR decryption ", ps_ctr)


main()

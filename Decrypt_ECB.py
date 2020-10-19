def ecb_dec(ys):
    xs = []
    key = int("0x08", 16)
    for i in range(len(ys)):
        xi = chr((163 * (int(ys[i], 16) - key + 256)) % 256)
        xs.append(xi)
    return xs


def main():
    cipher_ecb = ['0xcd', '0xcd', '0x54', '0xac', '0x5f']
    ps_ecb = ecb_dec(cipher_ecb)
    print("\nECB decryption ", ps_ecb)


main()

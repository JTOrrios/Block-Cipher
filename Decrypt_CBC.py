
def cbc_dec(ys):
    xs = []
    iv = int("0xAA", 16)
    key = int("0x08", 16)
    x0 = chr(((163 * (int(ys[0], 16) - key)) % 256) ^ iv)
    xs.append(x0)
    for i in range(1 , len(ys)):
        xi = chr(((163 * (int(ys[i], 16) - key)) % 256) ^ int(ys[i - 1], 16))
        xs.append(xi)
    return xs

def main():
    cipher_cbc = ['0X8a', '0Xdf', '0x98', '0x2c', '0x1d']
    ps_cbc = cbc_dec(cipher_cbc)
    print("\nCBC decryption ", ps_cbc)

main()

def cbc(word):
    list_of_letters = list(word)
    xs = []
    for i in list_of_letters:
        dec = ord(i)
        xs.append(dec)

    iv = int("0xAA", 16)
    key = int("0x08", 16)
    ys = []
    y0 = hex(key + 11 * (xs[0] ^ iv) % 256)
    ys.append(y0)

    for i in range(1, len(xs)):
        yi = hex(key + 11 * (xs[i] ^ int(ys[i-1],16)) % 256)
        ys.append(yi)
    return xs, ys


def main():
    word_cbc = "long"
    xs_cbc, ys_cbc = cbc(word_cbc)

    print("\nCBC plaintext", xs_cbc)
    print("CBC Mode ciphertext in hex =", ys_cbc)


main()

def cfb(word):
    list_of_letters = list(word)
    xs = []
    for i in list_of_letters:
        dec = ord(i)
        xs.append(dec)

    iv = int("0XAA", 16)
    key = int("0x08", 16)
    ys = []
    y0 = hex(xs[0] ^ ((key + 11 * iv) % 256))
    ys.append(y0)

    for i in range(1, len(xs)):
        yi = hex(xs[i] ^ (key + 11 * int(ys[i-1], 16)) % 256)
        ys.append(yi)
    return xs, ys


def main():
    word_cfb = "dangling"
    xs_cfb, ys_cfb = cfb(word_cfb)

    print("\nCFB plaintext", xs_cfb)
    print("CFB Mode ciphertext in hex =", ys_cfb)


main()
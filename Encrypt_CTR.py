
def ctr(word):
    list_of_letters = list(word)
    xs=[]
    for i in list_of_letters:
        dec=ord(i)
        xs.append(dec)

    ss = ["10101000", "10101001", "10101010", "10101011", "10101100", "10101101", "10101110" , "10101111"]
    key = int("0x08",16)
    ys = []
    for  i in range(len(xs)):
        ei = (key + 11 * int(ss[i],2)) % 256
        yi = hex(xs[i] ^ ei)
        ys.append(yi)
    return xs, ys

def main():
    word_ctr = "brownish"
    xs_ctr, ys_ctr = ctr(word_ctr)

    print("CTR plaintext", xs_ctr)
    print("CTR mode ciphrtext in hex =", ys_ctr)

main()
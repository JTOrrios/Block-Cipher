
def ecb(word):

	list_of_letters = list(word)
	xs = []
	for i in list_of_letters:
		dec = ord(i)
		xs.append(dec)

	key = int("0x08", 16)
	ys = []
	for xi in xs:
		yi = hex((key + 11 * xi) % 256)
		ys.append(yi)
	return xs, ys

def main():
	word_ecb = "bangs"
	xs_ecb, ys_ecb = ecb(word_ecb)

	print("\nECB plaintext", xs_ecb)
	print("ECB Mode ciphertext in hex =", ys_ecb)

main()
	

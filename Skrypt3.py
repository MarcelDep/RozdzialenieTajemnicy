"""Zdanie które będziemy szyfrować to - Moje pieniadze ukrylem pod drzewem - """
def function():
    cienie = []
    orginalne_zdanie = "Moje pieniadze ukrylem pod drzewem"
    print("Tajemnica przed zmianami: ", orginalne_zdanie)
    orginalne_zdanie = orginalne_zdanie.lower()
    zdanie_do_szyfrowania = orginalne_zdanie.replace(" ", "")
    binarne_zdanie = ' '.join(format(ord(literka), '08b') for literka in zdanie_do_szyfrowania)
    binarne_zdanie = binarne_zdanie.replace(" ", "")
    dziesietne_zdanie = int(binarne_zdanie, 2)
    M = dziesietne_zdanie
    a = 4852917589175891589165897836543785743985634857034578093423532390724
    b = 1242153124237123091282137896283127094820821938081238962932132326483
    p = 755294110712770756997189869755926863861836295184179865351777273763030389
    for x in range(1, 6):
        x = ((a * x ** 2 + b * x + M) % p)
        cienie.append(x)
    print(f"Prawdziwe wartości: a = {a}, b = {b}, M = {M}")
    return cienie

def reconstruction():
    cienie = function()
    print(cienie)
    print("Wybierz różne cienie od 1 do 5 od najmniejszego do największego.")
    i = int(input("Wybierz cień nr. 1: "))
    j = int(input("Wybierz cień nr. 2: "))
    k = int(input("Wybierz cień nr. 3: "))

    if k <= j or j <= i:
        exit("Błąd")

    if k == i or k == j or j == i:
        exit("Błąd")

    cien1 = cienie[i-1]
    cien2 = cienie[j-1]
    cien3 = cienie[k-1]

    p = 755294110712770756997189869755926863861836295184179865351777273763030389
    print(f"Wybrane cienie: {cien1}, {cien2}, {cien3}")

    # Rozwiązywanie równania
    a1 = ((j ** 2 - i ** 2) % p)
    b1 = ((j - i) % p)
    c1 = ((cien2 - cien1) % p)
    a2 = ((k ** 2 - j ** 2) % p)
    b2 = ((k - j) % p)
    c2 = ((cien3 - cien2) % p)

    det = (a1 * b2 - a2 * b1) % p
    dev_inv = pow(det, -1, p)

    a = ((c1 * b2 - c2 * b1) * dev_inv) % p
    b = ((a1 * c2 - a2 * c1) * dev_inv) % p

    M = (cien1 - a - b) % p

    print(f"Rozwiązanie: a = {a}, b = {b}, M = {M}")
    # Zamiana z postaci dziesiętnej na tekst
    binarne_M = bin(M)[2:]
    binarne_M = binarne_M.zfill(len(binarne_M) + (8 - len(binarne_M) % 8) % 8)
    po_8_bitow = [binarne_M[i:i + 8] for i in range(0, len(binarne_M), 8)]

    zdanie_orginalne = ''.join(chr(int(grupa, 2)) for grupa in po_8_bitow)
    print("Rekonstuowana tajemnica: ", zdanie_orginalne)

reconstruction()
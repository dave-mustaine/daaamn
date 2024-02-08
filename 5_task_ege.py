R = 0
numberr = 0

while R < 76:
    numberr += 1

    n_bits = str(bin(numberr))[2::]

    if not (numberr % 3):
        n_bits = n_bits + n_bits[-3:]
    else:
        a = (numberr % 3) * 3
        n_bits = n_bits + str(bin(a))[2::]

    R = int(n_bits, 2)

print(numberr - 1)

# akses list
nilaiA = [5, 3, 1, 9, 7]
print(nilaiA[2])
print(nilaiA[1:3])
print(nilaiA[4:])

# mengubah elemen list
nilaiA[3] = 0
print(nilaiA)
nilaiA[3:5] = [8, 2]
print(nilaiA)

# menambahkan elemen list
nilaiB = nilaiA[0 : 2]
print(nilaiB)
nilaiB.append("10")
print(nilaiB)
nilaiB.append(3)
print(nilaiB)
nilaiC = nilaiA + nilaiB
print(nilaiC)

mahasiswa = []
no = 1

while True:
    nama = str(input("Masukan Nama : ".format(no)))
    Nim = int(input("Masuk Nim    : ").format(no))
    nilai = [0, 0, 0]
    nilai_tugas = int(input("Masukan Nilai Tugas : "))
    nilai_uts = int(input("Masukan Nilai UTS   : "))
    nilai_uas = int(input("Masukan Nilai UAS   : "))

    nilai[0] = nilai_tugas
    nilai[1] = nilai_uts
    nilai[2] = nilai_uas
    akhir = float(nilai_tugas / 3 + nilai_uts / 3.5 + nilai_uas / 3.5)

    tambah = ('| ' + str(no) + ' | ' + str(nama) + ' | ' + str(Nim) + ' |  ' +
              str(nilai_tugas) + '  |  ' + str(nilai_uts) + '  |  ' +
              str(nilai_uas) + '  | ' + "%.2f" % (akhir) + ' |'.format(no))
    mahasiswa.append(tambah)
    verify = input('Tambah Data ? (y/n)')
    if verify == 'y':
        mahasiswa = mahasiswa
        no += 1
    else:
        print('=======================================================')
        print('| No |   Nama   |   Nim   | Tugas | UTS | UAS | Akhir |')
        print('========================================================')
        for data in mahasiswa:
            print(format(data))
        print('========================================================')
        exit()

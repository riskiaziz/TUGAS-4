#FLOWCHART
https://drive.google.com/file/d/1Lqk8cRhQGLqeF9q0XfGK4W7XbvIHXVa-/view?usp=drivesdk
#PSEUDOCODE
# Inisialisasi Matriks A dan B
DEFINISIKAN Orde_A sebagai [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
DEFINISIKAN Orde_B sebagai [[8, 14, -6], [12, 7, 4], [-11, 3, 21]]

# Memeriksa orde matriks
JIKA panjang(Orde_A) != 3 ATAU panjang(Orde_B) != 3 ATAU panjang(Orde_A[0]) != 3 ATAU panjang(Orde_B[0]) != 3 THEN
    TAMPILKAN "Matriks tidak dapat dikalikan, pastikan kedua matriks berordo 3x3."
    KELUAR

# Inisialisasi matriks hasil
DEFINISIKAN hasil sebagai matriks 3x3 dengan nilai awal 0

# Mengalikan matriks A dan B
UNTUK i DARI 0 HINGGA 2 Lakukan
    UNTUK j DARI 0 HINGGA 2 Lakukan
        hasil[i][j] = 0
        UNTUK k DARI 0 HINGGA 2 Lakukan
            hasil[i][j] += Orde_A[i][k] * Orde_B[k][j]

# Menampilkan hasil perkalian
TAMPILKAN "Hasil perkalian matriks A dan B adalah:"
UNTUK setiap baris dalam hasil Lakukan
    TAMPILKAN baris

TAMPILKAN "Selesai"
#PROGRAM PYTHON
Matriks A dan B yang sudah ditentukan
Orde_A = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
Orde_B = [[8, 14, -6],
          [12, 7, 4],
          [-11, 3, 21]]

# Memeriksa apakah orde matriks sesuai
if len(Orde_A) != 3 or len(Orde_B) != 3 or len(Orde_A[0]) != 3 or len(Orde_B[0]) != 3:
    print("Matriks tidak dapat dikalikan, pastikan kedua matriks berordo 3x3.")
else:
    # Inisialisasi matriks hasil
    hasil = [[0 for _ in range(3)] for _ in range(3)]

    # Mengalikan matriks A dan B
    for i in range(3):
        for j in range(3):
            hasil[i][j] = sum(Orde_A[i][k] * Orde_B[k][j] for k in range(3))

    # Menampilkan hasil perkalian
    print("Hasil perkalian matriks A dan B adalah:")
    for row in hasil:
        print(row)

print("Selesai")

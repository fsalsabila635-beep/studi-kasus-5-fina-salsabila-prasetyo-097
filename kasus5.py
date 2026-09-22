# sistem pemesanan hotel

# function unutuk menghitung biaya pemesanan hotel
def hitung_biaya(jenis_kamar, lama_menginap):
    if jenis_kamar == "Standard":
        tarif = 200000
    elif jenis_kamar == "Deluxe":
        tarif = 350000
    else:
        tarif = 0

    total_biaya = tarif * lama_menginap
    return total_biaya

# input data pemesanan hotel
jenis_kamar = input("masukkan jenis kamar (Standard/Deluxe): ")
tanggal_checkin = input("masukkan tanggal check-in: ")
tanggal_checkout = input("masukkan tanggal check-out: ")
lama_menginap = int(input("masukkan lama menginap (malam): "))

# memanggil function
total_biaya = hitung_biaya(
    jenis_kamar,
    tanggal_checkin,
    tanggal_checkout,
    lama_menginap
)

# hasil
print("\n===== PEMESANAN HOTEL =====")
print("jenis kamar      : ", jenis_kamar)
print("tanggal check-in : ", tanggal_checkin)
print("tanggal check-out: ", tanggal_checkout)
print("lama menginap    : ", lama_menginap, "malam")
print("total biaya      : ", total_biaya)
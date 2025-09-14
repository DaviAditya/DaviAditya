print("__________________________________")
print("___Diecast Collection Tracker___")
print("Welcome To The Collection Tracker")
print("===================================")

brand = ["HotWheels", "Tomica"]
print("Menu Diecast Collection Tracker")
print("[1].HotWheels\n[2].Tomica\n[3].List Diecast\n[4].Tambah Diecast\n[5].Hapus Diecast\n[6]Keluar")
print("________________________________")

pilihan = input("Apa yang ingin Anda kunjungi?? ")
if pilihan == "1":
    print("HotWheels")
    jenis = input("Jenis Hothwheels: Reguler/Silver? ")
    if jenis == "1":
        print("Reguler: Ferarri")
    elif jenis == "2":
        print("Siver: Accelarace")
    print("----------------------------------")
elif pilihan == "2":
    print("Tomica")
    jenis = input("Seri Tomica: Mainline/Dream? ")
    if jenis == "1":
        print("Mainline: Toyota")
    elif jenis =="2":
        print("Dream: Pokemon")
    print("----------------------------------")
elif pilihan == "3":
    print("List Diecast:",(brand))
    print("------------------------------")
elif pilihan == "4":
    brand_baru = input("Tambahkan Diecast: ")
    brand.append(brand_baru)
    print("Berhasil menambahkan: ", brand_baru)
    print("----------------------------------")
elif pilihan == "5":
    remove = input("Brand apa yang ingin dihapus?? ")
    brand.remove(remove)
    print(f"Berhasil Menghapus {remove}")
    print("Brand yang tersedia:", (brand))
    print("-------------------------------")
elif pilihan == "6":
    print("=============")
    print("---THANKS---")
    print("=============")

else:
    print("========================")
    print("--Menu Belum Tersedia--")
    print("========================")
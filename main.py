# Import kelas transaksi dari modul Transaksi
from transaksi import Transaksi


asc = """


 ______     __   __     _____     __        __    __     ______     ______     ______  
/\  __ \   /\ "-.\ \   /\  __-.  /\ \      /\ "-./  \   /\  __ \   /\  == \   /\__  _\ 
\ \  __ \  \ \ \-.  \  \ \ \/\ \ \ \ \     \ \ \-./\ \  \ \  __ \  \ \  __<   \/_/\ \/ 
 \ \_\ \_\  \ \_\\"\_\  \ \____-  \ \_\     \ \_\ \ \_\  \ \_\ \_\  \ \_\ \_\    \ \_\ 
  \/_/\/_/   \/_/ \/_/   \/____/   \/_/      \/_/  \/_/   \/_/\/_/   \/_/ /_/     \/_/ 
                                                                                       

                                            

"""
print(asc)

print("===SELAMAT DATANG DI SISTEM KASIR SUPERMARKET===" )

# Membuat objek transaksi dengan id 202
trans = Transaksi(202)

# Loop utama
while (1<2):

    # Menampilkan menu utama
    print("\n1. Tambah item")
    print("2. Perbarui item")
    print("3. Hapus item")
    print("4. Reset transaksi")
    print("5. Cek pemesanan")
    print("6. Hitung total ")
    print("7. Bayar")
    print("8. Keluar\n")

    # Req input dari user
    try:
        pil = int(input("Masukkan pilihan Anda (1-8): "))
    except ValueError:
        # Jika input bukan angka maka akan menampilkan pesan error
        print("Mohon maaf input hanya dalam angka")
        continue

    
    if pil == 1:
        # Tambah item
        # Mengambil input nama item, jumlah item, dan harga item
        try:
            item_name = input("Masukkan nama item: ")
            item_qty = int(input("Masukkan jumlah item: "))
            item_price = int(input("Masukkan harga item: "))
        except ValueError:
            # Jika input jumlah item atau harga item bukan angka, tampilkan pesan error
            print("Input jumlah dan harga item harus dalam angka")
            continue
        # Menambah item ke transaksi
        trans.add_item([ item_name, item_qty, item_price ])
        # Tampilkan pesan sukses
        print(f"{item_name} telah ditambahkan")
    elif pil == 2:
        # Update item
        # Mengambil input nama item dan pilihan data yang ingin diperbarui
        try:
            item_name = input("Masukkan nama item yang dibeli: ")
            update_pil = int(input("Pilih data yang ingin diperbarui (1. Nama item, 2. Jumlah item, 3. Harga item): "))
        except ValueError:
            # Jika input bukan angka, tampilkan pesan error
            print("Input pilihan harus dalam angka!")
            continue

        # Melakukan perbaruan item sesuai dengan pilihan
        if update_pil == 1:
            new_item_name = input("Masukkan nama item yang baru: ")
            trans.update_item_name(item_name, new_item_name)
            print(f"Nama item {item_name} telah diubah menjadi {new_item_name}")
        elif update_pil == 2:
            try:
                new_qty = int(input("Masukkan jumlah baru: "))
            except ValueError:
                print("Input jumlah item harus angka")
                continue
            trans.update_item_qty(item_name, new_qty)
            print(f"Jumlah item {item_name} telah diubah menjadi {new_qty}")
        elif update_pil == 3:
            try:
                new_price = int(input("Masukkan harga baru: "))
            except ValueError:
                print("Input harga item harus angka")
                continue
            trans.update_item_price(item_name, new_price)
            print(f"Harga {item_name} telah diubah menjadi {new_price}")
        else:
            print("Pilihan tidak tersedia")
    elif pil == 3:
        # Hapus item
        # Mengambil input nama item yang ingin dihapus
        item_name = input("Masukkan nama item yang ingin dihapus: ")
        trans.delete_item(item_name)
        print(f"{item_name} telah dihapus")
    elif pil == 4:
        # Menghapus semua item 
        trans.reset_transaction()
        print("Transaksi telah direset")
    elif pil == 5:
        # Cek pemesanan
        trans.check_order()
    elif pil == 6:
        # Hitung total belanja dan Menampilkan total belanja
        total_price = trans.total_price()
        print(f"Total belanja: {total_price}")
    elif pil == 7:
        # Bayar
        trans.checkout_and_pay()
    elif pil == 8:
        # Tampilkan pesan dan keluar dari loop  utama
        print("Terima kasih telah menggunakan sistem ini🙏")
        break
    else:
        # Jika pilihan tidak valid, tampilkan pesan error
        print("Pilihan tidak ada")
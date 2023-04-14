# Import Library
from tabulate import tabulate
import time
import csv


class Transaksi:
    
    '''
    Class untuk melakukan transaksi dan menyimpan informasi transaksi.
    '''

    def __init__(self, trnsct_id):
        '''
       Constructor untuk membuat objek Transaksi.
       ^====^====^====^====^====^====^====^====^===^
       trnsct_id : int (ID transaksi)
       '''
        self.trnsct_id = trnsct_id
        self.items = []

    def add_item(self, item):
        '''
        Function add_item() adl function dari class Transaksi yang berfungsi untuk menambahkan item/barang pada daftar item transaksi.
       ^====^====^====^====^====^====^====^====^===^
        item: list (Berisi informasi mengenai item, yaitu item_name dan item_quantity)
        '''
        item_name = item[0]
        item_exists = False
        for existing_item in self.items:
            if existing_item[ 0 ] == item_name:
                existing_item[ 1 ] += item[ 1 ]
                item_exists = True
                break

        if not item_exists:
            self.items.append(item)

    def update_item_name(self, item_name, new_item_name):
        '''
        Function update_item_name() adl function dari class Transaksi yang berfungsi untuk mengupdate nama item dalam transaksi
        ^====^====^====^====^====^====^====^====^===^
        item_name: str (Nama item yang ingin diupdate)
        new_item_name: str (Nama baru yang akan disetting dalam item)
        '''
        for item in self.items:
            if item[ 0 ] == item_name:
                item[ 0 ] = new_item_name

    def update_item_qty(self, item_name, new_qty):
        '''
        Function update_item_qty() adl function dari class Transaksi yang berfungsi untuk mengupdate 
        jumlah item yang ada di dalam list 'items' transaksi.
        ^====^====^====^====^====^====^====^====^===^
        new_qty: int (Jumlah baru yang ingin diupdate)
        '''
        for item in self.items:
            if item[ 0 ] == item_name:
                item[ 1 ] = new_qty

    def update_item_price(self, item_name, new_price):
        '''
        Function update_item_price() adl function dari class Transaksi yang berfungsi untuk mengupdate 
        harga barang yang ada di dalam list 'items' transaksi.
        ^====^====^====^====^====^====^====^====^===^
        new_price: int (Harga baru dari barang yang ingin diupdate)
        '''
        for item in self.items:
            if item[ 0 ] == item_name:
                item[ 2 ] = new_price

    def delete_item(self, item_name):
        '''
       Function update_item_price() adl function dari class Transaksi yang berfungsi untuk menghapus 
       barang yang ada di dalam list 'items' transaksi.
       '''
        for item in self.items:
            if item[ 0 ] == item_name:
                self.items.remove(item)

    def reset_transaction(self):
        '''
        Function reset_transaction() adl function dari class Transaksi untuk mereset daftar item yang telah ada di transaksi.
        '''
        self.items = [ ]

    def check_order(self):
        '''
        Function check order() adl function dari class Transaksi untuk memeriksa nilai kebenaran pesanan yang dibuat.
        Jika data pesanan memiliki kekurangan informasi (None), maka akan menampilkan pesan
        "Kesalahan pada saat menginput data"
        Jika semua data pesanan sudah benar, maka akan menampilkan tabel pesanan beserta informasi jumlah barang, harga, dan total harga yang harus dibayar.
        '''
        for item in self.items:
            if None in item:
                print("Kesalahan pada saat menginput data")
                return
            else:
                print("Pemesanan sudah benar")

        total_price = 0
        order_table = [ ]
        for i, item in enumerate(self.items):
            item_price = item[ 1 ] * item[ 2 ]
            total_price += item_price
            order_table.append([ i + 1, item[ 0 ], item[ 1 ], item[ 2 ], item_price ])

        order_table.append([ "Total", "", "", "", total_price ])
        print(tabulate(order_table, headers = [ "No.", "Nama Item", "Jumlah", "Harga", "Total" ]))

    def total_price(self):
        '''
        Function total_price() adl function dari class Transaksi untuk menghitung harga total barang berdasarkan item yang dibeli.
        Jika total pembelian melebihi kriteria maka akan mendapatkan diskon yang sesuai.
        '''
        total_price = 0
        for item in self.items:
            total_price += item[ 1 ] * item[ 2 ]

        discount = 0
        if total_price > 500000:
            discount = 0.9
            print("Selamat anda mendapat diskon sebesar 10% 🥳 ")
        elif total_price > 300000:
            discount = 0.92
            print("Selamat anda mendapat diskon sebesar 8% 🥳 ")
        elif total_price > 200000:
            discount = 0.95
            print("Selamat anda mendapat diskon sebesar 5% 🥳 ")
        else:
            print("Anda belum berhak mendapatkan diskon 😭 ")

        if discount != 0:
            print("Diskon: {}".format(total_price))
            total_price = total_price * discount

        return total_price

    def checkout_and_pay(self):
        '''
        Function checkout_and_pay() adl function dari class Transaksi untuk melakukan checkout dan pembayaran dari barang-barang
        yang telah dibeli .
        '''
        total_price = self.total_price()
        print("Harga total: {}".format(total_price))

        confirmation = input("Apakah Anda ingin melakukan pembayaran? (y/n) ")
        if confirmation.lower() == "y":
            try:
                payment = int(input("Masukkan nominal pembayaran: "))
            except ValueError:
                print("Input harus angka.")
                return
            change = payment - total_price
            if change < 0:
                print("Pembayaran kurang.")
                return
            with open("order_history.csv", "a", newline = '') as csvfile:
                writer = csv.writer(csvfile)
                for item in self.items:
                    writer.writerow(
                        [ time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), item[ 0 ], item[ 1 ], item[ 2 ],
                          item[ 1 ] * item[ 2 ] ])
            print("Pembayaran berhasil dilakukan. Kembalian Anda: {}".format(change))
            self.reset_transaction()
        else:
            print("Pembayaran dibatalkan.")

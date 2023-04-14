# Python-Super-Cashier-System-Project-Pacmann

## Latar Belakang
Latar belakang dari masalah yang dihadapi oleh Andi adalah kebutuhan untuk memperbaiki proses bisnis di supermarket miliknya. Disini andi ingin membuat sistem kasir self-service agar customer dapat diberikan kemudahan dan kenyamanan dengan bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dari mana saja bahkan dari kota lain. Maka untuk memenuhi ekspetasi tersebut disini sebagai programmer saya diharapkan dapat membuat program super Cashier yang dapat memecahkan masalah tersebut.

## Objective & Requirements

### Objective
- Membuat sistem kasir self-service di supermarket milik Andi
- Sistem kasir self-service tersebut dapat melakukan pemasukan item-item yang dibeli oleh customer, jumlah item yang dibeli, dan harga item yang dibeli
- Customer bisa melakukan pembelian barang dari supermarket meskipun dari luar kota supermarket tersebut

### Requirements
- Membuat project Super Cashier menggunakan bahasa pemrograman Python.
- Mengimplementasikan materi function, branching, looping, data structure serta OOP dalam Super Cashier yang dibangun.
- Adapun beberapa library yang digunakan antara lain: csv, time dan tabulate

## Flowchart

## Penjelasan Kode Program
- `Transaksi` : adalah Class untuk melakukan transaksi dan menyimpan informasi transaksi.
- `add_item(self, item)`:  add_item() adl method dari class Transaksi yang berfungsi untuk menambahkan item/barang pada daftar item transaksi.
- `update_item_name(self, item_name, new_item_name)`: update_item_name() adl method dari class Transaksi yang berfungsi untuk mengupdate nama item dalam transaksi
- `update_item_qty(self, item_name, new_qty)`: update_item_qty() adl method dari class Transaksi yang berfungsi untuk mengupdate 
        jumlah item yang ada di dalam list 'items' transaksi.
- `update_item_price(self, item_name, new_price)`: update_item_price() adl function dari class Transaksi yang berfungsi untuk mengupdate 
        harga barang yang ada di dalam list 'items' transaksi.nama item yang harganya akan diubah dan harga baru dari item tersebut.
- `delete_item(self, item_name)`: update_item_price() adl method dari class Transaksi yang berfungsi untuk menghapus 
       barang yang ada di dalam list 'items' transaksi.
- `reset_transaction(self)`:  reset_transaction() adl method dari class Transaksi untuk mereset daftar item yang telah ada di transaksi.
- `check_order(self)`: check order() adl method dari class Transaksi untuk memeriksa nilai kebenaran pesanan yang dibuat.
        Jika data pesanan memiliki kekurangan informasi (None), maka akan menampilkan pesan
        "Kesalahan pada saat menginput data"
        Jika semua data pesanan sudah benar, maka akan menampilkan tabel pesanan beserta informasi jumlah barang, harga, dan total harga yang harus dibayar.
- `total_price(self)`: total_price() adl method dari class Transaksi untuk menghitung harga total barang berdasarkan item yang dibeli.
        Jika total pembelian melebihi kriteria maka akan mendapatkan diskon yang sesuai.
- `transaction`: attribute bertipe list ini digunakan untuk menyimpan daftar item yang ada dalam transaksi.
- `total_price`: attribute bertipe float ini digunakan untuk menyimpan total harga dari transaksi yang sedang berlangsung.
- `discount`: attribute bertipe float ini digunakan untuk menyimpan persentase diskon yang diterima dari transaksi yang sedang berlangsung.

## Test Case
<img src='https://github.com/Iwanplayground/Python-Cashier-System-Project-Pacmann/blob/main/img/menu.png'> <br>
### Test Case 1
Customer ingin menambahkan dua item baru menggunakan method add_item(). Item yang ditambahkan adalah sebagai berikut:

Nama Item: Ayam Goreng Kremes, Qty: 2, Harga: 20000 dan Pasta Gigi close down, Qty: 3, Harga: 15000 <br>
<img src='https://github.com/Iwanplayground/Python-Cashier-System-Project-Pacmann/blob/main/img/ayam.png'> <br>
<img src='https://github.com/Iwanplayground/Python-Cashier-System-Project-Pacmann/blob/main/img/psta gigi.png'> <br>
Menu setelah ditambahkan: <br>
<img src='https://github.com/Iwanplayground/Python-Cashier-System-Project-Pacmann/blob/main/img/menu%201st.png'> <br>

### Test Case 2
Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka Customer menggunakan method delete_item() untuk menghapus item. Item yang ingin dihapuskan adalah Pasta Gigi. <br>
<img src='https://github.com/Iwanplayground/Python-Cashier-System-Project-Pacmann/blob/main/img/item dihapus.png'> <br>
Menu setelah terdapat item yang dihapus: <br>
<img src='https://github.com/Iwanplayground/Python-Cashier-System-Project-Pacmann/blob/main/img/menu 2nd.png'> <br>

### Test Case 3
Ternyata setelah dipikir-pikir, Customer salah memasukkan item yang ingin dibelanjakan! Daripada menghapusnya satu satu, maka Customer cukup menggunakan method reset_transaction() untuk menghapus semua item yang sudah ditambahkan. <br>
<img src='https://github.com/Iwanplayground/Python-Cashier-System-Project-Pacmann/blob/main/img/reset trans.png'> <br>
Setelah semua transaksi direset: <br>
<img src='https://github.com/Iwanplayground/Python-Cashier-System-Project-Pacmann/blob/main/img/endres.png'> <br>

### Test Case 4
Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method total_price(). Sebelum mengeluarkan output total belanja akan menampilkan item- item yang dibeli. <br>
<img src='https://github.com/Iwanplayground/Python-Cashier-System-Project-Pacmann/blob/main/img/last menu.png'> <br>
tampilan menu pembayaran: <br>
<img src='https://github.com/Iwanplayground/Python-Cashier-System-Project-Pacmann/blob/main/img/disk.png'> <br>
tampilan final saat proses transaksi selesai: <br>
<img src='https://github.com/Iwanplayground/Python-Cashier-System-Project-Pacmann/blob/main/img/bayar.png'> <br>


## Kesimpulan
Project python yang telah diprogram tersebut merupakan kode untuk mengelola transaksi pembelian barang di sebuah supermarket yang dimiliki Andi. Proyek ini menggunakan class Transaksi yang memiliki beberapa method seperti add_item, update_item_name, update_item_qty, update_item_price, delete_item, reset_transaction, check_order, dan total_price. Method-method tsb digunakan untuk menambah, mengubah, menghapus item, mereset transaksi, memeriksa pemesanan, dan menghitung total harga serta diskon yang didapatkan.

### Fitur yang dapat dikembangkan kedepan
- Mungkin kedepannya bisa dikembangkan Super Cashier dengan apps di web atau mobile dengan interface yang jauh lebih user friendly
- Mengembangkan fitur seperti tracking barang yang sudah pernah dibeli melalui history sehingga user dapat melihat transaksi yang dilakukan di masa lalu 
- Mengembangkan fitur seperti rincian tipe harga karena tentunya beberapa barang seperti beras, tepung, daging dijual kiloan lalu untuk kertas dalam rim, gelas dan piring dalam lusin serta barang lain yang sekiranya tipenya cukup spesifik.

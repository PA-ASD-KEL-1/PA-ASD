Deskripsi program
Program ini dibuat menggunakan bahasa pemrograman Python yang terhubung dengan database yang berguna untuk membantu meningkatkan efisiensi pengelolaan data buku di perpustakaan. Program ini memiliki fitur login multiuser dengan user utamanya adalah admin dan pengunjung. Diprogram, user dapat melakukan registrasi akun dan nantinya data akun tersebut akan disimpan kedalam sebuah database. Selanjutnya pada menu admin, terdapat tampilan beberapa pilihan menu yang dapat dipilih diantaranya yaitu dapat menampilkan data , menambah data, mengurutkan data secara ascending, menghapus data, dan mencari data. Sedangkan pada menu pengunjung, terdapat tampilan untuk menampilkan data buku yang tersedia, melakukan peminjaman buku, melakukan pengembalian buku,dan dan melihat riwayat peminjaman buku.

Struktur project
Project ini terdiri dari 2 file, yaitu : File program dan file dokumentasi
File program sebagai file utama dari project ini berisi codingan yang menerapkan database mysql sebagai tempat penyimpanan data akun, peminjaman, pengembalian, serta history. Program ini juga menerapkan fungsi linkedlist untuk mengelola databuku, fungsi shellsort untuk mengsorting databuku, serta fungsi fibbonaccisearch untuk mengsearching databuku. Lalu selanjutnya file dokumentasi, yakni readme.md yang merupakan file yang berisi dokumentasi project, penjelasan singkat program, fitur fitur yang terdapat pada program serta termasuk cara untuk menjalankan program.

Fitur dan fungsionalitas
Berikut adalah beberapa contoh fitur dan fungsionalitas pada program:
Fitur Login: Memungkinkan user untuk login ke akun mereka dengan mengautentikasi username dan password. Dalam proses login, user harus memasukkan kombinasi dari username dan password yang kemudian akan diverifikasi oleh sistem sebelum memberikan akses ke akun tersebut.
Fitur Dashboard: Memberikan tampilan menu yang dapat dipilih oleh user. Fitur ini akan ditampilkan berdasarkan dari role user(menu/pengunjung) yang login dan merupakan tampilan awal ketika user telah berhasil login.

Fitur dan fungsionalitas role admin terdapat :
Fitur Tambah data: Memungkinkan admin untuk melakukan penambahan databuku kedalam sistem.
Fitur Pencarian: Memungkinkan admin untuk mencari data atau informasi mengenai databuku didalam sistem.
Fitur Sorting: Memungkinkan admin untuk memfilter atau mensorting databuku dalam sistem berdasarkan judul buku secara ascending (urutan secara abjad)
Fitur Hapus data : Memungkinkan admin untuk melakukan penghapusan databuku didalam sistem.
Fitur dan fungsionalitas role pengunjung terdapat :
Fitur Peminjaman : Memungkinkan user untuk melakukan peminjaman buku. Dan buku yang dipinjam hanya dapat dipinjam sekali saja.
Fitur Pengembalian : Memungkin user untuk melakukan pengembalian buku yang telah dipinjam sebelumnya.
Fitur History: Memungkinkan pengguna untuk melihat daftar buku yang pernah dipinjam sebelumnya.

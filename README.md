### Deskripsi Program
---

Program ini dibuat menggunakan bahasa pemrograman Python yang terhubung dengan database yang berguna untuk membantu meningkatkan efisiensi pengelolaan data buku di perpustakaan. Program ini memiliki fitur login multiuser dengan user utamanya adalah admin dan pengunjung. Diprogram, user dapat melakukan registrasi akun dan nantinya data akun tersebut akan disimpan kedalam sebuah database. Selanjutnya pada menu admin, terdapat tampilan beberapa pilihan menu yang dapat dipilih diantaranya yaitu dapat menampilkan data , menambah data, mengurutkan data secara ascending, menghapus data, dan mencari data. Sedangkan pada menu pengunjung, terdapat tampilan untuk menampilkan data buku yang tersedia, melakukan peminjaman buku, melakukan pengembalian buku,dan dan melihat riwayat peminjaman buku.

### Struktur Project
---

Project ini terdiri dari 2 file, yaitu : File program dan file dokumentasi

File program sebagai file utama dari project ini berisi codingan yang menerapkan database mysql sebagai tempat penyimpanan untuk data akun user, peminjaman buku, pengembalian buku, serta history peminjaman. Program ini juga menerapkan fungsi linkedlist untuk mengelola data buku, fungsi shellsort untuk mengsorting data buku, serta fungsi jumpsearch untuk mengsearching data buku. 
Lalu selanjutnya file dokumentasi, yakni readme.md yang merupakan file berisi dokumentasi project, penjelasan singkat program, fitur fitur yang terdapat pada program serta termasuk cara untuk menjalankan program.


### Fitur dan Fungsionalitas
---

* Berikut adalah beberapa contoh fitur dan fungsionalitas pada program:

  - Fitur Login: Memungkinkan user untuk login ke akun mereka dengan mengautentikasi username dan password. Dalam proses login, user harus memasukkan kombinasi dari    username dan password yang kemudian akan diverifikasi oleh sistem sebelum memberikan akses ke akun tersebut.
  - Fitur Dashboard: Memberikan tampilan menu yang dapat dipilih oleh user. Fitur ini akan ditampilkan berdasarkan dari role user(menu/pengunjung) yang login dan merupakan tampilan awal ketika user telah berhasil login.

* Fitur dan fungsionalitas role admin terdapat :

  - Fitur Tambah data : Memungkinkan admin untuk melakukan penambahan databuku kedalam sistem.
  - Fitur Pencarian : Memungkinkan admin untuk mencari data atau informasi mengenai databuku didalam sistem.
  - Fitur Sorting : Memungkinkan admin untuk memfilter atau mensorting databuku dalam sistem berdasarkan judul buku secara ascending
  - Fitur Hapus data : Memungkinkan admin untuk melakukan penghapusan databuku didalam sistem.

* Fitur dan fungsionalitas role pengunjung terdapat :

  - Fitur Peminjaman : Memungkinkan user untuk melakukan peminjaman buku. Dan buku yang dipinjam hanya dapat dipinjam sekali saja.
  - Fitur Pengembalian : Memungkin user untuk melakukan pengembalian buku yang telah dipinjam sebelumnya.
  - Fitur History: Memungkinkan pengguna untuk melihat daftar buku yang pernah dipinjam sebelumnya.
  
  
### Cara Penggunaan
---

Program ini merupakan program CRUD (Create, Read, Update, Delete) dengan fitur login multiuser yang dibuat dengan menggunakan bahasa pemrograman Python. Program ini memiliki dua role user utama yaitu admin dan pengunjung.

Untuk memulai program ini, jika user (pengunjung) belum memiliki akun, user perlu melakukan registrasi akun terlebih dahulu, akun dapat dengan mudah dibuat hanya dengan memasukkan nama lengkap, username, dan password. 

Lalu kemudian setelah user berhasil membuat akun, user perlu mengakses fitur login untuk dapat masuk ke dalam program. 
Difitur login user akan diminta untuk memasukkan username dan password yang telah dibuat sebelumnya. 
*Disclamer (Fitur registrasi hanya dapat dimanfaatkan oleh role user pengunjung saja. Dan untuk role user admin tidak perlu membuat akun)*

Setelah berhasil login, user akan diarahkan ke menu dashboard yang terdiri dari beberapa pilihan menu. Jika role user yang berhasil login merupakan admin, maka akan tampil beberapa pilihan menu khusus admin yang dapat dipilih seperti menu menampilkan data buku, menambah data buku, menghapus data buku, mencari data buku, mengurutkan data buku secara ascending serta menu exit untuk keluar dari program. 

Sedangkan jika role user yang login merupakan pengunjung, maka akan tampil beberapa pilihan menu pengunjung yang dapat dipilih seperti menu menampilkan data buku, meminjam buku, mengembalikan buku, melihat histori peminjaman buku, dan menu exit untuk keluar dari program. 

Setiap pilihan menu memiliki fungsinya masing-masing dan tampilannya akan sangat berbeda menyesuaikan role user yang sedang login. 
Program ini akan terus berjalan hingga user memilih untuk keluar dari program. Jadi, setelah user selesai menggunakan program, user dapat keluar dari program dengan memilih menu exit atau menutup program secara langsung.

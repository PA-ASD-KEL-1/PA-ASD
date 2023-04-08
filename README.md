Perpustakaan merupakan tempat yang menyediakan berbagai jenis buku untuk dipinjam oleh masyarakat umum.tujuan adanya perpustakaan adalah untuk mendukung Pendidikan masyarakat.namun,seringkali perpustakaan masih kurang efisien/efektif dalam mengelola data buku.oleh karena itu program ini dibuat dengan harapan dapat membantu mengatasi masalah tersebut.
Program ini dibuat menggunakan bahasa pemrograman python. Dalam program ini terdapat login yang terdiri dari login pengunjung dan admin,jika pengunjung belum memiliki akun maka dapat mendaftar terlebih dahulu,pembuatan menu login ini terhubung dengan database,sehingga saat pengunjung melakukkan registrasi maka data tersebut akan tersimpan didalam database Bersama dengan data pengunjung yang sudah ada dan admin. Pada menu admin,terdapat pilihan tampilkan data buku,tambah data buku,urutkan data buku,menghapus data buku,searching data buku.sedangkan pada menu pengunjung terdapat pilihan tampilkan data buku.

Program ini dibuat dengan tujuan:
1.)	Mempermudah pengunjung untuk mencari dan meminjam buku yang tersedia.
2.)	Untuk menampilkan buku sesuai dengan abjad
3.)	Untuk menampilkan jumlah stok dari buku yang tersedia
4.)	Memudahkan admin untuk menambah dan menggubah data buku.

Fitur yang ada di dalam program dan fungsinya:
1.)	Node class,berfungsi untuk mepresentasikan node pada linked list yang berisi data yang ingin disimpan dan pointer ke node selanjutnya.
2.)	Linked list,merupakan sebuah class yang memresentasikan linked list yang berisi metode untuk menghapus data,menambah data,menampilkan data,dan melakukan sorting.
3.)	Tambah data,berfungsi untuk menambah data ke dalam linked list.
4.)	Hapus data,berfungsi untuk menghapus data yang ada dalam linked list.
5.)	Tampil,berfungsi untuk menampilkan data yang ada di dalam linked list.
6.)	Get_lenght berfungsi untuk menghitung jumlah node yang ada pada linked list
7.)	sorting,pada program ini menggunakan quick sort untuk mengurutkan data buku yang ada.fungsi  sorting pada program ini adalah untuk mengurutkan data buku sesuai dengan abjad.
8.)	Searching,program ini menggunakan Fibonacci search untuk mencari data buku yang tersedia,untuk menggunakan searching penggunjung dapat menginput judul buku yang ingin dicari.



Cara penggunaan program:
Menu awal terdapat dua pilihan yang pertama merupakan login dan yang kedua merupakan register.pada menu login admin maupun pengunjung akan diminta untuk menginput username dan password jika username dan password yang di input sesuai maka akan lanjut ke menu selanjutnya(admin ke menu admin dan pengunjung ke menu pengunjung),tetapi bila username atau password yang dimasukkan salah maka akan Kembali ke menu awal.pada menu register pengunjung akan diminta untuk menginput username dan password,sesudah itu data yang diinput akan masuk ke database.
Penggunaan program ini cukup sederhana.penggunjung dapat mencari buku dan meminjam buku yang tersedia,sedangkan admin dapat menambah data buku,menghapus,dan mengedit data buku. 

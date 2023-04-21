#PA ASD Kelompok 1
from prettytable import PrettyTable
import os, time, pwinput
import mysql.connector
import math

def clear():
    os.system('cls')

try :
    db = mysql.connector.connect(
    host='db4free.net',
    user='perpuskelompok1',
    password='kelompok1',
    database='perpuskelompok1'
    )
    
     class Node:
        def __init__(self, data1, data2, data3, data4):
            self.data1 = data1 
            self.data2 = data2
            self.data3 = data3
            self.data4 = data4
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None
            self.ul = []
            self.searching = []
            
        def tambahdata(self, data1, data2, data3, data4):
            newdata = Node(data1, data2, data3, data4)
            if not self.head:
                self.head = newdata
                clear()
                print("Berhasil menambahkan data buku")
                return
            else :
                current = self.head
                while current:
                    if current.data1 == newdata.data1:
                        clear()
                        print(f"Data buku dengan judul {current.data1} telah ada!")
                        return
                    if not current.next:
                        break
                    current = current.next
                current.next = newdata
                clear()
                print("Berhasil menambahkan data buku")

        def hapusdata(self):
            if not self.head :
                print("Data buku masih kosong")
            else :
                b1 = input("Masukan judul buku : ").capitalize()
                current = self.head
                if current and current.data1 == b1:
                    self.head = current.next
                    current = None
                    print("Data buku berhasil dihapus")
                    return
                prev = None
                while current and current.data1 != b1:
                    prev = current
                    current = current.next
                if current is None:
                    print("Data buku tidak ditemukan!")
                    return
                prev.next = current.next
                current = None
                print("Data buku berhasil dihapus!")    
        
        def jumpsearch(self,arr,x,n):
            step = math.sqrt(n)
            prev = 0
            while arr[int(min(step,n)-1)]<x:
                prev = step
                step += math.sqrt(n)
                if prev >= n:
                    return -1
            while arr[int(prev)] < x:
                prev += 1
                if prev == min(step, n):
                    return -1
            if arr[int(prev)] == x:
                return int(prev)
            return -1
        
        def tampil(self):
            if not self.head:
                print("Data masih kosong")
            else:
                current = self.head
                no = 1
                table = PrettyTable(["No", "Judul Buku", "Nama Pengarang", "Jumlah Halaman", "Stok"])
                while current is not None and current.data4 > 0:
                    table.add_row([no,current.data1,current.data2,current.data3,current.data4])
                    no += 1
                    current = current.next
                print(table)
                
        def tambahlist(self):
            current_node = self.head
            while current_node is not None:
                self.searching.append(current_node.data1)
                current_node = current_node.next
                
        def shellsort(self):
            j = self.get_length()
            if j > 0 :
                gap = j // 2
                while gap > 0 :
                    for i in range(gap,j):
                        temp_node = self.get_node_at_index(i)
                        temp_data1 = temp_node.data1
                        temp_data2 = temp_node.data2
                        temp_data3 = temp_node.data3
                        temp_data4 = temp_node.data4
                        v = i 
                        while v >= gap and self.get_node_at_index(v - gap).data1>temp_data1:
                            node_v_gap = self.get_node_at_index(v - gap)
                            self.get_node_at_index(v).data1 = node_v_gap.data1
                            self.get_node_at_index(v).data2 = node_v_gap.data2                
                            self.get_node_at_index(v).data3 = node_v_gap.data3
                            self.get_node_at_index(v).data4 = node_v_gap.data4                
                            v -= gap
                        self.get_node_at_index(v).data1 = temp_data1
                        self.get_node_at_index(v).data2 = temp_data2
                        self.get_node_at_index(v).data3 = temp_data3
                        self.get_node_at_index(v).data4 = temp_data4
                    gap //= 2
                    print("Berhasil mengurutkan data buku")
                    LinkedList.tampil(self)
            else :
                LinkedList.tampil(self)

        def get_node_at_index(self, index):
            current_node = self.head
            count = 0
            while current_node is not None:
                if count == index:
                    return current_node
                count += 1
                current_node = current_node.next
            return None
        
        def get_length(self):
            current_node = self.head
            count = 0
            while current_node:
                count += 1
                current_node = current_node.next
            return count
            

    ll = LinkedList()

    def tambah():
        while True:
            a1 = input("Masukan judul buku : ").capitalize()
            a1_space = a1.strip()
            if all(j.isalnum() or j.isspace() for j in a1) and len(a1_space) > 0:
                a2 = input("Masukan nama pengarang buku : ").capitalize()
                a2_space = a2.strip()
                if all(s.isalnum() or s.isspace() for s in a2) and len(a2_space) > 0:
                    try :
                        a3 = int(input("Masukan jumlah halaman buku : "))
                        a4= int(input("masukan jumlah stok buku : "))
                        if a4 >= 1:
                            ll.tambahdata(a1, a2, a3,a4)
                            ll.tampil()
                            break
                        else :
                            clear()
                            print("Stok tidak bisa 0")
                    except:
                        clear()
                        print("Mohon inputkan data dengan benar!\n")
                else :
                    clear()
                    print("Mohon masukan nama pengarang dengan benar!\n")
            else :
                clear()
                print("Mohon masukan judul buku dengan benar!\n")
                
    def search():
        clear()
        ll.shellsort()
        ll.tambahlist()
        try :
            cari = input("\nMasukan judul buku yang ingin dicari : ").capitalize()
            result = ll.jumpsearch(ll.searching,cari,len(ll.searching))
            if result == -1:
                clear()
                print(f"Data buku dengan judul {cari} tidak ditemukan")
            else:
                c = result
                c += 1
                clear()
                print(f"Data buku dengan judul {cari} ditemukan dinomor {c}")
        except :
            clear()
            print(f"Data buku tidak ditemukan")
    
    def pinjam():
        clear()
        ll.tampil()
        try :
            user = ll.ul[0]
            a = str(input("\nMasukan judul buku yang ingin dipinjam : ")).capitalize()
            node = ll.get_node_at_index(ll.jumpsearch(a))
            if not node:
                print("Data buku tidak ditemukan")
                return
            else :
                if node.data4 < 1:
                    clear()
                    print("stok tidak cukup")
                else:
                    myycursor = db.cursor()
                    sqlll = (f"Select namabuku from pinjambuku where namabuku = '{a}' and user= '{user}'")
                    myycursor.execute(sqlll)
                    results = myycursor.fetchone()

                    if results is None:
                        mycursor = db.cursor()
                        node.data4 -= 1
                        databuku = node.data1
                        jumlah = 1
                        sql = "INSERT INTO pinjambuku(namabuku, jumlah, user) VALUES (%s, %s, %s)"
                        val = (databuku, jumlah, user)
                        mycursor.execute(sql, val)
                        db.commit()
                        clear()
                        print(f"Jumlah buku yang dipinjam: {1} ,judul buku: {node.data1} berhasil dipinjam")
                    else :
                        clear()
                        print(f"Buku dengan judul {a} hanya bisa dipinjam sekali")
        except :
            clear()
            print(f"Gagal melakukan peminjaman, data buku tidak ditemukan")

    def kembalikan():
        b = input("\nMasukan judul buku yang ingin dikembalikan : ").capitalize()
        node = ll.get_node_at_index(ll.jumpsearch(b))
        if not node:
            clear()
            print("Data buku tidak ditemukan")
            return
        else :
            user = ll.ul[0]
            mcursor = db.cursor()
            sqll = (f"SELECT status FROM pinjambuku WHERE user = '{user}' and namabuku = '{b}'")
            mcursor.execute(sqll)
            result = mcursor.fetchone()

            a = "belum dikembalikan"
            for i in result:
                if i == a:
                    o = "dikembalikan"
                    ssql = (f"Update pinjambuku set status = '{o}' where user = '{user}' and namabuku = '{b}'")
                    mcursor.execute(ssql)
                    node.data4 +=1
                    db.commit()
                    clear()
                    print(f"Jumlah buku yang dikembalikan: {1}, judul buku: {node.data1} berhasil dikembalikan")
                else :
                    clear()
                    print("Buku sudah dikembalikan")

    def histori():
        user = ll.ul[0]
        cursorr = db.cursor()
        sqll = (f"SELECT namabuku,jumlah,status,user FROM pinjambuku WHERE user = '{user}'")
        cursorr.execute(sqll)
        results = cursorr.fetchall()
        import prettytable
        x = prettytable.PrettyTable()
        no = 1
        x.field_names = ["No", "Nama Buku", "Jumlah buku", "Status", "Peminjam"]
        if results is not None:
            for i in results:
                x.add_row([no, i[0], i[1], i[2], i[3]])
                no += 1
            print("Daftar riwayat Peminjaman Buku")
            print(x)
        else:
            clear()
            print("History masih kosong, belum ada data")



except mysql.connector.Error as error:
    clear()
    print("Tidak dapat terhubung kedatabase!")

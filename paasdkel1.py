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

except mysql.connector.Error as error:
    clear()
    print("Tidak dapat terhubung kedatabase!")

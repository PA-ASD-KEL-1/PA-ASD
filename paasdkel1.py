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


except mysql.connector.Error as error:
    clear()
    print("Tidak dapat terhubung kedatabase!")
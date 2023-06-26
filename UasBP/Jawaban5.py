import mysql.connector
import os

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="toko_kebab"
)
if db.is_connected():
    print("Berhasil Terhubung")

def insert_data(db):
  customers_id = input("Masukan id costumers: ")
  Nama = input("Masukan nama: ")
  Alamat = input("Masukan alamat: ")
  val = (customers_id,Nama, Alamat)
  cursor = db.cursor()
  sql = "INSERT INTO customers (customer_id,Nama, Alamat) VALUES (%s,%s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil disimpan".format(cursor.rowcount))


def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM customers"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def search_data(db):
  cursor = db.cursor()
  keyword = input("Kata kunci: ")
  sql = "SELECT * FROM customers WHERE Nama LIKE %s OR Alamat LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def show_menu(db):
  print("=== APLIKASI DATABASE PYTHON ===")
  print("1. Insert Data")
  print("2. Tampilkan Data")
  print("3. Cari Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if _name_ == "_main_":
  while(True):
    show_menu(db)
# Fungsi Exeption Handling
try:
    x =int(input("Masukan bilangan :"))
    assert x % 2 == 0
except:
    print("bukan bilangan genap")
else:
    print("bilangan genap")



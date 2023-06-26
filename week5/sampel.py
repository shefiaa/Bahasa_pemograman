# contoh penambahan terkait break/continue
for val in "bahasa" :
    if val =="h" :
        continue
    #break
    print(val)
print("selesai")

# contoh cara coding sederhana
def tambah():
    a = int(input("angka 1 = "))
    b = int(input("angka 2 = "))
    c = a+b
    print(c)
def kurang():
    a = int(input("angka 1 = "))
    b = int(input("angka 2 = "))
    c = a-b
    print(c)
def kali():
    a = int(input("angka 1 = "))
    b = int(input("angka 2 = "))
    c = a*b
    print(c)
def pilihan():
    print("1. +")
    print("2. -")
    print("3. *")
    print("exit")

while True:
    pilihan()
    pil=int(input("pilihan = "))
    if pil==1:
        tambah()
    elif pil==2:
        kurang()
    elif pil==3:
        kali()
    else :
        break
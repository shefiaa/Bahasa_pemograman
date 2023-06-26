def pilihan():
    menu1 = "capucino"
    menu2 = "teh"
    print ("Pilihan")
    print ("1.", menu1)
    print ("2.", menu2)
    print ("3. Exit")

def capucino():
    zebua = "memilih capucino"
    print(zebua)
    capucino = int(input("masukkan harga : "))
    PPN = 10/100
    harga = capucino*PPN
    total = capucino+harga
    print("jumlah yang harus di bayar", total)

def teh():
    teh = "memilih TEH"
    print(teh)
    teh = int(input("masukkan harga : "))
    PPN = 10/100
    harga = teh*PPN
    total = teh+harga
    print("jumlah yang harus di bayar", total)

def data():
    NIM = "20210801104"
    NAMA = "SHEFIA ANGGRAENI"
    print ("NIM : ", NIM)
    print ("NAMA : ", NAMA)

while True:
    data()
    pilihan()
    a = int(input("masukkan pilihan : "))
    if a == 1:
        capucino()
    elif a == 2:
        teh()
    elif a == 3:
        break
    else:
        print ("pilihan tidak tersedia")
        
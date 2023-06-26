# looping with range
for a in range(3) :
    print(a)
# looping python with break
for i in range(1, 10):
    print(i,' x ',i,'=',i*i)
    if i == 5:
        break
 
# looping python with continue
for i in range(1) :
    print(i)
    for a in "perkuliahan":
        if a == "p" :
            continue
        print(a)
    print("end")
# nested loop
listNama = ['Shefia', 'Tasya', 'Nanda', 'Restu', 'Dilah']
for Nama in listNama :
        print(Nama)
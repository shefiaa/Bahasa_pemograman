import tkinter
import tkinter.messagebox as messagebox

top = tkinter.Tk()

def helloCallBack():
    messagebox.showinfo( "Hello Python", "SHEFIA")

B = tkinter.Button(top, text ="20210801104 \n Shefia Anggraeni \n Teknik Informatika \n UAS Bahasa Pemrograman", command =helloCallBack)

B.pack()
top.mainloop()

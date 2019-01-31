from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def app():
        messagebox.showinfo("About app", "Notepad Version 1.0")
def author():
        messagebox.showinfo("About author", "Imanbay Nursaid \nIT Genius")
def new_file(event = None):
        txt.delete(1.0,END)
        win.title("untitled.txt")
def close():
        if messagebox.askyesno("Exit","Are you sure want to exit ?") :
                win.destroy()
def open_file(event = None):
        filename = filedialog.askopenfilename()
        pos = filename.rfind("/")
        newname = filename[pos+1:]
        win.title(newname)
        file = open(filename, "r")
        content = file.read()
        txt.insert(END, content)
def save_file(event = None):
        filename = filedialog.asksaveasfile(mode = "w", defaultextension = ".py")
        save = str(txt.get(0.0,END))
        filename.write(save)
        filnename.close()

def delete():
        txt.delete(1.0,END)
win = Tk()
win.geometry("400x400")
win.title("My Notpad")
win.config(bg = "#212223")

win.protocol("WM_DELETE_WINDOW", close)


frm1 = Frame(win, bg = "#212223")
frm1.pack()

menubar = Menu()
win.config(menu = menubar)

fmenu = Menu(menubar, tearoff = False)
menubar.add_cascade(label = "File", menu = fmenu)
fmenu.add_command(label = "New file", accelerator = "Ctrl + N", command = new_file)
fmenu.add_command(label = "Open file", accelerator = "Ctrl + O", command = open_file)
fmenu.add_command(label = "Save file", accelerator = "Ctrl + S", command = save_file)

afmenu = Menu(menubar, tearoff = False)
menubar.add_cascade(label = "About", menu = afmenu)
afmenu.add_command(label = "About app", command = app)
afmenu.add_command(label = "About author", command = author)


nfi = PhotoImage(file = "icons/newfile.gif")

sfi = PhotoImage(file = "icons/save.gif")

dfi = PhotoImage(file = "icons/undo.gif")

ofi = PhotoImage(file = "icons/openfile.gif")

emptylbl = Label(frm1, width = 1, bg = "#212223")
emptylbl.grid(row = 0, column = 0)

newfilebtn = Button(frm1, image = nfi, command = new_file, bg = "#161519")
newfilebtn.grid(row = 0, column = 1)

openfilebtn = Button(frm1, image = ofi, command = open_file, bg = "#161519")
openfilebtn.grid(row = 0, column = 2)

savefilebtn = Button (frm1, image = sfi, command = save_file, bg = "#161519")
savefilebtn.grid(row = 0, column = 3)

deletebtn = Button(frm1, image = dfi, command = delete, bg = "#161519")
deletebtn.grid(row = 0, column = 4)
txt = Text(win, bg = "#212223",fg = "silver")
txt.pack()

txt.bind("<Control-n>",new_file)
txt.bind("<Control-s>",save_file)
txt.bind("<Control-o>",open_file)

win.mainloop()

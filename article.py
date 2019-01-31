from tkinter import *
import requests, bs4,os
from tkinter import ttk as t
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
link = "https://tengrinews.kz/article/"
data = requests.get(link)
code = bs4.BeautifulSoup(data.text, "html.parser")
block = code.findAll("div", class_="block clearAfter")
data = code.findAll("div", class_="date") #print(data[0].text)
substr = code.findAll("span", class_="substr")
firsturl = "https://tengrinews.kz"

imgs = code.findAll("div", class_="block clearAfter")
for im in imgs:
      img1 = im.select("img")[0].get("src")
      img2 = im.select("img")[1].get("src")
      img3 = im.select("img")[2].get("src")
      img4 = im.select("img")[3].get("src")
      img5 = im.select("img")[4].get("src")
      img6 = im.select("img")[5].get("src")
      img7 = im.select("img")[6].get("src")

for blo in block:
      a1 = blo.select("a")[0].get('href')
      a2 = blo.select("a")[1].get('href')
      a3 = blo.select("a")[2].get('href')
      a4 = blo.select("a")[3].get('href')
      a5 = blo.select("a")[4].get('href')
      a6 = blo.select("a")[5].get('href')
      a7 = blo.select("a")[6].get('href')
      
      img1 = firsturl+blo.select("img")[0].get("src")
      data1 = data[0].text
      img2 = firsturl+blo.select("img")[1].get("src")
      data2 = data[1].text
      img3 = firsturl+blo.select("img")[2].get("src")
      data3 = data[2].text
      img4 = firsturl+blo.select("img")[3].get("src")
      data4 = data[3].text
      img5 = firsturl+blo.select("img")[4].get("src")
      data5 = data[4].text
      img6 = blo.select("img")[5].get("src")
      data6 = data[5].text
      img7 = blo.select("img")[6].get("src")
      data7 = data[6].text
      img8 = blo.select("img")[7].get("src")
      data8 = data[7].text

      p1 = blo.select("img")[0].get("alt")
      p2 = blo.select("img")[1].get("alt")
      p3 = blo.select("img")[2].get("alt")
      p4 = blo.select("img")[3].get("alt")
      p5 = blo.select("img")[4].get("alt")
      p6 = blo.select("img")[5].get("alt")
      p7 = blo.select("img")[6].get("alt")
      
an1 = substr[0].text
an2 = substr[1].text
an3 = substr[2].text
an4 = substr[3].text
an5 = substr[4].text
an6 = substr[5].text
an7 = substr[6].text



#listw.insert(END, a[2].text)

def show1():
      href1 = firsturl+a2
      data2 = requests.get(href1)
      code2 = bs4.BeautifulSoup(data2.text, "html.parser")
      div_text = code2.findAll("div", class_="text sharedText js-mediator-article")
      
      
      win2 = Tk()
      win2.geometry("800x500")
      win2.title(p2)

      scrollbar = Scrollbar(win2)
      scrollbar.pack( side = RIGHT, fill = Y )

  

      p1txt = Text(win2,font='Arial 14',bg = "#2c7f24",fg = "white",yscrollcommand = scrollbar.set)
      p1txt.pack()

      p1txt.insert(END, div_text[0].text)

      p1txt.pack( side = LEFT, fill = BOTH )
      scrollbar.config( command = p1txt.yview )
      
      win2.mainloop()
def show2():
      href1 = firsturl+a3
      data2 = requests.get(href1)
      code2 = bs4.BeautifulSoup(data2.text, "html.parser")
      div_text = code2.findAll("div", class_="text sharedText js-mediator-article")
      
      
      win2 = Tk()
      win2.geometry("800x500")
      win2.title(p3)

      scrollbar = Scrollbar(win2)
      scrollbar.pack( side = RIGHT, fill = Y )

  

      p1txt = Text(win2,font='Arial 14',bg = "#2c7f24",fg = "white",yscrollcommand = scrollbar.set)
      p1txt.pack()

      p1txt.insert(END, div_text[0].text)

      p1txt.pack( side = LEFT, fill = BOTH )
      scrollbar.config( command = p1txt.yview )
      
      win2.mainloop()

def show3():
      href1 = firsturl+a4
      data2 = requests.get(href1)
      code2 = bs4.BeautifulSoup(data2.text, "html.parser")
      div_text = code2.findAll("div", class_="text sharedText js-mediator-article")
      
      
      win2 = Tk()
      win2.geometry("800x500")
      win2.title(p4)

      scrollbar = Scrollbar(win2)
      scrollbar.pack( side = RIGHT, fill = Y )

  

      p1txt = Text(win2,font='Arial 14',bg = "#2c7f24",fg = "white",yscrollcommand = scrollbar.set)
      p1txt.pack()

      p1txt.insert(END, div_text[0].text)

      p1txt.pack( side = LEFT, fill = BOTH )
      scrollbar.config( command = p1txt.yview )
      
      win2.mainloop()

def show4():
      href1 = firsturl+a5
      data2 = requests.get(href1)
      code2 = bs4.BeautifulSoup(data2.text, "html.parser")
      div_text = code2.findAll("div", class_="text sharedText js-mediator-article")
      
      
      win2 = Tk()
      win2.geometry("800x500")
      win2.title(p5)

      scrollbar = Scrollbar(win2)
      scrollbar.pack( side = RIGHT, fill = Y )

  

      p1txt = Text(win2,font='Arial 14',bg = "#2c7f24",fg = "white",yscrollcommand = scrollbar.set)
      p1txt.pack()

      p1txt.insert(END, div_text[0].text)

      p1txt.pack( side = LEFT, fill = BOTH )
      scrollbar.config( command = p1txt.yview )
      
      win2.mainloop()
def show5():
      href1 = firsturl+a6
      data2 = requests.get(href1)
      code2 = bs4.BeautifulSoup(data2.text, "html.parser")
      div_text = code2.findAll("div", class_="text sharedText js-mediator-article")
      
      
      win2 = Tk()
      win2.geometry("800x500")
      win2.title(p6)

      scrollbar = Scrollbar(win2)
      scrollbar.pack( side = RIGHT, fill = Y )

  

      p1txt = Text(win2,font='Arial 14',bg = "#2c7f24",fg = "white",yscrollcommand = scrollbar.set)
      p1txt.pack()

      p1txt.insert(END, div_text[0].text)

      p1txt.pack( side = LEFT, fill = BOTH )
      scrollbar.config( command = p1txt.yview )
      
      win2.mainloop()
def show6():
      href1 = firsturl+a7
      data2 = requests.get(href1)
      code2 = bs4.BeautifulSoup(data2.text, "html.parser")
      div_text = code2.findAll("div", class_="text sharedText js-mediator-article")
      
      
      win2 = Tk()
      win2.geometry("800x500")
      win2.title(p7)

      scrollbar = Scrollbar(win2)
      scrollbar.pack( side = RIGHT, fill = Y )

  

      p1txt = Text(win2,font='Arial 14',bg = "#2c7f24",fg = "white",yscrollcommand = scrollbar.set)
      p1txt.pack()

      p1txt.insert(END, div_text[0].text)

      p1txt.pack( side = LEFT, fill = BOTH )
      scrollbar.config( command = p1txt.yview )
      
      win2.mainloop()
      
win = Tk()
win.geometry("1100x400")
win.title("Статьи")
win.config(bg = "#f7ea5b")

URL = img2
u = urlopen(URL)
raw_data = u.read()
u.close()

im = Image.open(BytesIO(raw_data))
photo1 = ImageTk.PhotoImage(im)

URL1 = img3
u1 = urlopen(URL1)
raw_data1 = u1.read()
u1.close()

im1 = Image.open(BytesIO(raw_data1))
photo2 = ImageTk.PhotoImage(im1)

URL2 = img4
u2 = urlopen(URL2)
raw_data2 = u2.read()
u2.close()

im2 = Image.open(BytesIO(raw_data2))
photo3 = ImageTk.PhotoImage(im2)

URL3 = img5
u3 = urlopen(URL3)
raw_data3 = u3.read()
u3.close()

im3 = Image.open(BytesIO(raw_data3))
photo4 = ImageTk.PhotoImage(im3)

URL4 = firsturl+img6
u4 = urlopen(URL4)
raw_data4 = u4.read()
u4.close()

im4 = Image.open(BytesIO(raw_data4))
photo5 = ImageTk.PhotoImage(im4)

URL5 = firsturl+img7
u5 = urlopen(URL5)
raw_data5 = u5.read()
u5.close()

im5 = Image.open(BytesIO(raw_data5))
photo6 = ImageTk.PhotoImage(im5)

URL6 = firsturl+img8
u6 = urlopen(URL6)
raw_data6 = u6.read()
u6.close()

im6 = Image.open(BytesIO(raw_data6))
photo7 = ImageTk.PhotoImage(im6)

my_img1 = Label(image = photo1)
my_img1.image = photo1
my_img1.grid(row = 0, column = 0, padx = 5, pady = 5)



datatxt1 = Label(win, text = data2, fg = "#5f6163", bg = "white")
datatxt1.grid(row = 1, column = 0, padx = 10, pady = 1)

p1txt = Text(win,bg = "#7f8229",fg = "white", width = 20, height = 6, font ="Arial 11")
p1txt.grid(row = 2, column = 0, padx = 10, pady = 1)

p1txt.insert(END,p2)

an1btn = Text(win, bg = "#2c7f24",fg = "white",width = 20, height = 6)
an1btn.grid(row = 3, column = 0, padx = 5, pady = 5)

an1btn.insert(END,an2)

readbtn1 = t.Button(win, text = "Прочитать!", command = show1)
readbtn1.grid(row = 4, column = 0, padx = 5, pady = 5)


my_img2 = Label(image = photo2)
my_img2.image = my_img2
my_img2.grid(row = 0, column = 1)

datatxt2 = Label(win, text = data3, fg = "#5f6163", bg = "white")
datatxt2.grid(row = 1, column = 1, padx = 10, pady = 1)

p2txt = Text(win,bg = "#7f8229",fg = "white", width = 20, height = 6,font ="Arial 11")
p2txt.grid(row = 2, column = 1, padx = 10, pady = 1)

p2txt.insert(END,p3)

an2btn = Text(win, bg = "#2c7f24",fg = "white",width = 20, height = 6)
an2btn.grid(row = 3, column = 1, padx = 5, pady = 5)

an2btn.insert(END,an3)

readbtn2 = t.Button(win, text = "Прочитать!", command = show2)
readbtn2.grid(row = 4, column = 1, padx = 5, pady = 5)

my_img3 = Label(image = photo3)
my_img3.image = my_img3
my_img3.grid(row = 0, column = 2)

datatxt3 = Label(win, text = data4, fg = "#5f6163", bg = "white")
datatxt3.grid(row = 1, column = 2, padx = 10, pady = 1)

p3txt = Text(win, width = 20, height = 6,bg = "#7f8229",fg = "white",font ="Arial 11")
p3txt.grid(row = 2, column = 2, padx = 10, pady = 1)

p3txt.insert(END,p4)

an3btn = Text(win, bg = "#2c7f24",fg = "white",width = 20, height = 6)
an3btn.grid(row = 3, column = 2, padx = 5, pady = 5)

an3btn.insert(END,an4)

readbtn3 = t.Button(win, text = "Прочитать!", command = show3)
readbtn3.grid(row = 4, column = 2, padx = 5, pady = 5)

my_img4 = Label(image = photo4)
my_img4.image = my_img4
my_img4.grid(row = 0, column = 3)

datatxt4 = Label(win, text = data5, fg = "#5f6163", bg = "white")
datatxt4.grid(row = 1, column = 3, padx = 10, pady = 1)

p4txt = Text(win,bg = "#7f8229",fg = "white",width = 20, height = 6,font ="Arial 11")
p4txt.grid(row = 2, column = 3, padx = 10, pady = 1)

p4txt.insert(END,p5)

an4btn = Text(win, bg = "#2c7f24",fg = "white",width = 20, height = 6)
an4btn.grid(row = 3, column = 3, padx = 5, pady = 5)

an4btn.insert(END,an5)

readbtn4 = t.Button(win, text = "Прочитать!", command = show4)
readbtn4.grid(row = 4, column = 3, padx = 5, pady = 5)

my_img5 = Label(image = photo5)
my_img5.image = my_img5
my_img5.grid(row = 0, column = 4)

datatxt5 = Label(win, text = data6, fg = "#5f6163", bg = "white")
datatxt5.grid(row = 1, column = 4, padx = 10, pady = 1)

p5txt = Text(win,bg = "#7f8229",fg = "white",width = 20, height = 6,font ="Arial 11")
p5txt.grid(row = 2, column = 4, padx = 10, pady = 1)

p5txt.insert(END,p6)

an5btn = Text(win, bg = "#2c7f24",fg = "white",width = 20, height = 6)
an5btn.grid(row = 3, column = 4, padx = 5, pady = 5)

an5btn.insert(END,an6)

readbtn5 = t.Button(win, text = "Прочитать!", command = show5)
readbtn5.grid(row = 4, column = 4, padx = 5, pady = 5)


my_img6 = Label(image = photo6)
my_img6.image = my_img6
my_img6.grid(row = 0, column = 5)

datatxt6 = Label(win, text = data7, fg = "#5f6163", bg = "white")
datatxt6.grid(row = 1, column = 5, padx = 10, pady = 1)

p6txt = Text(win,bg = "#7f8229",fg = "white",width = 20, height = 6,font ="Arial 11")
p6txt.grid(row = 2, column = 5, padx = 10, pady = 1)

p6txt.insert(END,p7)

an6btn = Text(win, bg = "#2c7f24",fg = "white",width = 20, height = 6)
an6btn.grid(row = 3, column = 5, padx = 5, pady = 5)

an6btn.insert(END,an7)

readbtn6 = t.Button(win, text = "Прочитать!", command = show6)
readbtn6.grid(row = 4, column = 5, padx = 5, pady = 5)

win.mainloop()


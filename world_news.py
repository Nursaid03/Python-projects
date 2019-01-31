from tkinter import *
from tkinter import ttk as t
import requests, bs4,os
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO

firstpage = "https://tengrinews.kz"
firsturl = "https://tengrinews.kz/world_news/"
data = requests.get(firsturl)
code = bs4.BeautifulSoup(data.text, "html.parser")

bignews = code.findAll("div", class_="h2")
bignewsdate = code.findAll("div", class_="date")

  
firstimg = code.findAll("div", class_="owl-carousel-news")
for first in firstimg:
  img1 = first.select("img")[0].get("src")

news_photos1 = code.findAll("div", class_="news clearAfter pl mb")[0]
img2 = news_photos1.select("div")[0].get("data-w320")
news_photos2 = code.findAll("div", class_="news clearAfter pl mb")[1]
img3 = news_photos2.select("div")[0].get("data-w320")
news_photos3 = code.findAll("div", class_="news clearAfter pl mb")[2]
img4 = news_photos3.select("div")[0].get("data-w320")
news_photos4 = code.findAll("div", class_="news clearAfter pl mb")[3]
img5 = news_photos4.select("div")[0].get("data-w320")
news_photos5 = code.findAll("div", class_="news clearAfter pl mb")[4]
img6 = news_photos5.select("div")[0].get("data-w320")
news_photos6 = code.findAll("div", class_="news clearAfter pl mb")[5]
img7 = news_photos6.select("div")[0].get("data-w320")
  

bignewsp1 = code.findAll("span", class_="name")
news1 = bignewsp1[0].text
news2 = bignewsp1[1].text
news3 = bignewsp1[2].text
news4 = bignewsp1[3].text
news5 = bignewsp1[4].text
news6 = bignewsp1[5].text

date = code.findAll("span", class_="date")
bigdate = bignewsdate[0].text
date1 = date[0].text
date2 = date[1].text
date3 = date[2].text
date4 = date[3].text
date5 = date[4].text
date6 = date[5].text

p1news = code.findAll("div", class_="tab_content rubric-page clearAfter")
for p1 in p1news:
  bignewsurl = p1.select("a")[0].get("href")
  url1 = p1.select("a")[2].get("href")
  url2 = p1.select("a")[3].get("href")
  url3 = p1.select("a")[4].get("href")
  url4 = p1.select("a")[5].get("href")
  url5 = p1.select("a")[6].get("href")
  url6 = p1.select("a")[7].get("href")


def show1():
  news1url = firstpage+bignewsurl
  data = requests.get(news1url)
  code = bs4.BeautifulSoup(data.text, "html.parser")
  sharedText = code.findAll("div", class_="text sharedText js-mediator-article")

  win2 = Tk()
  win2.geometry("700x450")
  win2.title(bignews[0].text)
  win2.config(bg = "#f7ea5b")

  scrollbar = Scrollbar(win2)
  scrollbar.pack( side = RIGHT, fill = Y )

  frm2 = Frame(win2, bg ="#e5e2b0")
  frm2.pack()

  p1txt = Text(win2,font='Arial 14',bg = "#7f8229",fg = "white",yscrollcommand = scrollbar.set)
  p1txt.pack()

  p1txt.insert(END, sharedText[0].text)

  p1txt.pack( side = LEFT, fill = BOTH )
  scrollbar.config( command = p1txt.yview )
      
  win2.mainloop()

def show2():
  news1url = firstpage+url1
  data = requests.get(news1url)
  code = bs4.BeautifulSoup(data.text, "html.parser")
  sharedText = code.findAll("div", class_="text sharedText js-mediator-article")

  win2 = Tk()
  win2.geometry("700x450")
  win2.title(news1)
  win2.config(bg = "#f7ea5b")

  scrollbar = Scrollbar(win2)
  scrollbar.pack( side = RIGHT, fill = Y )

  frm2 = Frame(win2, bg ="#e5e2b0")
  frm2.pack()

  p1txt = Text(win2,font='Arial 14',bg = "#2c7f24",fg = "white",yscrollcommand = scrollbar.set)
  p1txt.pack()

  p1txt.insert(END, sharedText[0].text)

  p1txt.pack( side = LEFT, fill = BOTH )
  scrollbar.config( command = p1txt.yview )
      
  win2.mainloop()

def show3():
  news1url = firstpage+url2
  data = requests.get(news1url)
  code = bs4.BeautifulSoup(data.text, "html.parser")
  sharedText = code.findAll("div", class_="text sharedText js-mediator-article")

  win2 = Tk()
  win2.geometry("700x450")
  win2.title(news2)
  win2.config(bg = "#f7ea5b")

  scrollbar = Scrollbar(win2)
  scrollbar.pack( side = RIGHT, fill = Y )

  frm2 = Frame(win2, bg ="#e5e2b0")
  frm2.pack()

  p1txt = Text(win2,font='Arial 14',bg = "#2c7f24",fg = "white",yscrollcommand = scrollbar.set)
  p1txt.pack()

  p1txt.insert(END, sharedText[0].text)

  p1txt.pack( side = LEFT, fill = BOTH )
  scrollbar.config( command = p1txt.yview )
      
  win2.mainloop()

def show4():
  news1url = firstpage+url3
  data = requests.get(news1url)
  code = bs4.BeautifulSoup(data.text, "html.parser")
  sharedText = code.findAll("div", class_="text sharedText js-mediator-article")

  win2 = Tk()
  win2.geometry("700x450")
  win2.title(news3)
  win2.config(bg = "#f7ea5b")

  scrollbar = Scrollbar(win2)
  scrollbar.pack( side = RIGHT, fill = Y )

  frm2 = Frame(win2, bg ="#e5e2b0")
  frm2.pack()

  p1txt = Text(win2,font='Arial 14',bg = "#2c7f24",fg = "white",yscrollcommand = scrollbar.set)
  p1txt.pack()

  p1txt.insert(END, sharedText[0].text)

  p1txt.pack( side = LEFT, fill = BOTH )
  scrollbar.config( command = p1txt.yview )
      
  win2.mainloop()

def show5():
  news1url = firstpage+url4
  data = requests.get(news1url)
  code = bs4.BeautifulSoup(data.text, "html.parser")
  sharedText = code.findAll("div", class_="text sharedText js-mediator-article")
  div_txt = code.findAll("div", class_="txt")

  win2 = Tk()
  win2.geometry("700x450")
  win2.title(news4)
  win2.config(bg = "#f7ea5b")

  scrollbar = Scrollbar(win2)
  scrollbar.pack( side = RIGHT, fill = Y )

  frm2 = Frame(win2, bg ="#e5e2b0")
  frm2.pack()

  p1txt = Text(win2,font='Arial 14',bg = "#2c7f24",fg = "white",yscrollcommand = scrollbar.set)
  p1txt.pack()

  p1txt.insert(END, sharedText[0].text)

  p1txt.pack( side = LEFT, fill = BOTH )
  scrollbar.config( command = p1txt.yview )
      
  win2.mainloop()

def show6():
  news1url = firstpage+url5
  data = requests.get(news1url)
  code = bs4.BeautifulSoup(data.text, "html.parser")
  sharedText = code.findAll("div", class_="text sharedText js-mediator-article")

  win2 = Tk()
  win2.geometry("700x450")
  win2.title(news5)
  win2.config(bg = "#f7ea5b")

  scrollbar = Scrollbar(win2)
  scrollbar.pack( side = RIGHT, fill = Y )

  frm2 = Frame(win2, bg ="#e5e2b0")
  frm2.pack()

  p1txt = Text(win2,font='Arial 14',bg = "#2c7f24",fg = "white",yscrollcommand = scrollbar.set)
  p1txt.pack()

  p1txt.insert(END, sharedText[0].text)

  p1txt.pack( side = LEFT, fill = BOTH )
  scrollbar.config( command = p1txt.yview )
      
  win2.mainloop()

def show7():
  news1url = firstpage+url6
  data = requests.get(news1url)
  code = bs4.BeautifulSoup(data.text, "html.parser")
  sharedText = code.findAll("div", class_="text sharedText js-mediator-article")
  win2 = Tk()
  win2.geometry("700x450")
  win2.title(news6)
  win2.config(bg = "#f7ea5b")

  scrollbar = Scrollbar(win2)
  scrollbar.pack( side = RIGHT, fill = Y )

  frm2 = Frame(win2, bg ="#e5e2b0")
  frm2.pack()

  p1txt = Text(win2,font='Arial 14',bg = "#2c7f24",fg = "white",yscrollcommand = scrollbar.set)
  p1txt.pack()

  p1txt.insert(END, sharedText[0].text)

  p1txt.pack( side = LEFT, fill = BOTH )
  scrollbar.config( command = p1txt.yview )
      
  win2.mainloop()

win = Tk()
win.geometry("1240x800")
win.title("Новости мира")
win.config(bg = "#f7ea5b")

URL = firstpage+img1
u = urlopen(URL)
raw_data = u.read()
u.close()

im = Image.open(BytesIO(raw_data))
photo1 = ImageTk.PhotoImage(im)

URL1 = firstpage+img2
u1 = urlopen(URL1)
raw_data1 = u1.read()
u1.close()

im1 = Image.open(BytesIO(raw_data1))
photo2 = ImageTk.PhotoImage(im1)

URL2 = firstpage+img3
u2 = urlopen(URL2)
raw_data2 = u2.read()
u2.close()

im2 = Image.open(BytesIO(raw_data2))
photo3 = ImageTk.PhotoImage(im2)

URL3 = firstpage+img4
u3 = urlopen(URL3)
raw_data3 = u3.read()
u3.close()

im3 = Image.open(BytesIO(raw_data3))
photo4 = ImageTk.PhotoImage(im3)

URL4 = firstpage+img5
u4 = urlopen(URL4)
raw_data4 = u4.read()
u4.close()

im4 = Image.open(BytesIO(raw_data4))
photo5 = ImageTk.PhotoImage(im4)

URL5 = firstpage+img6
u5 = urlopen(URL5)
raw_data5 = u5.read()
u5.close()

im5 = Image.open(BytesIO(raw_data5))
photo6 = ImageTk.PhotoImage(im5)

URL6 = firstpage+img7
u6 = urlopen(URL6)
raw_data6 = u6.read()
u6.close()

im6 = Image.open(BytesIO(raw_data6))
photo7 = ImageTk.PhotoImage(im6)



my_img1 = Label(image = photo1)
my_img1.image = photo1
my_img1.grid(row = 0, column = 0, padx = 10, pady = 5)


datatxt1 = Label(win, text = bigdate, fg = "#5f6163", bg = "white")
datatxt1.grid(row = 1, column = 0, padx = 10, pady = 3)



p1txt1 = Text(win,bg = "#7f8229",fg = "white", width = 20, height = 4, font = "Arial 12")
p1txt1.grid(row = 2, column = 0, padx = 10, pady = 1)
p1txt1.insert(END,bignews[0].text)

readbtn1 = t.Button(win, text = "Прочитать!", command = show1)
readbtn1.grid(row = 3, column = 0, padx = 5, pady = 5)

my_img2 = Label(image = photo2)
my_img2.image = photo2
my_img2.grid(row = 0, column = 1)

datatxt2 = Label(win, text = date1, fg = "#5f6163", bg = "white")
datatxt2.grid(row = 1, column = 1, padx = 5, pady = 3)

p1txt2 = Text(win,bg = "#2c7f24",fg = "white", width = 20, height = 4,font = "Arial 12")
p1txt2.grid(row = 2, column = 1, padx = 1, pady = 1)
p1txt2.insert(END,news1)


readbtn2 = t.Button(win, text = "Прочитать!", command = show2)
readbtn2.grid(row = 3, column = 1, padx = 5, pady = 5)

my_img3 = Label(image = photo3)
my_img3.image = photo3
my_img3.grid(row = 0, column = 2)

datatxt3 = Label(win, text = date2, fg = "#5f6163", bg = "white")
datatxt3.grid(row = 1, column = 2, padx = 10, pady = 3)

p1txt3 = Text(win,bg = "#2c7f24",fg = "white", width = 20, height = 4,font = "Arial 12")
p1txt3.grid(row = 2, column = 2, padx = 10, pady = 1)
p1txt3.insert(END,news2)


readbtn3 = t.Button(win, text = "Прочитать!", command = show3)
readbtn3.grid(row = 3, column = 2, padx = 5, pady = 5)

my_img4 = Label(image = photo4)
my_img4.image = photo4
my_img4.grid(row = 0, column = 3)

datatxt4 = Label(win, text = date3, fg = "#5f6163", bg = "white")
datatxt4.grid(row = 1, column = 3, padx = 10, pady = 3)

p1txt4 = Text(win,bg = "#2c7f24",fg = "white", width = 20, height = 4,font = "Arial 12")
p1txt4.grid(row = 2, column = 3, padx = 10, pady = 1)
p1txt4.insert(END,news3)

readbtn4 = t.Button(win, text = "Прочитать!", command = show4)
readbtn4.grid(row = 3, column = 3, padx = 5, pady = 5)

my_img5 = Label(image = photo5)
my_img5.image = photo5
my_img5.grid(row = 4, column = 1)

datatxt5 = Label(win, text = date4, fg = "#5f6163", bg = "white")
datatxt5.grid(row = 5, column = 1, padx = 10, pady = 3)

p1txt5 = Text(win,bg = "#2c7f24",fg = "white", width = 20, height = 4,font = "Arial 12")
p1txt5.grid(row = 6, column = 1, padx = 10, pady = 1)
p1txt5.insert(END,news4)

readbtn5 = t.Button(win, text = "Прочитать!", command = show5)
readbtn5.grid(row = 7, column = 1, padx = 5, pady = 5)

my_img6 = Label(image = photo6)
my_img6.image = photo6
my_img6.grid(row = 4, column = 2)

datatxt6 = Label(win, text = date5, fg = "#5f6163", bg = "white")
datatxt6.grid(row = 5, column = 2, padx = 10, pady = 3)

p1txt6 = Text(win,bg = "#2c7f24",fg = "white", width = 20, height = 4,font = "Arial 12")
p1txt6.grid(row = 6, column = 2, padx = 10, pady = 1)
p1txt6.insert(END,news5)

readbtn6 = t.Button(win, text = "Прочитать!", command = show6)
readbtn6.grid(row = 7, column = 2, padx = 5, pady = 5)

my_img7 = Label(image = photo7)
my_img7.image = photo7
my_img7.grid(row = 4, column = 3)

datatxt7 = Label(win, text = date6, fg = "#5f6163", bg = "white")
datatxt7.grid(row = 5, column = 3, padx = 10, pady = 3)

p1txt7 = Text(win,bg = "#2c7f24",fg = "white", width = 20, height = 4,font = "Arial 12")
p1txt7.grid(row = 6, column = 3, padx = 10, pady = 1)
p1txt7.insert(END,news6)

readbtn7 = t.Button(win, text = "Прочитать!", command = show7)
readbtn7.grid(row = 7, column = 3, padx = 6, pady = 5)

win.mainloop()



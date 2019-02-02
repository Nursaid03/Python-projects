from tkinter import *
from tkinter import ttk as t
import requests, bs4,os
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO

def hot_news():
  os.system("C:\\Users\\Нурсаид\\Downloads\\Проект\\hot_news.py")
def kazakhstan_news():
  os.system("C:\\Users\\Нурсаид\\Downloads\\Проект\\kazakhstan_news.py")
def world_news():
  os.system("C:\\Users\\Нурсаид\\Downloads\\Проект\\world_news.py")
def economic_news():
  os.system("C:\\Users\\Нурсаид\\Downloads\\Проект\\economic.py")
def accidents_news():
  os.system("C:\\Users\\Нурсаид\\Downloads\\Проект\\accidents.py")
def article_news():
  os.system("C:\\Users\\Нурсаид\\Downloads\\Проект\\article.py")
def tech_news():
  os.system("C:\\Users\\Нурсаид\\Downloads\\Проект\\tech.py")
def culture_news():
  os.system("C:\\Users\\Нурсаид\\Downloads\\Проект\\culture.py")
def sports_news():
  os.system("C:\\Users\\Нурсаид\\Downloads\\Проект\\sports.py")
def life_news():
  os.system("C:\\Users\\Нурсаид\\Downloads\\Проект\\life.py")
firsturl = "https://tengrinews.kz"
data = requests.get(firsturl)
code = bs4.BeautifulSoup(data.text, "html.parser")



  
firstimg = code.findAll("div", class_="owl-carousel-news")
for first in firstimg:
  img1 = first.select("img")[0].get("data-w360")
  
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


news1 = code.findAll("div", class_="h2")[0].text
news_list = code.findAll("span", class_="name")
news2 = news_list[0].text
news3 = news_list[1].text
news4 = news_list[2].text
news5 = news_list[3].text
news6 = news_list[4].text
news7 = news_list[5].text


date_list = code.findAll("span", class_="date")
date1 = code.findAll("div", class_="date")[0].text
date2 = date_list[0].text
date3 = date_list[1].text
date4 = date_list[2].text
date5 = date_list[3].text
date6 = date_list[4].text
date7 = date_list[5].text

url_list = code.findAll("div", class_="tab_content rubric-page clearAfter")
for p1 in url_list:
  url1 = p1.select("a")[0].get("href")
  url2 = p1.select("a")[2].get("href")
  url3 = p1.select("a")[3].get("href")
  url4 = p1.select("a")[4].get("href")
  url5 = p1.select("a")[5].get("href")
  url6 = p1.select("a")[6].get("href")
  url7 = p1.select("a")[7].get("href")


class News:

	def __init__(self,photo,date,news,url):
		self.photo = firsturl + photo
		self.date = date
		self.news = news
		self.url = firsturl + url

	def photo_url(self,img):
		self.img = img
		URL = self.photo
		u = urlopen(URL)
		raw_data = u.read()
		u.close()
		im = Image.open(BytesIO(raw_data))
		img = ImageTk.PhotoImage(im)

	def open_news(self):
		news_url = self.url
		data = requests.get(news_url)
		code = bs4.BeautifulSoup(data.text, "html.parser")
		sharedText = code.findAll("div", class_="text sharedText js-mediator-article")

		windows = Tk()
		windows.geometry("700x450")
		windows.title(self.news)
		windows.config(bg = "#f7ea5b")

		scrollbar = Scrollbar(windows)
		scrollbar.pack( side = RIGHT, fill = Y )
		frm2 = Frame(windows, bg ="#e5e2b0")
		frm2.pack()

		p1txt = Text(windows,font='Arial 14',bg = "#2c7f24",fg = "white",yscrollcommand = scrollbar.set)
		p1txt.pack()
		p1txt.insert(END, sharedText[0].text)

		p1txt.pack( side = LEFT, fill = BOTH )
		scrollbar.config( command = p1txt.yview )      
		windows.mainloop()

first_news = News(img1,date1,news1,url1)
second_news = News(img2,date2,news2,url2)
third_news = News(img3,date3,news3,url3)
fourth_news = News(img4,date4,news4,url4)
fifth_news = News(img5,date5,news5,url5)
sixth_news = News(img6,date6,news6,url6)
seventh_news = News(img7,date7,news7,url7)

win = Tk()
win.geometry("1040x600")
win.title("Tengri News")
win.config(bg = "white")

menubar = Menu()
win.config(menu = menubar)

news = Menu(menubar, tearoff = False)
menubar.add_cascade(label = "Новости", menu = news)
news.add_command(label = "Новости Казахстана", command = kazakhstan_news)
news.add_command(label = "Новости мира", command = world_news)
news.add_command(label = "Горячие Новости", command = hot_news)

economic = Menu(menubar, tearoff = False)
menubar.add_cascade(label = "Экономика", command = economic_news)

accidents = Menu(menubar, tearoff = False)
menubar.add_cascade(label = "Происшествия", command = accidents_news)

article = Menu(menubar, tearoff = False)
menubar.add_cascade(label = "Статьи", command = article_news)

tech = Menu(menubar, tearoff = False)
menubar.add_cascade(label = "Технологии", command = tech_news)

culture = Menu(menubar, tearoff = False)
menubar.add_cascade(label = "Культура", command = culture_news)

sports = Menu(menubar, tearoff = False)
menubar.add_cascade(label = "Спорт", command = sports_news)

life = Menu(menubar, tearoff = False)
menubar.add_cascade(label = "Жизнь", command = life_news)


# my_img1 = Label(image = first_news.photo_url(first_news.photo))
# my_img1.image = first_news.photo_url(first_news.photo)
# my_img1.grid(row = 0, column = 0, padx = 10, pady = 5)


datatxt1 = Label(win, text = first_news.date, fg = "#5f6163", bg = "white")
datatxt1.grid(row = 1, column = 0, padx = 10, pady = 3)

p1txt1 = Text(win,bg = "#2c7f24",fg = "white", width = 20, height = 4, font = "Arial 12")
p1txt1.grid(row = 2, column = 0, padx = 10, pady = 1)
p1txt1.insert(END,first_news.news)

readbtn1 = t.Button(win, text = "Прочитать!", command = first_news.open_news)
readbtn1.grid(row = 3, column = 0, padx = 5, pady = 5)

# my_img2 = Label(image = photo2)
# my_img2.image = photo2
# my_img2.grid(row = 0, column = 1)

datatxt2 = Label(win, text = second_news.date, fg = "#5f6163", bg = "white")
datatxt2.grid(row = 1, column = 1, padx = 5, pady = 3)

p1txt2 = Text(win,bg = "#2c7f24",fg = "white", width = 20, height = 4,font = "Arial 12")
p1txt2.grid(row = 2, column = 1, padx = 1, pady = 1)
p1txt2.insert(END,second_news.news)


readbtn2 = t.Button(win, text = "Прочитать!", command = second_news.open_news)
readbtn2.grid(row = 3, column = 1, padx = 5, pady = 5)

# my_img3 = Label(image = photo3)
# my_img3.image = photo3
# my_img3.grid(row = 0, column = 2)

datatxt3 = Label(win, text = third_news.date, fg = "#5f6163", bg = "white")
datatxt3.grid(row = 1, column = 2, padx = 10, pady = 3)

p1txt3 = Text(win,bg = "#2c7f24",fg = "white", width = 20, height = 4,font = "Arial 12")
p1txt3.grid(row = 2, column = 2, padx = 10, pady = 1)
p1txt3.insert(END,third_news.news)


readbtn3 = t.Button(win, text = "Прочитать!", command = third_news.open_news)
readbtn3.grid(row = 3, column = 2, padx = 5, pady = 5)

# my_img4 = Label(image = photo4)
# my_img4.image = photo4
# my_img4.grid(row = 0, column = 3)

datatxt4 = Label(win, text = fourth_news.date, fg = "#5f6163", bg = "white")
datatxt4.grid(row = 1, column = 3, padx = 10, pady = 3)

p1txt4 = Text(win,bg = "#2c7f24",fg = "white", width = 20, height = 4,font = "Arial 12")
p1txt4.grid(row = 2, column = 3, padx = 10, pady = 1)
p1txt4.insert(END,fourth_news.news)

readbtn4 = t.Button(win, text = "Прочитать!", command = fourth_news.open_news)
readbtn4.grid(row = 3, column = 3, padx = 5, pady = 5)

# my_img5 = Label(image = photo5)
# my_img5.image = photo5
# my_img5.grid(row = 4, column = 0)

datatxt5 = Label(win, text = fifth_news.date, fg = "#5f6163", bg = "white")
datatxt5.grid(row = 5, column = 0, padx = 10, pady = 3)

p1txt5 = Text(win,bg = "#2c7f24",fg = "white", width = 20, height = 4,font = "Arial 12")
p1txt5.grid(row = 6, column = 0, padx = 10, pady = 1)
p1txt5.insert(END,fifth_news.news)

readbtn5 = t.Button(win, text = "Прочитать!", command = fifth_news.open_news)
readbtn5.grid(row = 7, column = 0, padx = 5, pady = 5)

# my_img6 = Label(image = photo6)
# my_img6.image = photo6
# my_img6.grid(row = 4, column = 1)

datatxt6 = Label(win, text = sixth_news.date, fg = "#5f6163", bg = "white")
datatxt6.grid(row = 5, column = 1, padx = 10, pady = 3)

p1txt6 = Text(win,bg = "#2c7f24",fg = "white", width = 20, height = 4,font = "Arial 12")
p1txt6.grid(row = 6, column = 1, padx = 10, pady = 1)
p1txt6.insert(END,sixth_news.news)

readbtn6 = t.Button(win, text = "Прочитать!", command = sixth_news.open_news)
readbtn6.grid(row = 7, column = 1, padx = 5, pady = 5)

# my_img7 = Label(image = photo7)
# my_img7.image = photo7
# my_img7.grid(row = 4, column = 2)

datatxt7 = Label(win, text = seventh_news.date, fg = "#5f6163", bg = "white")
datatxt7.grid(row = 5, column = 2, padx = 10, pady = 3)

p1txt7 = Text(win,bg = "#2c7f24",fg = "white", width = 20, height = 4,font = "Arial 12")
p1txt7.grid(row = 6, column = 2, padx = 10, pady = 1)
p1txt7.insert(END,seventh_news.news)

readbtn7 = t.Button(win, text = "Прочитать!", command = seventh_news.open_news)
readbtn7.grid(row = 7, column = 2, padx = 6, pady = 5)

win.mainloop()

import backend
from tkinter import *
import pyttsx3
from tkinter import messagebox
from PIL import ImageTk, Image
from difflib import get_close_matches

def go(event):
    global meaning_text
    index = list.curselection()[0]
    meaning_text = list.get(index)

def bookmark_command():
    backend.insert(word_text.get(), meaning_text)

def speak_command():
    engine1 = pyttsx3.init()
    engine1.say(word_text.get())
    engine1.runAndWait()

    engine2 = pyttsx3.init()
    engine2.say(meaning_text)
    engine2.runAndWait()

def add_command():
    top = Toplevel()

    top.geometry("600x350")
    top.resizable(0,0)
    top.title("Add Keyword")
    top.iconbitmap("icon\dictionary.ico")

    canv2 = Canvas(top, width=80, height=80, bg='white')
    canv2.pack(expand = True, fill = "both")

    img = ImageTk.PhotoImage(Image.open("add.jpg"))  # PIL solution
    canv2.create_image(5, 80, image=img)

    label = Label(canv2,
    text = "Enter word ",
    height = 2,
    width = 25)
    label.place(x = 20 , y = 20)

    w = StringVar()
    e1 = Entry(canv2,
    textvariable = w,
    width = 25,
    font = ("Verdana",13))
    e1.place(x = 230 , y = 25)

    label1 = Label(canv2,
    text = "Enter meaning",
    height = 2,
    width = 25)
    label1.place(x = 20 , y = 80)

    m = StringVar()
    e2 = Entry(canv2,
    textvariable = m,
    width = 25,
    font = ("Verdana",13))
    e2.place(x = 230 , y = 85)

    button = Button(canv2,
    text = "Add to my wordlist",
    height = 2,
    width = 20,
    relief = "solid",
    bd=2,
    command = lambda: backend.insert(w.get(), m.get()))
    button.place(x = 120 , y = 170)

    button = Button(canv2,
    text = "Quit",
    height = 2,
    width = 20,
    relief = "solid",
    bd=2,
    command = lambda: top.destroy())
    button.place(x = 320 , y = 170)

    top.mainloop()

def search_command():
    list.delete(0,END)
    for row in backend.search(word_text.get()):
        list.insert(END, row)

def delete_command():
    backend.delete(selected_row[0])

def view_command():

    def get_selected_row(event):
        global selected_row
        index = list1.curselection()[0]
        selected_row = list1.get(index)

    def get_selected_search(event):
        global selected_search
        index = list2.curselection()[0]
        selected_search = list2.get(index)

    def search_command_db():
        list2.delete(0,END)
        for row in backend.search_db(word_db.get()):
            list2.insert(END, row)

    def speak_command_db():
        engine1 = pyttsx3.init()
        engine1.say(word_db.get())
        engine1.runAndWait()

        engine2 = pyttsx3.init()
        engine2.say(selected_search)
        engine2.runAndWait()

    def refresh_command():
        list1.delete(0,END)
        for row in backend.view():
            list1.insert(END, row)

    top = Toplevel()

    top.geometry("750x550")
    top.resizable(0,0)
    top.title("View")
    top.iconbitmap("icon\dictionary.ico")

    canv1 = Canvas(top, width=60, height=60, bg='white')
    canv1.pack(expand = True, fill = "both")

    img = ImageTk.PhotoImage(Image.open("add.jpg"))  # PIL solution
    canv1.create_image(60, 280, image=img)

    list1 = Listbox(canv1, height = 15, width = 75)
    list1.place(x=80, y=280)

    list2 = Listbox(canv1, height = 5, width = 75)
    list2.place(x=80, y=120)

    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)

    list1.bind('<<ListboxSelect>>',get_selected_row)
    list2.bind('<<ListboxSelect>>',get_selected_search)

    label1 = Label(canv1,
    text = "Search: ",
    height = 2,
    anchor = "w")
    label1.place(x=10,y=52)

    label2 = Label(canv1,
    text = "Database: ",
    height = 2,
    anchor = "w")
    label2.place(x=10,y=240)

    word_db = StringVar()
    e2 = Entry(canv1,
    textvariable = word_db,
    width = 30,
    font = ("Verdana",13))
    e2.place(x=80, y=60)

    search_btn2 = PhotoImage(file = 'icon\mag_glass.png')
    search_label2 = Label(image = search_btn)

    button = Button(canv1,
    image = search_btn2,
    borderwidth = 0,
    height = 2,
    width = 20,
    relief = "solid",
    bd=2,
    command= search_command_db)
    button.place(x=430, y=50, height = 40, width = 40)

    speak_btn2 = PhotoImage(file = 'icon\speakers.png')
    speak_label2 = Label(image = speak_btn2)

    button = Button(canv1,
    image = speak_btn2,
    borderwidth = 0,
    height = 2,
    width = 20,
    relief = "solid",
    bd=2,
    command= speak_command_db)
    button.place(x=490, y=50, height = 40, width = 40)

    button = Button(canv1,
    text = "Delete in Vocab",
    height = 2,
    width = 20,
    relief = "solid",
    bd=2,
    command = delete_command)
    button.place(x=570,y=280)

    button = Button(canv1,
    text = "Refresh",
    height = 2,
    width = 20,
    relief = "solid",
    bd=2,
    command = refresh_command)
    button.place(x=570,y=350)

    button = Button(canv1,
    text = "Quit",
    height = 2,
    width = 20,
    relief = "solid",
    bd=2,
    command = lambda: top.destroy())
    button.place(x=570,y=420)

    top.mainloop()

def info_A():
    messagebox.showinfo("About Application", "It is an offline Python GUI application which has all the basic features that a dictionary software must have. \nYou can search meaning of a word which is parsed from the JSON file, bookmark it in your own database, add your own word with its meaning, and can delete the existing word from the database. \n\nThe application also has text-to-speech feature to pronounce the difficult word and can read the selected meaning for you.\n\nThis application also serves the purpose of maintaining your own glossary with its personal database feature. One can use this application to learn new words and can save them for future reference. Searching and text-to-speech feature is also available with database.")

def info_D():
    messagebox.showinfo("About Developer", "Hello!, My name is Tushar Malhotra, I am the developer of this application.\n\nRoll number: 42513202718 | CSE-2")


root = Tk()

root.geometry("1050x600")
root.resizable(0,0)
root.title("Dictionary")
root.iconbitmap("icon\dictionary.ico")

canv = Canvas(root, width=80, height=80, bg='white')
canv.pack(expand = True, fill = "both")

img = ImageTk.PhotoImage(Image.open("add.jpg"))  # PIL solution
canv.create_image(400, 280, image=img)
canv.create_text(215,50, text = "Dictionary", font=("Lucida Handwriting",48))
canv.create_text(525,80, text = "...your helping hand", font=("Lucida Handwriting",15))


label = Label(canv,
text = "Enter your word to search",
height = 2,
width = 25)
label.place(x=350,y=150)

word_text = StringVar()

e1 = Entry(canv,
textvariable = word_text,
width = 25,
font = ("Verdana",13))
e1.place(x=570, y=150)

label1 = Label(canv,
text = "Meaning",
height = 2,
width = 20)
label1.place(x=350,y=240)

xScroll = Scrollbar(canv, orient=HORIZONTAL)

list = Listbox(canv,
height = 10,
width = 46,
xscrollcommand=xScroll.set)
list.bind('<<ListboxSelect>>',go)

xScroll.config(command=list.xview)
xScroll.pack(side=BOTTOM, fill=X)

list.place(x=570,y=240)

search_btn = PhotoImage(file = 'icon\mag_glass.png')
search_label = Label(image = search_btn)

button = Button(canv,
image = search_btn,
borderwidth = 0,
height = 2,
width = 20,
relief = "solid",
bd=2,
command= search_command)
button.place(x=890, y=140, height = 40, width = 40)

speak_btn = PhotoImage(file = 'icon\speakers.png')
speak_label = Label(image = speak_btn)

button = Button(canv,
image = speak_btn,
borderwidth = 0,
height = 2,
width = 20,
relief = "solid",
bd=2,
command= speak_command)
button.place(x=970, y=140, height = 40, width = 40)

button = Button(canv,
text = "Bookmark",
height = 2,
width = 20,
relief = "solid",
bd=2,
command= bookmark_command)
button.place(x=880,y=240)

button = Button(canv,
text = "Add in Vocab",
height = 2,
width = 20,
relief = "solid",
bd=2,
command = add_command)
button.place(x=880,y=302)

button = Button(canv,
text = "View All in Vocab",
height = 2, width = 20,
relief = "solid",
bd=2,
command = view_command)
button.place(x=880,y=363)

button = Button(canv,
text = "Quit",
height = 2,
width = 20,
relief = "solid",
bd=2,
command = lambda: root.destroy())
button.place(x=880,y=485)


menubar = Menu(canv)
file = Menu(menubar, tearoff=0, activeborderwidth=5)
file.add_command(label="Add", command= add_command)
file.add_command(label="Bookmark", command= bookmark_command)
file.add_command(label="View", command= view_command)
file.add_separator()
file.add_command(label="Quit", command= lambda: root.destroy())
menubar.add_cascade(label="File", menu=file)

help = Menu(menubar, tearoff=0, activeborderwidth=5, relief = "solid")
help.add_command(label="About the Application", command = info_A)
help.add_command(label="About the Developer", command = info_D)
menubar.add_cascade(label="Help", menu=help)

root.config(menu=menubar)

root.mainloop()

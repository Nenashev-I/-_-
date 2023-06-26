from tkinter import *

import random
import tkinter.messagebox
from tkinter import Frame

window = Tk()

window.title("-_-",) #Окно
window.geometry("300x220") #Размер окна


canvas = Canvas(height=290, width=210,) #Холст
canvas.pack()

frame = Frame(bg="#696969") #Рамка
frame.place(relx=0, rely=0, relheight=1, relwidth=1)

title1 = Label(frame, text="Какой пост хотите написать?", bg="#696969", font=('Helvetica', 15))
title1.pack()
title1.place(relx=0.5, rely=0.1, anchor='center')
title2 = Label(frame, text="Грустный", bg="#696969", font=20)
title2.pack()
title2.place(relx=0.2, rely=0.37, anchor='center')
title3 = Label(frame, text="Нейтральный", bg="#696969", font=20)
title3.pack()
title3.place(relx=0.8, rely=0.37, anchor='center')
title3 = Label(frame, text="Весёлый", bg="#696969", font=20)
title3.pack()
title3.place(relx=0.5, rely=0.37, anchor='center')

def create_window1():
    canvass = Canvas(height=200, width=200, )  # Холст
    canvass.pack()

    frame0 = Frame(bg="#696969")  # Рамка
    frame0.place(relx=0, rely=0, relheight=1, relwidth=1)

    title10 = Label(frame0, text="Ваш пост написан", bg="#696969", font=20)
    title10.pack()
    title10.place(relx=0.5, rely=0.5, anchor='center')
    def click():
        commentTroll = ['Что за бред сумашедшего я сейчас прочитал', 'Удали аккаунт', 'Емае ну дает']
        commentMini = ['Звони скорее в психушку, я его нашел', 'За тобой выехали', 'Давай встретимся обсудим, ауф']
        commentCasl = ['Ну что вы на человека накинулись, обычное дело, с кем не бывает?',
                       'К чему агрессия, он просто написал, что думал', 'Судите себя, а не других']
        commentExtra = ['Всё супер, давай общаться', 'Классно не хочешь повторить это вместе',
                        'Никого не слушай,  всегда поддержу тебя']
        commentIntro = ['Я привык к непониманию общества, советую тебе заблокить возможность комментикровать',
                        'Люди такие злые, не слушай их', 'В нашем мире ты все что у тебя есть']

        tkinter.messagebox.showinfo("Troll-_-", random.choice(commentTroll))
        tkinter.messagebox.showinfo("Singing along35", random.choice(commentMini))
        tkinter.messagebox.showinfo("no opinion228", random.choice(commentMini))
        tkinter.messagebox.showinfo("Защитник", random.choice(commentCasl))
        tkinter.messagebox.showinfo("Intro22", random.choice(commentIntro))
        tkinter.messagebox.showinfo("Friend33", random.choice(commentExtra))

    title10 = Label(frame0, text="Посмотреть комментарии", bg="#696969", font=20)
    title10.pack()
    title10.place(relx=0.5, rely=0.7, anchor='center')

    btn11 = Button(frame0,text="✉✉✉✉✉✉" ,bg="#696969", command=click,)
    btn11.pack()
    btn11.place(relx=0.5, rely=0.82, anchor='center')

btn1 = Button(frame, text="(×﹏×)", bg="#696969", command=create_window1,)
btn1.pack()
btn1.place(relx=0.2, rely=0.5, anchor='center')
def create_window1():

    canvass = Canvas(height=200, width=200, )  # Холст
    canvass.pack()

    frame0 = Frame(bg="#696969")  # Рамка
    frame0.place(relx=0, rely=0, relheight=1, relwidth=1)

    title10 = Label(frame0, text="Ваш пост написан", bg="#696969", font=20)
    title10.pack()
    title10.place(relx=0.5, rely=0.5, anchor='center')

    def click():
        commentTroll = ['Что за бред сумашедшего я сейчас прочитал', 'Удали аккаунт', 'Емае ну дает']
        commentMini = ['Звони скорее в психушку, я его нашел', 'За тобой выехали', 'Давай встретимся обсудим, ауф']
        commentCasl = ['Ну что вы на человека накинулись, обычное дело, с кем не бывает?',
                       'К чему агрессия, он просто написал, что думал', 'Судите себя, а не других']
        commentExtra = ['Всё супер, давай общаться', 'Классно не хочешь повторить это вместе',
                        'Никого не слушай,  всегда поддержу тебя']
        commentIntro = ['Я привык к непониманию общества, советую тебе заблокить возможность комментикровать',
                        'Люди такие злые, не слушай их', 'В нашем мире ты все что у тебя есть']

        tkinter.messagebox.showinfo("Troll-_-", random.choice(commentTroll))
        tkinter.messagebox.showinfo("Singing along35", random.choice(commentMini))
        tkinter.messagebox.showinfo("no opinion228", random.choice(commentMini))
        tkinter.messagebox.showinfo("Защитник", random.choice(commentCasl))
        tkinter.messagebox.showinfo("Intro22", random.choice(commentIntro))
        tkinter.messagebox.showinfo("Friend33", random.choice(commentExtra))

    title10 = Label(frame0, text="Посмотреть комментарии", bg="#696969", font=20)
    title10.pack()
    title10.place(relx=0.5, rely=0.7, anchor='center')

    btn11 = Button(frame0,text="✉✉✉✉✉✉" ,bg="#696969", command=click,)
    btn11.pack()
    btn11.place(relx=0.5, rely=0.82, anchor='center')

btn2 = Button(frame, text="╮( ˘､˘ )╭", bg="#696969", command=create_window1,)
btn2.place(relx=0.8, rely=0.5, anchor='center')

def create_window1():
    canvass = Canvas(height=200, width=200, )  # Холст
    canvass.pack()

    frame0 = Frame(bg="#696969")  # Рамка
    frame0.place(relx=0, rely=0, relheight=1, relwidth=1)

    title10 = Label(frame0, text="Ваш пост написан", bg="#696969", font=20)
    title10.pack()
    title10.place(relx=0.5, rely=0.5, anchor='center')
    def click():
        commentTroll = ['Что за бред сумашедшего я сейчас прочитал', 'Удали аккаунт', 'Емае ну дает']
        commentMini = ['Звони скорее в психушку, я его нашел', 'За тобой выехали', 'Давай встретимся обсудим, ауф']
        commentCasl = ['Ну что вы на человека накинулись, обычное дело, с кем не бывает?',
                       'К чему агрессия, он просто написал, что думал', 'Судите себя, а не других']
        commentExtra = ['Всё супер, давай общаться', 'Классно не хочешь повторить это вместе',
                        'Никого не слушай,  всегда поддержу тебя']
        commentIntro = ['Я привык к непониманию общества, советую тебе заблокить возможность комментикровать',
                        'Люди такие злые, не слушай их', 'В нашем мире ты все что у тебя есть']

        tkinter.messagebox.showinfo("Troll-_-", random.choice(commentTroll))
        tkinter.messagebox.showinfo("Singing along35", random.choice(commentMini))
        tkinter.messagebox.showinfo("no opinion228", random.choice(commentMini))
        tkinter.messagebox.showinfo("Защитник", random.choice(commentCasl))
        tkinter.messagebox.showinfo("Intro22", random.choice(commentIntro))
        tkinter.messagebox.showinfo("Friend33", random.choice(commentExtra))

    title10 = Label(frame0, text="Посмотреть комментарии", bg="#696969", font=20)
    title10.pack()
    title10.place(relx=0.5, rely=0.7, anchor='center')

    btn11 = Button(frame0,text="✉✉✉✉✉✉" ,bg="#696969", command=click,)
    btn11.pack()
    btn11.place(relx=0.5, rely=0.82, anchor='center')

btn3 = Button(frame, text="ʕ ᵔᴥᵔ ʔ", bg="#696969", command=create_window1, )
btn3.pack()
btn3.place(relx=0.5, rely=0.5, anchor='center')

window.mainloop() # Конец
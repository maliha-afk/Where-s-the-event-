from tkinter import *
from tkinter import messagebox, ttk

import googletrans
from googletrans import LANGUAGES, Translator

language=list(googletrans.LANGUAGES.values())

language_code={v:k for k,v in LANGUAGES.items()}


screen=Tk()
screen.title("Language Translator App")
screen.config(bg="bisque1")
screen.geometry("720x480")

Label(screen,text="Welcome To Language App",font=("alice",15,"bold"),fg="black",bg="bisque1").place(x=230,y=3)

Label(screen,text="From",font=("alice",20,"bold"),fg="black",bg="bisque1").place(x=90,y=50)
lang1=ttk.Combobox(screen,value=language,state="readonly")
lang1.place(x=90,y=80,width=100)
lang1.set("english")



Label(screen,text="To",font=("alice",20,"bold"),fg="black",bg="bisque1").place(x=450,y=50)
lang2=ttk.Combobox(screen,value=language,state="readonly")
lang2.place(x=450,y=80,width=100)
lang2.set("bengali")

input_text=Text(screen,wrap=WORD,font=("arial",15,"bold"))
input_text.place(x=90,width=200,height=100,y=130)

output_text=Text(screen,wrap=WORD,font=("arial",15,"bold"))
output_text.place(x=450,width=200,height=100,y=130)

def translate():
    translator=Translator()
    mytext=input_text.get(1.0,END).strip()
    if mytext:
        source=language_code[lang1.get()]
        destination=language_code[lang2.get()]

        translatedtext=translator.translate(mytext,src=source,dest=destination).text
        output_text.delete(1.0,END)
        output_text.insert(END,translatedtext)


transb=Button(screen,text="Translate",font=("arial",15,"bold"),fg="black",bg="bisque2",padx=10,pady=5,relief="groove",command=translate)
transb.place(x=300,y=280)
screen.mainloop()


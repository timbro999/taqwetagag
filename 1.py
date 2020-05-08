from tkinter import *
from sentencegen import sentence_list
from sentencegen import start_gen
from threading import Timer
import time
from tkinter import ttk
import keyboard
import random
import time
import threading
writen_list = []


z=[]


def trigger(e):

    global writen_list
    time.sleep(60)
    s = word_entry.get()
    e = s.split(" ")
    print(e)
    mark_answer(e)


thread = threading.Thread(target=trigger)
thread.daemon = True
thread.start()
def mark_answer(e):

    correct_words=0

    print(len(z))
    for i in range(len(e)):
        if e[i] == sentence_list[i]:
            print("correct")
            correct_words+=1
    print(correct_words)
    return correct_words

x=mark_answer(e)

def start_game():



    global word_entry

    game = Tk()
    game.geometry("1000x500")
    start_gen()






    game.title("leshgo")

    play_button1 = ttk.Label(game, text=sentence_list[0:20])
    play_button1.grid(row=50, column=0, pady=20, columnspan=2)
    play_button2 = ttk.Label(game, text=sentence_list[20:40])
    play_button2.grid(row=51, column=0, pady=20, columnspan=2)
    play_button3 = ttk.Label(game, text=sentence_list[40:60])
    play_button3.grid(row=52, column=0, pady=20, columnspan=2)
    play_button4 = ttk.Label(game, text=sentence_list[60:80])
    play_button4.grid(row=53, column=0, pady=20, columnspan=2)
    x=mark_answer()
    wpm_display = ttk.Label(game,text="WPM:{}".format(x))
    wpm_display.grid(row=50, column = 5, pady=20, columnspan=2)

    words = DoubleVar()
    words.set("")

    word_entry = ttk.Entry(game)
    word_entry.grid(row=1, column=1)
    word_entry.pack


    start_button = ttk.Button(game, text="start", command=lambda :trigger(z))
    start_button.grid(row=30, column=100, pady=20, columnspan=2)



    game.mainloop()












root = Tk()
root.geometry("500x120")

root.title("Typer Game")

header_text= StringVar()
header_text.set("Welcome to the typer racer game, press start to play")

header_label = ttk.Label(root, textvariable=header_text, wraplength=300)
header_label.grid(row=0, column=0, columnspan=2, padx=120, pady=10)
header_label.config(font=("Courier", 11))


play_button = ttk.Button(root, text="Play", command=start_game)
play_button.grid(row=50, column=0, pady=20, columnspan = 2 )



















root.mainloop()
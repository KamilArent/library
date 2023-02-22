import tkinter as tk
import random

def sprawdz(gracz):
    wygrane = {
        "papier": "kamień",
        "kamień": "nożyczki",
        "nożyczki": "papier"
        }
    aiChoice = random.choice(gun)
    if(wygrane[gracz] == aiChoice):
        status.config(text = "Wygrana! :) broń przeciwnika: " + aiChoice, fg = "green")
    elif(gracz == aiChoice):
        status.config(text="Remis :O broń przeciwnika: " + aiChoice, fg = "blue")
    else:
        status.config(text="Przegrana :( broń przeciwnika: " + aiChoice,  fg = "dark red")

window = tk.Tk()
window.title = "Rock paper scissors"
window.geometry("600x400")
window.resizable(False, False)
gun = ["papier", "kamień", "nożyczki"]
status = tk.Label(
    text="Wybierz swoją broń!",
    fg = "blue",
    bg = "grey",
    font = ("Arial", 25),
    width= 30,
    height=2
)
status.pack()
P = tk.Button(
    text = "📃 PAPER",
    bg = "lightgrey",
    fg = "blue",
    font = ("Arial", 25),
    width = 30,
    height = 2,
    command=lambda: sprawdz("papier")
).pack()
K = tk.Button(
    text = "🗿 ROCK",
    bg = "lightgrey",
    fg = "blue",
    font = ("Arial", 25),
    width = 30,
    height = 2,
    command=lambda: sprawdz("kamień")
).pack()
N = tk.Button(
    text = "✂️ SCISSORS",
    bg = "lightgrey",
    fg = "blue",
    font = ("Arial", 25),
    width = 30,
    height = 2,
    command=lambda: sprawdz("nożyczki")
).pack()
window.mainloop()

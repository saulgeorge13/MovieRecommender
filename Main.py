import pandas as pd
import numpy as np
import PlotRecommender
import CastRecommender
from tkinter import *

root = Tk()
root.geometry("480x480")
root.title("Saul's Movie Recommender")

l1 = Label(root, text="Name a movie you love: ")
l1.grid(row=0, column=0, columnspan=2, padx=15, pady=10)

def search():
    l2 = Label(root, text="Here are some movies for you!")
    l2.grid(row=1)
    movie = e.get()
    movies = PlotRecommender.get_recommendations(movie)
    txt.insert(0.0, movies)

searchButton = Button(root, text="Find movies for you!", command=search)
searchButton.grid(row=0, column=5)


e = Entry(root, borderwidth= 5)
e.grid(row=0, column=2, columnspan=3, padx=10, pady=10)

txt = Text(root, width=60, height=20, wrap=WORD)
txt.grid(row=3, columnspan=8, sticky=W)

root.mainloop()
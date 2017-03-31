'''
Created on Mar 26, 2017

@author: Austin Dillinger
'''

import tkinter as tk

from getStyle import getStyle
from getABV import getABV
from getBeerDate import getBeerDate
from getTemperature import getTemperature

side1 = "Shower Hop"
side2 = "Shower Hop"

root = tk.Tk()
root.geometry("480x320")
root.title("Beer!")

backgroundFile = tk.PhotoImage(file = "D:\\Pictures\\Iowa.png")
backgroundLabel = tk.Label(root, image=backgroundFile)

backgroundLabel.place(x=0,y=0, relwidth=1, relheight=1)

mainframe = tk.Frame(root)

mainframe.grid(column=1, row=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)

feet_entry = tk.Entry(mainframe, width=7, textvariable="beer")

tk.Label(mainframe, height=2, width = 10, text=getStyle(side1)).grid(column=2, row=1 )
tk.Label(mainframe, height=2, width = 10, text=getStyle(side2)).grid(column=3, row=1 )

tk.Label(mainframe, height=2, width = 10, text=getTemperature(side1)).grid(column=1, row=2 )
tk.Label(mainframe, height=2, width = 10, text=getABV(side1)).grid(column=2, row=2 )
tk.Label(mainframe, height=2, width = 10, text=getABV(side2)).grid(column=3, row=2 )
tk.Label(mainframe, height=2, width = 10, text=getTemperature(side2)).grid(column=4, row=2 )

tk.Label(mainframe, height=2, width = 10, text=getBeerDate(side1)).grid(column=2, row=3 )
tk.Label(mainframe, height=2, width = 10, text=getBeerDate(side2)).grid(column=3, row=3)

root.mainloop()
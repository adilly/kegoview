'''
Created on Mar 26, 2017

@author: Austin Dillinger
'''

import tkinter as tk

from getStyle import getStyle
from getABV import getABV
from getBeerDate import getBeerDate
from getTemperature import getTemperature
#from PIL import ImageTk, Image


side1 = "Shower Hop"
side2 = "Shower Hop"

defaultFont=("FontAwesome Regular",12)

root = tk.Tk()
root.geometry("480x320")
root.title("Keg-O-View")

#img = ImageTk.PhotoImage(Image.open("D:\\Pictures\\command_prompt.png"))

backgroundFile = tk.PhotoImage(file = "D:\\Pictures\\kegs.png")
backgroundLabel = tk.Label(root, image=backgroundFile)
backgroundLabel.place(x=0,y=0, relwidth=1, relheight=1)

frame = tk.Frame(root)


frame.grid(padx=7, pady=100)
frame.config(bg="black")



#Row 1
tk.Label(frame, 
         font = (defaultFont), 
         #justify = 'left', 
         fg="red",
         #bg="black",
         #padx=30,
         #image=img,
         #height = 2, 
         width = 16, 
         text = side1
         ).grid(column=1, row=1)

tk.Label(frame, width = 23).grid(column=2, row=4)
         
tk.Label(frame, 
         font = defaultFont, 
         #justify = "left", 
         fg="red",
         #bg="black",
         #padx=80,
         #height = 2, 
         width = 16,
         text = side2
         ).grid(column=3, row=1)

#Row 2
tk.Label(frame, 
         font = defaultFont, 
         #justify = 'center', 
         fg="red",
         #padx=30,
         #bg="black",
         #height = 1, 
         width = 16, 
         text = getStyle(side1)
         ).grid(column=1, row=2)
         
tk.Label(frame, width = 20).grid(column=2, row=4)
         
tk.Label(frame, 
         font = defaultFont, 
         #justify = 'center', 
         fg="red",
         #padx=80,
         #bg="black",
         #height = 1, 
         width = 16,
         text = getStyle(side2)
         ).grid(column=3, row=2)

#Row 3
tk.Label(frame, 
         font = defaultFont, 
         #justify = "left", 
         fg="red",
         #padx=30,
         #bg="black",
         #height = 2, 
         width = 16,
         text=getTemperature(side1)
         ).grid(column=1, row=3)
         
tk.Label(frame, width = 20).grid(column=2, row=4)
         
tk.Label(frame, 
         font = defaultFont, 
         #justify = "left", 
         fg="red",
         #padx=80,
         #bg="black",
         #height = 2, 
         width = 16,
         text=getTemperature(side2)
         ).grid(column=3, row=3)
         
#Row 4         
tk.Label(frame, 
         font = defaultFont, 
         #justify = "left", 
         fg="red",
         #padx=30,
         #bg="black",
         #height = 2, 
         width = 16,
         text=getABV(side2)
         ).grid(column=1, row=4)
         
tk.Label(frame, width = 20).grid(column=2, row=4)
         
tk.Label(frame, 
         font = defaultFont, 
         #justify = "left", 
         fg="red",
         #padx=80,
         #bg="black",
         #height = 2, 
         width = 16,
         text=getABV(side1)
         ).grid(column=3, row=4)

#Row 5
tk.Label(frame, 
         font = defaultFont, 
         #justify = "left", 
         fg="red",
         #padx=30,
         #bg="black",
         #height = 1, 
         width = 16, 
         text="Brew Date:"
         ).grid(column=1, row=5)
         
tk.Label(frame, width = 20).grid(column=2, row=4)
         
tk.Label(frame, 
         font = defaultFont, 
         #justify = "left", 
         fg="red",
         #padx=80,
         #bg="black",
         #height = 1, 
         width = 16,   
         text="Brew Date:"
         ).grid(column=3, row=5)
         
#Row 6
tk.Label(frame, 
         font = defaultFont, 
         #justify = "left",
         fg="red",
         #padx=30,
         #bg="black", 
         #height = 2, 
         width = 16, 
         text=getBeerDate(side1)
         ).grid(column=1, row=6)
         
tk.Label(frame, width = 20).grid(column=2, row=4)
         
tk.Label(frame, 
         font = defaultFont, 
         #justify = "left", 
         fg="red",
         #padx=80,
         #bg="black",
         #height = 2, 
         width = 16,   
         text=getBeerDate(side2)
         ).grid(column=3, row=6)

root.mainloop()
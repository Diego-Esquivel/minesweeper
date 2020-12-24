import tkinter as tk
import tkinter.simpledialog as sdg
import tkinter.messagebox as mbx
import tkinter.font as tkf
import tkinter.filedialog as fdg
import platform as pt
import time
import sys

id = "C:\\"

base = tk.Tk()
base.title("Diego G Esquivel's Minesweeper Demo")
base.resizable(False, False)

buttonSaveTimes = [[0 for i in range(32)] for j in range(10)]

# Fonts
fontNormal = tkf.Font(family = "Consolas", size = 8)
fontTitle = tkf.Font(family = "Consolas", size = 12, weight = "bold", slant = "italic")

frameTimes = tk.LabelFrame(base, text = "Minesweeper", bd = 4, relief = "raised", font = fontTitle)
frameTimes.grid(row = 0, column = 0, padx = 4, pady = 4, sticky = "n")

frameTimesScreen = tk.Canvas(frameTimes, width = 800, height = 400)
frameTimesScreen.pack(padx = 4, pady = 4)

for u in range(32):
			for c in range(10):
				buttonSaveTimes[c][u] = tk.Button(frameTimesScreen, text = "?", bd = 1, command = lambda row = c, col = u: checkSweeper(row, col), font = fontNormal, justify = 'center')
				buttonSaveTimes[c][u].grid(row = c, column = u, columnspan = 1)

def checkSweeper(row_, column_):
	buttonSaveTimes = tk.Button(frameTimesScreen, text = " ", bd = 1, command = lambda row = row_, column = column_: checkSweeper(row, column), font = fontNormal, justify = 'center')
	print(str(row_) + "\t" + str(column_))
	buttonSaveTimes.grid(row = row_, column = column_, columnspan = 1)
	return 1

frameMain = tk.LabelFrame(base, text="Sorting Panel", bd = 4, relief = "raised", font = fontTitle)
frameMain.grid(row = 1, column = 0, columnspan = 2, padx = 4, pady = 4)

frameScreen = tk.Canvas(frameMain, width = 800, height = 100)
frameScreen.pack(padx = 4, pady = 4)

def clearElements():
	for el in frameScreen.find_all():
		frameScreen.delete(el)

def updateElements(strNewElements):
	try:
		newElements = int(strNewElements)
	except ValueError:
		newElements = strNewElements

	clearElements()


	for u in range(32):
		for c in range(10):
			buttonSaveTimes[c][u] = tk.Button(frameTimesScreen, text = buttonSaveTimes[c][u]['text'], bd = 1, command = lambda row = c, col = u: checkSweeper(row, col), font = fontNormal, justify = 'center')
			buttonSaveTimes[c][u].grid(row = c, column = u, columnspan = 1)

	frameScreen.update_idletasks()

updateElements(0)

base.mainloop()
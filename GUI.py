import tkinter
from tkinter import Button, Label, Entry, StringVar
from sort import Sort


class GUI:
	def __init__ (self, title):
		self.window = tkinter.Tk()
		self.window.title(title)
		Label(self.window, text='Number of values').grid(row=0)
		Label(self.window, text='Range of values').grid(row=1)
		self.number = StringVar()
		self.range = StringVar()
		self.number_entry = Entry(self.window, textvariable=self.number)
		self.range_entry= Entry(self.window, textvariable=self.range)
		self.number_entry.grid(row=0, column=1)
		self.range_entry.grid(row=1, column=1)
		self.btn = Button(self.window, text="Start", width = 15, command=self.getValues)
		self.btn.grid(row=2, columnspan=2)
		self.window.mainloop()

	def getValues(self):
		num_amount, num_range = self.number.get(), self.range.get()
		self.window.destroy()
		sort = Sort(num_amount, num_range)
		sort.draw()



newGUI = GUI('Settings')
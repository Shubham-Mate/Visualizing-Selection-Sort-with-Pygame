import tkinter
from tkinter import Button, Label, Entry, StringVar
from sort import Sort


class GUI:
	def __init__ (self, title):
		self.window = tkinter.Tk()
		self.window.title(title)
		Label(self.window, text='Number of values').grid(row=0)
		self.number = StringVar()
		self.number_entry = Entry(self.window, textvariable=self.number)
		self.number_entry.grid(row=0, column=1)
		self.btn = Button(self.window, text="Start", width = 15, command=self.getValues)
		self.btn.grid(row=2, columnspan=2)
		self.window.mainloop()

	def getValues(self):
		num_amount = self.number.get()
		try:
			num_amount = int(num_amount)
			self.window.destroy()
			sort = Sort(num_amount)
			sort.draw()
		except ValueError:
			pass


newGUI = GUI('Settings')
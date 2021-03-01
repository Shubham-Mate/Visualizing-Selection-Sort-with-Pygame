import tkinter
from tkinter import Button, Label, Entry, StringVar, Frame
from tkinter.font import Font
from sort import Sort


class GUI:
	def __init__ (self, title):
		self.window = tkinter.Tk()
		self.window.title(title)
		self.window['bg'] = '#161b22'
		
		self.font_size = 16
		
		Label(self.window, text='Number of values', fg='white', bg='#161b22', font=Font(family="Helvetica",size=self.font_size)).grid(row=0, padx=10, pady=10)
		
		self.text_frame = Frame(self.window, width=100, height=50)
		self.text_frame.grid(row=0, column=1, padx=10, pady=10)
		
		self.number = StringVar()
		self.number_entry = Entry(self.text_frame, textvariable=self.number, font=Font(family="Helvetica",size=self.font_size)).grid()
		self.btn = Button(self.window, text="Start", width = 15, fg='white', bg='#0d1117', font=Font(family="Helvetica",size=self.font_size), highlightthickness=0, bd=0, activebackground='#040507', activeforeground='white', command=self.getValues)
		self.btn.bind("<Enter>", self.onEnter)
		self.btn.bind("<Leave>", self.onLeave)
		self.btn.grid(row=2, columnspan=2, padx=10, pady=10)
		self.window.mainloop()
	
	def onLeave(self, e):
		self.btn['background'] = '#0d1117'

	def onEnter(self, e):
		self.btn['background'] = '#040507'
	
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

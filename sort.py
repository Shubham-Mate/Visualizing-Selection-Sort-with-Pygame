import pygame
import random
import math
import time



class Sort:
	def __init__(self, numval):
		#Window
		self.WIDTH, self.HEIGHT = 1280, 550
		self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		self.FPS_CAP = 60

		#Colors
		self.WHITE = (255, 255, 255)
		self.BLUE = (0, 0, 255)
		self.GREEN = (0, 255, 0)
		self.RED = (255, 0, 0)

		# List Generation
		self.NUMBERS = numval
		self.genList = ([i for i in range(1, self.NUMBERS)]) # Generates a list of numbers from 1 till the input
		random.shuffle(self.genList) # Shuffles the List


		# Width of one bar representing a value
		self.rect_width = (self.WIDTH/len(self.genList))

		# Some Variables needed for the sort and mainloop 
		self.count = 0
		self.sort_start = False
		self.run = True
		pygame.display.set_caption("Selection Sort")

	def selection_sort(self, count):
		# Variables for loop
		min = 0 # Stores the so far minimum value
		storeVal = 0 # Stores the index of the minimum value
		for i in range(count, len(self.genList)):
			for j in range(i, len(self.genList)):				
				if min == 0: # Sets the min if min hasn't been set yet
					min = self.genList[j]
					storeVal = j
				elif self.genList[j] < min: # If smaller than min then it'll be the new min
					min = self.genList[j]
					storeVal = j
			self.genList[i], self.genList[storeVal] = self.genList[storeVal], self.genList[i] # Interchanges the places of value at i and value in storeVal
			return storeVal, count

	def drawValues(self, val1, val2):
		listInd = 0 # Variable to keep a track of the index
		for i in self.genList:
			color = self.BLUE if (val1 != listInd and val2 !=listInd) else self.GREEN if val2==listInd else self.RED # Decides the color
				
			# Draw the bar
			pygame.draw.rect(self.WIN, color, pygame.Rect(self.rect_width*listInd, (self.HEIGHT) - (i * (self.HEIGHT/self.NUMBERS)), self.rect_width, i * (self.HEIGHT/self.NUMBERS) + (self.HEIGHT-round((self.HEIGHT/30)))))
			listInd += 1

	def draw(self):
		while self.run: # Main Loop
			self.WIN.fill(self.WHITE)
			val1, val2 = None, None # Initializing the variables for representing the colors

			if self.sort_start:
				try:
					val1, val2 = self.selection_sort(self.count)
				except:
					val1, val2 = self.NUMBERS+1, self.NUMBERS+1
				self.count += 1

			self.drawValues(val1, val2)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.run = False

			keys_pressed = pygame.key.get_pressed()
			if keys_pressed[pygame.K_s]: # Pressing S for Pausing/Continuing Sort
				if not(self.sort_start): # If Sort is paused
					self.sort_start = True # Start sort
				else:
					self.sort_start = False # Else pause sort
				time.sleep(0.2) # To avoid multiple key presses
			if keys_pressed[pygame.K_r]: # If R is pressed
				print(self.genList)
				 # Generate new list
				self.genList = ([i for i in range(1, self.NUMBERS)])
				random.shuffle(self.genList)

				
				# Reset some variables
				self.count = 0 
				self.sort_start = False
				time.sleep(0.5) # To avoid multiple key presses

			
			pygame.display.update()

		pygame.quit()

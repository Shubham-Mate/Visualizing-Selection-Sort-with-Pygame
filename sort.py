import pygame
import random
import math
import time



class Sort:
	def __init__(self, numval):
		# Initialize Pygame
		pygame.init()

		#Windows
		self.WIDTH, self.HEIGHT = 1280, 550
		self.SURFACE_WIDTH, self.SURFACE_HEIGHT = 1000, 550
		self.MENU_WIDTH, self.MENU_HEIGHT = 280, 550
		self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		self.DATA_SURFACE = pygame.Surface((self.SURFACE_WIDTH, self.SURFACE_HEIGHT))
		self.MENU_SURFACE = pygame.Surface((self.MENU_WIDTH, self.MENU_HEIGHT))
		self.FPS_CAP = 60

		#Colors
		self.WHITE = (255, 255, 255)
		self.BLUE = (0, 0, 255)
		self.GREEN = (0, 255, 0)
		self.RED = (255, 0, 0)
		self.BLACK = (0, 0, 0)
		self.MENU_BACKGROUND = (22, 27, 34)
		self.BUTTON_BACKGROUND = (13, 17, 23)

		# Fonts
		font = pygame.font.SysFont("Helvetica", 32)
		self.sort_text = font.render("Continue/Pause Sort", True, self.WHITE)
		self.gen_text = font.render("Generate new list", True, self.WHITE)

		# List Generation
		self.NUMBERS = numval
		self.genList = ([i for i in range(1, self.NUMBERS)]) # Generates a list of numbers from 1 till the input
		random.shuffle(self.genList) # Shuffles the List


		# Width of one bar representing a value
		self.rect_width = (self.SURFACE_WIDTH/len(self.genList))

		# Some Variables needed for the sort and mainloop 
		self.count = 0
		self.sort_start = False
		self.run = True
		pygame.display.set_caption("Selection Sort")

	# Selection Sort
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

	# Bubble Sort
	def bubble_sort(self, count):
		count2 = 0
		for i in range(count, len(self.genList)):
			for j in range(i, len(self.genList)):
				if self.genList[j+1] < self.genList[j]:
					self.genList[j+1], self.genList[j] = self.genList[j], self.genList[j+1]
			return j, i

	# Draws the Bars representing each value
	def drawValues(self, val1, val2):
		listInd = 0 # Variable to keep a track of the index
		for i in self.genList:
			color = self.BLUE if (val1 != listInd and val2 !=listInd) else self.GREEN if val2==listInd else self.RED # Decides the color
				
			# Draw the bar
			pygame.draw.rect(self.DATA_SURFACE, color, pygame.Rect(self.rect_width*listInd, (self.SURFACE_HEIGHT) - (i * (self.SURFACE_HEIGHT/self.NUMBERS)), self.rect_width, i * (self.SURFACE_HEIGHT/self.NUMBERS) + (self.SURFACE_HEIGHT-round((self.SURFACE_HEIGHT/30)))))
			listInd += 1
		self.WIN.blit(self.DATA_SURFACE, (0, 0))


	# Draws the menu
	def drawMenu(self):
			pygame.draw.rect(self.MENU_SURFACE, self.BUTTON_BACKGROUND, pygame.Rect(10, 10, self.MENU_WIDTH-20, 50)) # Sort Button
			pygame.draw.rect(self.MENU_SURFACE, self.BUTTON_BACKGROUND, pygame.Rect(10, 10+50+10, self.MENU_WIDTH-20, 50)) # Generate Button
			self.MENU_SURFACE.blit(self.sort_text, (10+round((self.MENU_WIDTH-20)/35), 10+round(50/10))) # Text for Sort Button
			self.MENU_SURFACE.blit(self.gen_text, (10+round((self.MENU_WIDTH-20)/10), 10+50+10+round(50/10))) # Text for Generate Button
			self.WIN.blit(self.MENU_SURFACE, (1000, 0))
			

	def generateNewList(self):
		# Generate new list
		self.genList = ([i for i in range(1, self.NUMBERS)])
		random.shuffle(self.genList)
	
		# Reset some variables
		self.count = 0 
		self.sort_start = False


	def startSort(self):
		if not(self.sort_start): # If Sort is paused
			self.sort_start = True # Start sort
		else:
			self.sort_start = False # Else pause sort


	def draw(self):
		while self.run: # Main Loop
			self.DATA_SURFACE.fill(self.WHITE)
			self.MENU_SURFACE.fill(self.MENU_BACKGROUND)
			val1, val2 = None, None # Initializing the variables for representing the colors

			if self.sort_start:
				try:
					val1, val2 = self.selection_sort(self.count)
				except:
					val1, val2 = self.NUMBERS+1, self.NUMBERS+1
				self.count += 1

			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.run = False
				if event.type == pygame.MOUSEBUTTONUP: # If mouse is clicked
					position = pygame.mouse.get_pos()
					if (1000+10 <= position[0] <= 1000+10+self.MENU_WIDTH-20) and (10 <= position[1] <= 50):  # If mouse is inside sort button
						self.startSort()
					if (1000+10 <= position[0] <= 1000+10+self.MENU_WIDTH-20) and (10+50+10 <= position[1] <= 10+50+10+50): # If mouse is inside gen button
						self.generateNewList()


			self.drawValues(val1, val2)
			self.drawMenu()

			pygame.display.update()

		pygame.quit()


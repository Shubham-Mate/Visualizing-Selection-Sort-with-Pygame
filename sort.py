import pygame
import random
import math
import time



class Sort:
	def __init__(self):
		self.WIN = pygame.display.set_mode((700, 700))
		self.FPS_CAP = 60
		self.WHITE = (255, 255, 255)
		self.BLUE = (0, 0, 255)
		self.NUMBERS = 250
		self.NUMBER_RANGE = 500000000
		self.genList = [random.randint(1, self.NUMBER_RANGE) for i in range(self.NUMBERS)]
		self.rect_width = (700/len(self.genList))
		self.count = 0
		self.sort_start = False
		self.run = True
		pygame.display.set_caption("Selection Sort")

	def selection_sort(self, count):
		min = 0
		for i in range(count, len(self.genList)):
			for j in range(i, len(self.genList)):
				if min == 0:
					min = self.genList[j]
				elif self.genList[j] < min:
					min = self.genList[j]
					self.genList[i], self.genList[j] = self.genList[j], self.genList[i]
			break

	def main(self):
		while self.run:
			self.WIN.fill(self.WHITE)
			listInd = 0
			for i in self.genList:
				pygame.draw.rect(self.WIN, self.BLUE, pygame.Rect(self.rect_width*listInd, 690 - (i * (700/self.NUMBER_RANGE)), self.rect_width, i * (700/self.NUMBER_RANGE)))
				listInd += 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.run = False
			keys_pressed = pygame.key.get_pressed()
			if keys_pressed[pygame.K_s]:
				self.sort_start = True
			if keys_pressed[pygame.K_r]:
				self.genList = [random.randint(1, self.NUMBER_RANGE) for i in range(self.NUMBERS)]
				self.count = 0
				self.sort_start = False
				time.sleep(0.5)

			if self.sort_start:
				self.selection_sort(self.count)
				self.count += 1

			pygame.display.update()

		pygame.quit()

sort = Sort()
sort.main()
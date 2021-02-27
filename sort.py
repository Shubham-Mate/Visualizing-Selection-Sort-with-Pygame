import pygame
import random
import math
import time



class Sort:
	def __init__(self, numval, numrange):
		self.WIDTH, self.HEIGHT = 1280, 720
		self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		self.FPS_CAP = 60
		self.WHITE = (255, 255, 255)
		self.BLUE = (0, 0, 255)
		self.NUMBERS = int(numval)
		self.NUMBER_RANGE = int(numrange)
		self.genList = [random.randint(1, self.NUMBER_RANGE) for i in range(self.NUMBERS)]
		self.rect_width = (self.WIDTH/len(self.genList))
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

	def draw(self):
		while self.run:
			self.WIN.fill(self.WHITE)

			if self.sort_start:
				self.selection_sort(self.count)
				self.count += 1

			listInd = 0
			for i in self.genList:
				pygame.draw.rect(self.WIN, self.BLUE, pygame.Rect(self.rect_width*listInd, (self.HEIGHT-(self.HEIGHT/30)) - (i * (self.HEIGHT/self.NUMBER_RANGE)), self.rect_width, i * (self.HEIGHT/self.NUMBER_RANGE) + (self.HEIGHT-round((self.HEIGHT/30)))))
				listInd += 1

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.run = False

			keys_pressed = pygame.key.get_pressed()
			if keys_pressed[pygame.K_s]:
				if not(self.sort_start):
					self.sort_start = True
				else:
					self.sort_start = False
				time.sleep(0.2)
			if keys_pressed[pygame.K_r]:
				self.genList = [random.randint(1, self.NUMBER_RANGE) for i in range(self.NUMBERS)]
				self.count = 0
				self.sort_start = False
				time.sleep(0.5)

			
			pygame.display.update()

		pygame.quit()

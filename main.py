import pygame
import random
import math
import time

WIN = pygame.display.set_mode((700, 700))
FPS_CAP = 60
CLOCK = pygame.time.Clock()
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
NUMBERS = 250

pygame.display.set_caption("Selection Sort")
genList = [random.randint(1, 100) for i in range(NUMBERS)]
#print(genList)
rect_width = (700/len(genList))
count = 0

def selection_sort(count):
	min = 0
	for i in range(count, len(genList)):
		for j in range(i, len(genList)):
			if min == 0:
				min = genList[j]
			elif genList[j] < min:
				min = genList[j]
				genList[i], genList[j] = genList[j], genList[i]
		break

sort_start = False
run = True
while run:
	CLOCK.tick(FPS_CAP)
	WIN.fill(WHITE)
	listInd = 0
	for i in genList:
		pygame.draw.rect(WIN, BLUE, pygame.Rect(rect_width*listInd, 690 - (i*5), rect_width, i*5))
		listInd += 1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	keys_pressed = pygame.key.get_pressed()
	if keys_pressed[pygame.K_s]:
		sort_start = True
	if keys_pressed[pygame.K_r]:
		genList = [random.randint(1, 100) for i in range(NUMBERS)]
		count = 0
		sort_start = False
		time.sleep(1)

	if sort_start:
		selection_sort(count)
		count += 1

	pygame.display.update()

pygame.quit()
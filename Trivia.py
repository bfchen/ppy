import sys
import pygame
from pygame.locals import *
import math


class Trivia(object):
	"""docstring for Trivia"""
	def __init__(self, fileName):
		super(Trivia, self).__init__()
		self.data = []
		self.current = 0
		self.total = 0
		self.correct = 0
		self.score = 0
		self.scored = False
		self.failed = False
		self.wrongAnswer = 0
		self.colors = [white, white, white, white]
		
		f = open(fileName, "r")
		triviaData = f.readlines()
		f.close()

		for textLine in triviaData:
			self.data.append(textLine.strip())
			self.total += 1

	def showQuestion(self):
		printText(font1, 210, 5, "TRIVIA GAME")
		printText(font2, 190, 500-20, "Press Keys (1-4) To Answer", purple)
		printText(font2, 530, 5, "SCORE", purple)
		printText(font2, 550, 25, str(self.score), purple)

		self.correct = int(self.data[self.current+5])

		question = self.current // 6 + 1
		printText(font1, 5, 80, "QUESTION"+str(question))
		printText(font2, 20, 120, self.data[self.current], yellow)

		if self.score:
			self.colors = [white, white, white, white]
			self.colors[self.correct-1] = green
			printText(font1, 230, 380, "CORRECT!", green)
			printText(font2, 170, 420, "Press Enter For Next Question", green)
		elif self.failed:
			self.colors = [white, white, white, white]
			self.colors[self.wrongAnswer-1] = red
			self.colors[self.correct-1] = green
			printText(font1, 220, 380, "INCORRECT!", red)
			printText(font2, 170, 420, "Press Enter For Next Question", red)

		printText(font1, 5, 170, "ANSWERS")
		printText(font2, 20, 210,"1 - " + self.data[self.current+1], self.colors[0])
		printText(font2, 20, 240,"2 - " + self.data[self.current+2], self.colors[1])
		printText(font2, 20, 270,"3 - " + self.data[self.current+3], self.colors[2])
		printText(font2, 20, 300,"4 - " + self.data[self.current+4], self.colors[3])


	def hanleInput(self, number):
		if not self.scored and not self.failed:
			if number == self.correct:
				self.scored = True
				self.score += 1
			else:
				self.failed = True
				self.wrongAnswer = number


	def nextQuestion(self):
		if self.scored or self.failed:
			self.scored = False
			self.failed = False
			self.correct = 0
			self.colors = [white, white, white, white]
			self.current += 6
			if self.current >= self.total:
				self.current = 0
	

def printText(font, x, y, text, color=(255,255,255), shadow = True):
	if shadow:
		imgText = font.render(text, True, (0,0,0))
		screen.blit(imgText, (x-2,y-2))
	imgText = font.render(text, True, color)
	screen.blit(imgText, (x, y))


# main program begins

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("The Trivia Game")

font1 = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 24)

white = 255, 255, 255
cyan = 0, 255, 255
yellow = 255, 255, 0
purple = 255, 0, 255
green = 0, 255, 0
red = 255, 0, 0

# load the trivia file
trivia = Trivia("triviadata.txt")

#repeat loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
		elif event.type == KEYUP:
			if event.key == pygame.K_1:
				trivia.hanleInput(1)
			elif event.key == pygame.K_2:
				trivia.hanleInput(2)
			elif event.key == pygame.K_3:
				trivia.hanleInput(3)
			elif event.key == pygame.K_4:
				trivia.hanleInput(4)
			elif event.key == pygame.K_RETURN:
				trivia.nextQuestion()

	# clear screen
	screen.fill((0, 0, 200))

	# display question
	trivia.showQuestion()

	#update the display
	pygame.display.update()



















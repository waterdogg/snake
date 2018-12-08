import pygame
import pygame
from pygame.locals import *
from sys import exit
import random
pygame.init()
JIANGE=20
black=(255,255,255)
screen = pygame.display.set_mode((400, 400), 0, 32)
yellow=(255,255,0)
green=(0,255,0)
red=(255,0,0)
snake=[[0,0],[1,0],[2,0]]
dian=[]
XIANG="r"
yan=0
c_XIANG=""
#C_XIANG=CHANGE XIANG
score_score=0
keep_going=True
pygame.display.set_caption("贪吃蛇V0.01")
class score:
	
	def __init__(self,score):
			
			
			scorestr=str(score)
			
			self.red=(255,0,0)
			self.font=pygame.font.SysFont(None,52)
			self.image=self.font.render(scorestr,True,self.red)
	
	def update_score(self,score):
			
			scorestr=str(score)
			self.image=self.font.render(scorestr,True,self.red)
	def update_text(self,text):
			self.font=pygame.font.SysFont(None,30)
			
			self.image=self.font.render(text,True,self.red)
def ran():
	global snake
	global dian
	a=random.randint(0,19)
	b=random.randint(0,19)
	dian=[a,b]
	for i in snake:
		if i[0]==a and i[1]==b:
			ran()
def update():
	
	global keep_going
	global s
	global score_score

	global snake
	global XIANG
	
	global yan

	global dian
	if not dian:
		ran()		 
			
		
	
		
	pygame.draw.rect(screen,(0,0,255),Rect((dian[0]*JIANGE,dian[1]*JIANGE),(JIANGE,JIANGE)))
	 
	if XIANG=="r":
		snake.append([snake[-1][0]+1,snake[-1][1]])
	elif XIANG=="l":
		snake.append([snake[-1][0]-1,snake[-1][1]])
	elif XIANG=="u":
		snake.append([snake[-1][0],snake[-1][1]-1])
	elif XIANG=="d":
		snake.append([snake[-1][0],snake[-1][1]+1])
	
	if snake[-1][0] != dian[0] or snake[-1][1] != dian[1]:
		del snake[0]
	else:
		score_score+=1
		dian=[]
		screen.fill((0,0,0))
	
	if snake[-1][0] < 0 or snake[-1][0] >19 or snake[-1][1] <0 or snake[-1][1] >19:
		keep_going=False
	
	for i in range(len(snake)):
		if i==len(snake)-1:
			pygame.draw.rect(screen,yellow,Rect((snake[i][0]*JIANGE,snake[i][1]*JIANGE),(JIANGE,JIANGE)),1) 
		elif i==0:
			pygame.draw.rect(screen,green,Rect((snake[i][0]*JIANGE,snake[i][1]*JIANGE),(JIANGE,JIANGE)),1) 
		else:
			pygame.draw.rect(screen,black,Rect((snake[i][0]*JIANGE,snake[i][1]*JIANGE),(JIANGE,JIANGE)),1) 
	
	for i in range(len(snake)-1):
		if snake[-1][0]==snake[i][0] and snake[-1][1]==snake[i][1]:
			
			keep_going=False
fps=pygame.time.Clock()
s=score("score: "+str(score_score))
c=score("Level "+str(score_score//10+1))	
while True:

	if keep_going==True:
				
		for event in pygame.event.get():
	
			if event.type == QUIT:
				exit()
			if event.type == KEYDOWN:
				if event.key==K_LEFT:
			
				
				
					c_XIANG="l"
				elif event.key==K_RIGHT: 
				
					c_XIANG="r"
				elif event.key==K_UP:
					c_XIANG="u"
				elif event.key==K_DOWN: 
			
					c_XIANG="d"
				
		if c_XIANG=="l" and not XIANG=="r":
			XIANG=c_XIANG
		if c_XIANG=="r" and not XIANG=="l":
			XIANG=c_XIANG
		if c_XIANG=="u" and not XIANG=="d":
			XIANG=c_XIANG
		if c_XIANG=="d" and not XIANG=="u":
			XIANG=c_XIANG
	elif keep_going==False:
		s.update_text("GameOver!"+" "+"Your"+" "+"score"+" "+"is"+" "+str(score_score))
		screen.blit(s.image,(0,50))
	
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
			if event.type==KEYDOWN:
			

	
				if event.key==K_SPACE:

					snake=[[0,0],[1,0],[2,0]]
					dian=[]
					XIANG="r"
					
					c_XIANG=""
					score_score=0
					keep_going=True
					s=score("score: "+str(score_score))
					c=score("Level "+str(score_score//10+1))
					screen.fill((0,0,0))
					
				
				
				
				
	if keep_going==True:
		
		s.update_score("score: "+str(score_score))
		screen.fill((0,0,0))
		update()
		screen.blit(s.image,(0,0))
		c.update_score("Level "+str(score_score//10+1))
		screen.blit(c.image,(200,350))
	
	pygame.display.update()
	
	fps.tick(2*(score_score//10)+4)
	
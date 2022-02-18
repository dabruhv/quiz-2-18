# quiz-2-18
import pygame
import random

pygame.init


#creates game screen and caption
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("quiz")

#game variables
doExit = False #variable to quit out of game loop

class butterfly():
    def __init__(self,x,y):
        self.x = x 
        self.y = y
    def draw(self,x,y):
        pygame.draw.circle(screen, (220,220, 220), (self.x-20, self.y+90), 40)
        pygame.draw.circle(screen, (220, 220, 220), (self.x+70, self.y+90), 40)

        pygame.draw.circle(screen, (115, 115, 115), (self.x-20, self.y+50), 50)
        pygame.draw.circle(screen, (115, 115, 115), (self.x+70, self.y+50), 50)



        pygame.draw.ellipse(screen, (192,192,192), (self.x, self.y, 50, 150))

        pygame.draw.line(screen, (255,255,255), (self.x+20,self.y+10), (self.x-30,self.y-40),5)
        pygame.draw.line(screen, (255,255,255), (self.x+20,self.y+10), (self.x+70,self.y-40),5)

        pygame.draw.arc(screen, (0, 0, 0), (self.x, self.y, 50, 50), (7*3.14)/6, (11*3.14)/6,5)
        pygame.draw.arc(screen, (0, 0, 0), (self.x, self.y+20, 50, 50), (7*3.14)/6, (11*3.14)/6,5)
        pygame.draw.arc(screen, (0, 0, 0), (self.x,self.y+40, 50, 50), (7*3.14)/6, (11*3.14)/6,5)
        pygame.draw.arc(screen, (0, 0, 0), (self.x, self.y+60, 50, 50), (7*3.14)/6, (11*3.14)/6,5)
        pygame.draw.arc(screen, (0, 0, 0), (self.x, self.y+80, 50, 50), (7*3.14)/6, (11*3.14)/6,5)


butt = list()

for i in range(5):
    butt.append(butterfly(random.randrange(200,800),random.randrange(200,800)))

#BEGIN GAME LOOP######################################################
while not doExit:
   
   
    #clock.tick(60) #FPS (frames per second)
   
    #pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True #lets you quit program

      
  
     
    #render section-----------------------------------
    screen.fill((0,0,0))

    for butterfly in butt:
        butterfly.draw(random.randrange(200,800),random.randrange(200,800))
 


    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
 
 
 
import pygame
import random

class Snowflake():
    
    def __init__(self):
        self.x=random.randint(0,1600)
        self.y=random.randint(-10,0)
        self.dy=random.randint(1,5)
        self.dx=0
        
class Snowman():
    
    def __init__(self,color,x,y):
        self.color=color
        self.hitpoints=1000
        self.hitpointsfull=1000
        self.image=pygame.surface.Surface((100,200))
        pygame.draw.circle(self.image,color,(50,150),50) #fuss
        pygame.draw.circle(self.image,color,(50,100),40) #bauch
        pygame.draw.circle(self.image,color,(50,50),20) #kopf
        self.crit=50
        self.x=x
        self.y=y
        self.dx=0
        self.dy=0
        self.speed=10#pixel pro sekunde
        self.image.set_colorkey((0,0,0))
        self.image.convert_alpha()

class Ball():
    
    def __init__(self,color,x,y,dx,dy,boss):
        self.color=color
        self.boss=boss
        self.image=pygame.surface.Surface((10,10))
        pygame.draw.circle(self.image,color,(5,5),5) 
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.speed=80#pixel pro sekunde
        self.image.set_colorkey((0,0,0))
        self.image.convert_alpha()

        
class Crosshair():
    def __init__(self,color,x,y):
        self.color=color
        self.image=pygame.surface.Surface((100,100))
        pygame.draw.line(self.image,(0,0,255),(50,50),(50,50),50)
        pygame.draw.line(self.image,(0,0,255),(50,50),(50,50),40)
        pygame.draw.circle(self.image,(50,50),20,1)
        self.x=x
        self.y=y
        self.image.set_colorkey((0,0,0))
        self.image.convert_alpha()
        
class Viewer():
    
    width=800
    height=600
    def __init__(self, maxx=800, maxy=600):
        Viewer.width=maxx
        Viewer.height=maxy             
        pygame.init()
        pygame.joystick.init()
        self.joysticks = [pygame.joystick.Joystick(x) for x in range (
                               pygame.joystick.get_count())]
        for j in self.joysticks:
            j.init()
        
        
        self.screen=pygame.display.set_mode((maxx,maxy))
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((255,255,255))     # fill the background white (red,green,blue)
        self.background = self.background.convert() 
         # faster blitting
        self.clock=pygame.time.Clock()
        self.playtime=0
        self.all=[]
        self.snowman1=Snowman(color=(173,216,230),x=200, y=200)
        self.snowman2=Snowman(color=(255,192,203), x=400, y=300)
        self.snowman1.speed=150
        self.snowman2.speed=150
        self.all.append(self.snowman1)
        self.all.append(self.snowman2)
        
    def run(self):
        running=True
        while running:
            
            milliseconds=self.clock.tick(60)
            seconds=milliseconds/1000.0
            self.playtime +=seconds
            
            
            
            for number , j in enumerate (self.joysticks):
                if number== 0:
                    x= j.get_axis(0)
                    y= j.get_axis(1)
                    x2= j.get_axis(2)
                    y2= j.get_axis(3)
                    buttons = j.get_numbuttons()
                    for b in range (buttons):
                        pushed=j.get_button(b)
                        if pushed and b ==0:
                            self.all.append(
                            Ball(color=(255,30,50),boss=self.snowman1,
                                x=self.snowman1.x+40,
                                y=self.snowman1.y+40,
                                dx=seconds*self.snowman1.speed*x*3,
                                dy=seconds*self.snowman1.speed*y*3))

                                
                    print(x,y)# x,y between -1 and 1
                    self.snowman1.dx=seconds*self.snowman1.speed*x
                    self.snowman1.dy=seconds*self.snowman1.speed*y
                if number==1:
                    x=j.get_axis(0)
                    y=j.get_axis(1)
                    self.snowman2.dx=seconds*self.snowman2.speed*x
                    self.snowman2.dy=seconds*self.snowman2.speed*y
                    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False # pygame window closed by user
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                       running = False # user pressed ESC
                         
                 #------taste(n)sind jetzt gedrückt-----
            pressed_keys=pygame.key.get_pressed()
            #schneeman1 tastatur steuerung
            if pressed_keys[pygame.K_a]:
                self.snowman1.x-=seconds*self.snowman1.speed
            if pressed_keys[pygame.K_d]:
                self.snowman1.x+=seconds*self.snowman1.speed
            if pressed_keys[pygame.K_w]:
                self.snowman1.y-=seconds*self.snowman1.speed
            if pressed_keys[pygame.K_s]:
                self.snowman1.y+=seconds*self.snowman1.speed
                 #schneeman2
            if pressed_keys[pygame.K_LEFT]:
                self.snowman2.x-=seconds*self.snowman2.speed
            if pressed_keys[pygame.K_RIGHT]:
                self.snowman2.x+=seconds*self.snowman2.speed
            if pressed_keys[pygame.K_UP]:
                self.snowman2.y-=seconds*self.snowman2.speed
            if pressed_keys[pygame.K_DOWN]:
                self.snowman2.y+=seconds*self.snowman2.speed
            
            self.screen.blit(self.background, (0,0))
            #lifebar
            balkenweiten=[0,0]
            for i, m in enumerate((self.snowman1,self.snowman2)):
                prozent=m.hitpoints/m.hitpointsfull
                balkenweiten[i]=int(Viewer.width//2*prozent)
            pygame.draw.rect(self.screen,(0,200,0), (0,0,balkenweiten[0],10))
            pygame.draw.rect(self.screen, (0,200,0), (Viewer.width//2,0,
                                                       balkenweiten[1],10))
            newlist=[]
            #hits
            for ball in self.all:
                
                if ball.__class__.__name__=="Snowman":
                    newlist.append(ball)
                    continue
                if ball.boss==self.snowman1:
                    target=self.snowman2
                elif ball.boss==self.snowman2:
                    target=self.snowman1
                distance=((ball.x-target.x)**2+(ball.y-target.y)**2)**0.5
                if distance<target.crit:
                    target.hitpoints-=1
                else:
                    newlist.append(ball)
            self.all=newlist        
                               
            newlist=[]
            for guy in self.all:
                guy.x+=guy.dx
                guy.y+=guy.dy
                
                
                #--kill if out of screen--
                
                if guy.__class__.__name__=="Snowman":
                    newlist.append(guy)
                    continue
                if guy.y <0 or guy.x<0 or guy.y>Viewer.height or guy.x>Viewer.width:
                    pass
                else:
                    newlist.append(guy)
            self.all=newlist
            for guy in self.all:
                xcorr,ycorr=0,0
                if guy.__class__.__name__=="Snowman":
                    xcorr=-5
                    ycorr=-50
                self.screen.blit(guy.image,(guy.x+xcorr,guy.y+ycorr))
                
                
                
            pygame.display.flip()
         
         
if __name__ == "__main__":
    Viewer().run()                

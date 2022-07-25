from colorama import Fore, Back, Style 
import random
from src.buildings import *

class Archer():
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.hitpts = 100
        self.orihitpts = 100
        self.damage = 30
        self.backg = Back.LIGHTMAGENTA_EX + ' ' + Style.RESET_ALL
        self.start_time = -1
        self.is_alive = False
        self.length = 1
        self.breadth = 1
        self.is_attacking = False 
    
    
    def move_arch(self,Used,x,y,tx,ty):
        self.x = x
        self.y = y
        self.tx = tx
        self.ty = ty
        if self.is_alive == True:
            self.temp = 0
            if self.y > self.ty and self.y > 0:
                self.y-=1
                for i in range(self.y,self.y+self.length):
                    for j in range(self.x,self.x+self.breadth):
                         if(Used[i][j] == 1):
                            self.temp = 1
                            break
                    if(self.temp == 1):
                        break
                if(self.temp == 1):
                    self.y+=1
                                  
            elif self.y < self.ty and self.y < 28 :
                self.y+=1
                for i in range(self.y,self.y+self.length):
                    for j in range(self.x,self.x+self.breadth):
                         if(Used[i][j] == 1):
                            self.temp = 1
                            break
                    if(self.temp == 1):
                        break
                if(self.temp == 1):
                    self.y-=1
                
            
            if self.x > self.tx and self.x > 0:
                self.x-=1
                for i in range(self.y,self.y+self.length):
                    for j in range(self.x,self.x+self.breadth):
                         if(Used[i][j] == 1):
                            self.temp = 1
                            break
                    if(self.temp == 1):
                        break
                if(self.temp == 1):
                    self.x+=1
            elif self.x < self.tx and self.x < 78 :
                self.x+=1
                for i in range(self.y,self.y+self.length):
                    for j in range(self.x,self.x+self.breadth):
                         if(Used[i][j] == 1):
                            self.temp = 1
                            break
                    if(self.temp == 1):
                        break
                if(self.temp == 1):
                    self.x-=1
                    
    
    
    
    
    
    
    def dist_from_walls(self,x,y,wx,wy):
        self.x = x
        self.y = y
        self.wx = wx
        self.wy = wy

        self.d_left = (self.x + self.length) - Wall(self.wx,self.wy).x
        self.d_right = (self.x) - (Wall(self.wx,self.wy).x + Wall(self.wx,self.wy).breadth)
        self.d_up = (self.y + self.length) - Wall(self.wx,self.wy).y
        self.d_bottom = (self.y) - (Wall(self.wx,self.wy).y + Wall(self.wx,self.wy).length)
        if ((Wall(self.wx,self.wy).y >= self.y  and Wall(self.wx,self.wy).y <= self.y + self.length) or (Wall(self.wx,self.wy).y + Wall(self.wx,self.wy).length >= self.y and Wall(self.wx,self.wy).y + Wall(self.wx,self.wy).length <= self.y + self.length)) and (self.d_left == 0):
            return 1
        elif ((Wall(self.wx,self.wy).y >= self.y  and Wall(self.wx,self.wy).y <= self.y + self.length) or (Wall(self.wx,self.wy).y + Wall(self.wx,self.wy).length >= self.y and Wall(self.wx,self.wy).y + Wall(self.wx,self.wy).length <= self.y + self.length)) and (self.d_right == 0):
            return 1
        elif ((Wall(self.wx,self.wy).x >= self.x and  Wall(self.wx,self.wy).x <= self.x + self.length) or (Wall(self.wx,self.wy).x + Wall(self.wx,self.wy).length>= self.x and  Wall(self.wx,self.wy).x + Wall(self.wx,self.wy).length <= self.x + self.length )) and (self.d_up == 0):
            return 1
        elif ((Wall(self.wx,self.wy).x >= self.x and  Wall(self.wx,self.wy).x <= self.x + self.length) or (Wall(self.wx,self.wy).x + Wall(self.wx,self.wy).length>= self.x and  Wall(self.wx,self.wy).x + Wall(self.wx,self.wy).length <= self.x + self.length )) and (self.d_bottom == 0):
            return 1
                                  
        return 0
    
    
    def dist_from_TH_EU(self,x,y):
        self.x = x
        self.y = y
        
        return ((self.x - 40)**2 + (self.y - 15)**2)**0.5
    
    def dist_from_buildings_EU(self,x,y,cx,cy):
        self.x = x
        self.y = y
        self.cx = cx
        self.cy = cy
        
        return ((self.x - self.cx)**2 + (self.y - self.cy)**2)**0.5
    
    
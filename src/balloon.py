from colorama import Fore, Back, Style 
import random
from src.buildings import *

class Balloon():
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.hitpts = 200
        self.orihitpts = 200
        self.damage = 120
        self.backg = Back.RED + ' ' + Style.RESET_ALL
        self.start_time = -1
        self.is_alive = False
        self.length = 1
        self.breadth = 1
        self.is_attacking = False 
    
    
    def move_balloon(self,Used,x,y,tx,ty):
        self.x = x
        self.y = y
        self.tx = tx
        self.ty = ty
        if self.is_alive == True:
            self.temp = 0
            if self.y > self.ty and self.y > 0:
                self.y-=1
                
                                  
            elif self.y < self.ty and self.y < 28 :
                self.y+=1
                
                
            
            if self.x > self.tx and self.x > 0:
                self.x-=1
                
            elif self.x < self.tx and self.x < 78 :
                self.x+=1
                
                    
    def dist_from_TH(self,x,y):

        self.x = x
        self.y = y
        
        if self.x == 40 and self.y == 15:
            return 1
               
       
        
        return 0
    
    def dist_from_cannon(self,x,y,cx,cy):
        self.x = x
        self.y = y
        self.cx = cx
        self.cy = cy

        if self.x == self.cx and self.y == self.cy:
            return 1
        
        return 0
    
    def dist_from_huts(self,x,y,hx,hy):
        self.x = x
        self.y = y
        self.hx = hx
        self.hy = hy

        
        if self.x == self.hx and self.y == self.hy:
            return 1    
        
        return 0
    
    
    
    def dist_from_witower(self,x,y,cx,cy):
        self.x = x
        self.y = y
        self.cx = cx
        self.cy = cy

        
        if self.x == self.cx and self.y == self.cy:
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
    
    
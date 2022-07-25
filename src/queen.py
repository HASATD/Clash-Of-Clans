from re import X
from colorama import Fore, Back, Style 
import random
from src.buildings import *
from time import sleep,time



class Queen():
    
    def __init__(self,x,y):        
        self.x = x
        self.y = y
        self.hitpts = 2000
        self.orihitpts = 2000
        self.backg = Back.MAGENTA + ' ' + Style.RESET_ALL
        self.damage = 120
        self.is_alive = False
        self.length = 2
        self.breadth = 2
        self.is_attacking = False        
        self.prev_key = 'a'
        self.atck_x= x
        self.atck_y = y
        self.eagle = 0
        self.eagletimer = 0
        
    def update_queen(self,x,y):
        self.x =  x
        self.y = y
    
    def move_queen(self,key,Used,queen_sleep):
        if self.is_alive == True:            
            self.temp = 0
            if key == 'w' and self.y > 0:                
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
                elif self.temp != 1 :
                    self.prev_key = key
                
                sleep(queen_sleep)
                                  
            elif key == 's' and self.y < 28 :
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
                elif self.temp != 1 :
                    self.prev_key = key
                sleep(queen_sleep)
                
                
            elif key == 'a' and self.x > 0:
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
                elif self.temp != 1 :
                    self.prev_key = key
                sleep(queen_sleep)
                
            elif key == 'd' and self.x < 78 :
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
                elif self.temp != 1 :
                    self.prev_key = key
                sleep(queen_sleep)
                
    
    def dist_from_TH(self,x,y):

        self.x = x
        self.y = y
        self.d_left = (self.x + self.length) - Town_Hall(40,15).x
        self.d_right = (self.x) - (Town_Hall(40,15).x + Town_Hall(40,15).breadth)
        self.d_up = (self.y + self.length) - Town_Hall(40,15).y
        self.d_bottom = (self.y) - (Town_Hall(40,15).y + Town_Hall(40,15).length)
        
        if ((self.y >= Town_Hall(40,15).y and self.y <= Town_Hall(40,15).y+Town_Hall(40,15).length) or (self.y+self.length >= Town_Hall(40,15).y and self.y+self.length <= Town_Hall(40,15).y+Town_Hall(40,15).length)) and (self.d_left == 0):
            return 1
        elif ((self.y >= Town_Hall(40,15).y and self.y <= Town_Hall(40,15).y+Town_Hall(40,15).length) or (self.y+self.length >= Town_Hall(40,15).y and self.y+self.length<= Town_Hall(40,15).y + Town_Hall(40,15).length)) and (self.d_right == 0):
            return 1
        elif ((self.x >= Town_Hall(40,15).x and self.x <=Town_Hall(40,15).x + Town_Hall(40,15).breadth) or (self.x+self.breadth >= Town_Hall(40,15).x and self.x+self.breadth <= Town_Hall(40,15).x + Town_Hall(40,15).breadth)) and (self.d_up == 0):
            return 1
        elif ((self.x >= Town_Hall(40,15).x and self.x <=Town_Hall(40,15).x + Town_Hall(40,15).breadth) or (self.x+self.breadth >= Town_Hall(40,15).x and self.x+self.breadth <= Town_Hall(40,15).x + Town_Hall(40,15).breadth)) and (self.d_bottom == 0):
            return 1
        
        return 0
    
    def dist_from_cannon(self,x,y,cx,cy):
        self.x = x
        self.y = y
        self.cx = cx
        self.cy = cy

        self.d_left = (self.x + self.length) - Cannon(self.cx,self.cy).x
        self.d_right = (self.x) - (Cannon(self.cx,self.cy).x + Cannon(self.cx,self.cy).breadth)
        self.d_up = (self.y + self.length) - Cannon(self.cx,self.cy).y
        self.d_bottom = (self.y) - (Cannon(self.cx,self.cy).y + Cannon(self.cx,self.cy).length)
        
            
        if ((self.y >= Cannon(self.cx,self.cy).y and self.y <= Cannon(self.cx,self.cy).y+Cannon(self.cx,self.cy).length) or (self.y+self.length >= Cannon(self.cx,self.cy).y and self.y+self.length <= Cannon(self.cx,self.cy).y+Cannon(self.cx,self.cy).length)) and (self.d_left == 0):
            return 1
        elif ((self.y >= Cannon(self.cx,self.cy).y and self.y <= Cannon(self.cx,self.cy).y+Cannon(self.cx,self.cy).length) or (self.y+self.length >= Cannon(self.cx,self.cy).y and self.y+self.length<= Cannon(self.cx,self.cy).y + Cannon(self.cx,self.cy).length)) and (self.d_right == 0):
            return 1
        elif ((self.x >= Cannon(self.cx,self.cy).x and self.x <=Cannon(self.cx,self.cy).x + Cannon(self.cx,self.cy).breadth) or (self.x+self.breadth >= Cannon(self.cx,self.cy).x and self.x+self.breadth <= Cannon(self.cx,self.cy).x + Cannon(self.cx,self.cy).breadth)) and (self.d_up == 0):
            return 1
        elif ((self.x >= Cannon(self.cx,self.cy).x and self.x <=Cannon(self.cx,self.cy).x + Cannon(self.cx,self.cy).breadth) or (self.x+self.breadth >= Cannon(self.cx,self.cy).x and self.x+self.breadth <= Cannon(self.cx,self.cy).x + Cannon(self.cx,self.cy).breadth)) and (self.d_bottom == 0):
            return 1    
        
        return 0
    
    def dist_from_witower(self,x,y,cx,cy):
        self.x = x
        self.y = y
        self.cx = cx
        self.cy = cy

        self.d_left = (self.x + self.length) - WiTower(self.cx,self.cy).x
        self.d_right = (self.x) - (WiTower(self.cx,self.cy).x + WiTower(self.cx,self.cy).breadth)
        self.d_up = (self.y + self.length) - WiTower(self.cx,self.cy).y
        self.d_bottom = (self.y) - (WiTower(self.cx,self.cy).y + WiTower(self.cx,self.cy).length)
        
            
        if ((self.y >= WiTower(self.cx,self.cy).y and self.y <= WiTower(self.cx,self.cy).y+WiTower(self.cx,self.cy).length) or (self.y+self.length >= WiTower(self.cx,self.cy).y and self.y+self.length <= WiTower(self.cx,self.cy).y+WiTower(self.cx,self.cy).length)) and (self.d_left == 0):
            return 1
        elif ((self.y >= WiTower(self.cx,self.cy).y and self.y <= WiTower(self.cx,self.cy).y+WiTower(self.cx,self.cy).length) or (self.y+self.length >= WiTower(self.cx,self.cy).y and self.y+self.length<= WiTower(self.cx,self.cy).y + WiTower(self.cx,self.cy).length)) and (self.d_right == 0):
            return 1
        elif ((self.x >= WiTower(self.cx,self.cy).x and self.x <=WiTower(self.cx,self.cy).x + WiTower(self.cx,self.cy).breadth) or (self.x+self.breadth >= WiTower(self.cx,self.cy).x and self.x+self.breadth <= WiTower(self.cx,self.cy).x + WiTower(self.cx,self.cy).breadth)) and (self.d_up == 0):
            return 1
        elif ((self.x >= WiTower(self.cx,self.cy).x and self.x <=WiTower(self.cx,self.cy).x + WiTower(self.cx,self.cy).breadth) or (self.x+self.breadth >= WiTower(self.cx,self.cy).x and self.x+self.breadth <= WiTower(self.cx,self.cy).x + WiTower(self.cx,self.cy).breadth)) and (self.d_bottom == 0):
            return 1    
        
        return 0
    
    def dist_from_huts(self,x,y,hx,hy):
        self.x = x
        self.y = y
        self.hx = hx
        self.hy = hy

        self.d_left = (self.x + self.length) - Hut(self.hx,self.hy).x
        self.d_right = (self.x) - (Hut(self.hx,self.hy).x + Hut(self.hx,self.hy).breadth)
        self.d_up = (self.y + self.length) - Hut(self.hx,self.hy).y
        self.d_bottom = (self.y) - (Hut(self.hx,self.hy).y + Hut(self.hx,self.hy).length)
        if ((self.y >= Hut(self.hx,self.hy).y and self.y <= Hut(self.hx,self.hy).y+Hut(self.hx,self.hy).length) or (self.y+self.length >= Hut(self.hx,self.hy).y and self.y+self.length <= Hut(self.hx,self.hy).y+Hut(self.hx,self.hy).length)) and (self.d_left == 0):
            return 1
        elif ((self.y >= Hut(self.hx,self.hy).y and self.y <= Hut(self.hx,self.hy).y+Hut(self.hx,self.hy).length) or (self.y+self.length >= Hut(self.hx,self.hy).y and self.y+self.length<= Hut(self.hx,self.hy).y + Hut(self.hx,self.hy).length)) and (self.d_right == 0):
            return 1
        elif ((self.x >= Hut(self.hx,self.hy).x and self.x <=Hut(self.hx,self.hy).x + Hut(self.hx,self.hy).breadth) or (self.x+self.breadth >= Hut(self.hx,self.hy).x and self.x+self.breadth <= Hut(self.hx,self.hy).x + Hut(self.hx,self.hy).breadth)) and (self.d_up == 0):
            return 1
        elif ((self.x >= Hut(self.hx,self.hy).x and self.x <=Hut(self.hx,self.hy).x + Hut(self.hx,self.hy).breadth) or (self.x+self.breadth >= Hut(self.hx,self.hy).x and self.x+self.breadth <= Hut(self.hx,self.hy).x + Hut(self.hx,self.hy).breadth)) and (self.d_bottom == 0):
            return 1 
        
        return 0
    
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
    
    
    def dist_from_buildings_EU(self,x,y,cx,cy):
        
        return ((x - cx)**2 + (y - cy)**2)**0.5
        
        
        
        
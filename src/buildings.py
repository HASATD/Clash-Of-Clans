from pickle import FALSE
from colorama import Fore, Back, Style 
import random

class Buildings():
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.length = -1
        self.breadth = -1
        self.hitpts = -1
        
        






class Town_Hall(Buildings):
    
    def __init__(self,x,y):
        super().__init__(x,y)        
        self.length = 3
        self.breadth = 4
        self.orihitpts = 4200        
        self.hitpts = 4200
        self.backg = self.reduced_health()
        self.is_alive = True
        self.is_walled = True
        
    def reduced_health(self):
        
        if (1.0*self.hitpts)/self.orihitpts >= 0.5:
            self.backg = Back.BLACK+ ' ' + Style.RESET_ALL
        elif (1.0*self.hitpts)/self.orihitpts >= 0.2:
            self.backg = Back.LIGHTYELLOW_EX+ ' ' + Style.RESET_ALL
        elif (1.0*self.hitpts)/self.orihitpts >= 0.1:
            self.backg = Back.LIGHTRED_EX+ ' ' + Style.RESET_ALL             
            
    
        return self.backg 

class Cannon(Buildings):
    
    def __init__(self,x,y):
        super().__init__(x,y)
        self.length = 2
        self.breadth = 2
        self.orihitpts = 1060
        self.hitpts = 1060
        self.damage = 74
        self.range = 5
        self.backg = Back.LIGHTBLACK_EX + ' ' + Style.RESET_ALL
        self.is_alive = True
        self.range = 10
        self.is_attacking = [False,False,False,False,False,False,False,False,False,False,False,False,False]
        self.start_time = -1
    
    
        
        
        
class Hut(Buildings): 
    
    def __init__(self,x,y):
        super().__init__(x,y)        
        self.length = 2
        self.breadth = 2
        self.orihitpts = 150        
        self.hitpts = 150
        self.backg = self.reduced_health()
        self.is_alive = True
    def reduced_health(self):
        
        if (1.0*self.hitpts)/self.orihitpts >= 0.5:
            self.backg = Back.CYAN+ ' ' + Style.RESET_ALL
        elif (1.0*self.hitpts)/self.orihitpts >= 0.2:
            self.backg = Back.LIGHTCYAN_EX+ ' ' + Style.RESET_ALL
        elif (1.0*self.hitpts)/self.orihitpts >= 0.1:
            self.backg = Back.LIGHTRED_EX+ ' ' + Style.RESET_ALL        
            
    
        return self.backg 
 
class WiTower(Buildings):
    
    def __init__(self,x,y):
        super().__init__(x,y)
        self.length = 3
        self.breadth = 3
        self.orihitpts = 1060
        self.hitpts = 1060
        self.damage = 74
        self.range = 5
        self.backg = self.reduced_health()
        self.is_alive = True
        self.range = 10
        self.is_attacking = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
        self.start_time = -1
    
    def reduced_health(self):
        
        if (1.0*self.hitpts)/self.orihitpts >= 0.5:
            self.backg = Back.LIGHTBLACK_EX+ ' ' + Style.RESET_ALL
        elif (1.0*self.hitpts)/self.orihitpts >= 0.2:
            self.backg = Back.LIGHTYELLOW_EX+ ' ' + Style.RESET_ALL
        elif (1.0*self.hitpts)/self.orihitpts >= 0.1:
            self.backg = Back.LIGHTRED_EX+ ' ' + Style.RESET_ALL             
            
    
        return self.backg   

class Wall:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.length = 1
        self.breadth = 1
        self.orihitpts = 1000        
        self.hitpts = 1000
        self.backg = Back.BLUE + ' ' + Style.RESET_ALL
        self.is_alive = True
        
        
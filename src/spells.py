from colorama import Fore, Back, Style 
import random



class Spells:
    
    def __init__(self):
        self.is_raged = 0.5
        self.is_notraged = 1
        self.start_time = -1
       
        
    
    
    def heal(self,king,barbarians,loons,archers,queen):
        self.king = king 
        self.barbarians = barbarians
        self.loons = loons
        self.archers = archers
        self.queen = queen
        
        if self.king!= None and self.king.hitpts > 0:
                if self.king.hitpts*(1.5) > self.king.orihitpts:
                    self.king.hitpts = 2000
                else:
                    self.king.hitpts = self.king.hitpts*(1.5)
        
        if self.queen!= None and self.queen.hitpts > 0:
                if self.queen.hitpts*(1.5) > self.queen.orihitpts:
                    self.queen.hitpts = 2000
                else:
                    self.queen.hitpts = self.queen.hitpts*(1.5)
        
        for i in range(len(self.barbarians)):
            if self.barbarians[i]!=None and self.barbarians[i].hitpts > 0:
                if self.barbarians[i].hitpts*(1.5) > self.barbarians[i].orihitpts:
                    self.barbarians[i].hitpts = 200
                else:
                    self.barbarians[i].hitpts = self.barbarians[i].hitpts*(1.5)
        
        for i in range(len(self.archers)):
            if self.archers[i]!=None and self.archers[i].hitpts > 0:
                if self.archers[i].hitpts*(1.5) > self.archers[i].orihitpts:
                    self.archers[i].hitpts = 100
                else:
                    self.archers[i].hitpts = self.archers[i].hitpts*(1.5)
        
        for i in range(len(self.loons)):
            if self.loons[i]!=None and self.loons[i].hitpts > 0:
                if self.loons[i].hitpts*(1.5) > self.loons[i].orihitpts:
                    self.loons[i].hitpts = 200
                else:
                    self.loons[i].hitpts = self.loons[i].hitpts*(1.5)
        
    def rage(self):
        self.is_raged = 0.5
        self.is_notraged = 1
        self.start_time = -1
        
        
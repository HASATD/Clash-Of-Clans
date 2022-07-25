
from colorama import Fore, Back, Style 
from time import sleep,time
from os import system
import os.path
from src.buildings import *
from src.king import *
from src.queen import *
from src.input import *
from src.barbarian import *
from src.archer import *
from src.balloon import *
from src.spawningpoints import *
from time import *
from src.spells import *
import os

class Base():
    
    def __init__(self,level):
        self.level = level
        self.cols = 80
        self.rows = 30
        self.backg = Back.LIGHTGREEN_EX + ' ' + Style.RESET_ALL
        self.TH = Town_Hall(40,15)
        self.Cannon1 = Cannon(28,10)
        self.Cannon2 = Cannon(46,25)
        self.huts = [Hut(2,2)]        
        self.huts.append(Hut(78,2))
        self.huts.append(Hut(78,28))
        self.huts.append(Hut(2,28))
        self.huts.append(Hut(35,22))
        
        self.walls = self.create_walls()
        self.witowers = self.create_witowers()
        self.king = None
        self.queen = None 
        self.base = None
        self.Used = None
        self.barbarians = [None]
        self.archers = [None]
        self.loons = [None]
        self.total_barbs = 5
        self.total_archs = 5
        self.total_loons = 3
        self.livedefs = 0
        self.no_kings = 0
        self.no_queens = 0
        self.Cannons = self.create_cannons()
        self.rage = 1
        self.ragetimer = -1       
        self.spell = Spells()
        self.ragevalue = 1
        self.sleep = 0.5
        self.game_over = -1
        self.replay_no = 1
        self.f_path = ''
        self.rep_file()
        
        
    
    def rep_file(self):
        self.f_path = './replays/replay_' + str(self.replay_no) + '.txt'
        if(os.path.exists(self.f_path) == True):
            self.replay_no += 1
            self.rep_file()   
        
    
        
    def create_walls(self):
        self.walls = [Wall(39,14)]
        self.walls.append(Wall(39,15))
        self.walls.append(Wall(39,16))
        self.walls.append(Wall(39,17))
        self.walls.append(Wall(39,18))
        self.walls.append(Wall(40,14))
        self.walls.append(Wall(41,14))
        self.walls.append(Wall(42,14))
        self.walls.append(Wall(43,14))
        self.walls.append(Wall(44,14))
        self.walls.append(Wall(44,15))
        self.walls.append(Wall(44,16))
        self.walls.append(Wall(44,17))
        self.walls.append(Wall(44,18))
        self.walls.append(Wall(43,18))
        self.walls.append(Wall(42,18))
        self.walls.append(Wall(41,18))
        self.walls.append(Wall(40,18))  
                 
        return self.walls
    
    def create_witowers(self):
        self.witowers = [WiTower(30,13)]
        self.witowers.append(WiTower(47,19))
        if self.level == 2 or self.level == 3:
            self.witowers.append(WiTower(35,18))
        if self.level == 3:
            self.witowers.append(WiTower(23,10))
        return self.witowers
        
        
    
    def create_cannons(self):
        self.Cannons = [Cannon(28,10)]
        self.Cannons.append(Cannon(46,25))
        if self.level == 2 or self.level == 3:
            self.Cannons.append(Cannon(50,25))
        if self.level == 3:
            self.Cannons.append(Cannon(10,15))
        
        return self.Cannons
    
    def Game_Over(self):
        
        
        if (self.king==None and self.queen==None) or self.total_barbs!=0 or self.total_archs!=0 or self.total_loons!=0:                   
            return
            
        
        c = 0
        
        if self.king != None and self.king.hitpts > 0:
            c = 1
        
        if self.queen != None and self.queen.hitpts > 0:
            c = 1
        
        
        for i in range(len(self.barbarians)):
            if self.barbarians[i]!=None and self.barbarians[i].hitpts > 0:
                c+=1
        
        for i in range(len(self.archers)):
            if self.archers[i]!=None and self.archers[i].hitpts > 0:
                c+=1
        for i in range(len(self.loons)):
            if self.loons[i]!=None and self.loons[i].hitpts > 0:
                c+=1
        
        if c == 0:
            self.game_over = 0
            return
        
        c = 0
        
        if self.TH.hitpts > 0:
            c = 1
        
        for i in range(len(self.Cannons)):
            if self.Cannons[i].hitpts > 0:
                c+=1
        
        for i in range(len(self.huts)):
            if self.huts[i].hitpts > 0:
                c+=1
        
        for i in range(len(self.witowers)):
            if self.witowers[i].hitpts > 0:
                c+=1
        
        if c == 0:
            self.game_over = 1
            return
            
        
    
    def queen_attack(self,queen,TH,cannons,witowers,huts,walls,atckptx,atckpty,range):
        self.TH = TH
        self.queen = queen
        self.cannons = cannons
        self.witowers = witowers
        self.huts = huts
        self.walls = walls
        self.atckptx = atckptx
        self.atckpty = atckpty
        self.range = range
        
        if self.TH.hitpts > 0 and self.queen.dist_from_buildings_EU(self.atckptx,self.atckpty,self.TH.x,self.TH.y) <= self.range:
            self.TH.hitpts = self.TH.hitpts - self.queen.damage
            self.TH.backg = Base(self.level).reduced_health(self.TH.hitpts,self.TH.orihitpts,self.TH.backg)
            
        for i in self.cannons:
            if i.hitpts > 0 and self.queen.dist_from_buildings_EU(self.atckptx,self.atckpty,i.x,i.y) <= self.range:
                i.hitpts = i.hitpts - self.queen.damage
                i.backg = Base(self.level).reduced_health(i.hitpts,i.orihitpts,i.backg)
        
        for i in self.witowers:
            if i.hitpts > 0 and self.queen.dist_from_buildings_EU(self.atckptx,self.atckpty,i.x,i.y) <= self.range:
                i.hitpts = i.hitpts - self.queen.damage
                i.backg = Base(self.level).reduced_health(i.hitpts,i.orihitpts,i.backg)
                
        
        for i in self.huts:
            if i.hitpts > 0 and self.queen.dist_from_buildings_EU(self.atckptx,self.atckpty,i.x,i.y) <= self.range:
                i.hitpts = i.hitpts - self.queen.damage
                i.backg = Base(self.level).reduced_health(i.hitpts,i.orihitpts,i.backg)
                
                
        for i in self.walls:
            if i.hitpts > 0 and self.queen.dist_from_buildings_EU(self.atckptx,self.atckpty,i.x,i.y) <= self.range:
                i.hitpts = i.hitpts - self.queen.damage
                i.backg = Base(self.level).reduced_health(i.hitpts,i.orihitpts,i.backg)
                
             
    
    def get_key(self,key):       
        
        if self.Used != None and self.king!=None:            
            self.king.move_king(key,self.Used,self.sleep*self.ragevalue)             
            
        if self.Used != None and self.queen != None:
            self.queen.move_queen(key,self.Used,self.sleep*self.ragevalue)          
        
        if key == 'b' and self.no_kings == 0:
            self.king = King(20,20)
            self.king.is_alive = True
            self.no_kings = 1
            self.no_queens = 1
        
        if key == 'e' and self.no_queens == 0:
            self.queen = Queen(20,20)
            self.queen.is_alive = True 
            self.no_queens = 1
            self.no_kings = 1   
            
        if key == ' ' and self.king!= None and self.king.is_alive == True:            
            if self.king!=None and self.TH.hitpts > 0 and self.king.dist_from_TH(self.king.x,self.king.y) == 1:                
                self.TH.hitpts = self.TH.hitpts - self.king.damage
                self.TH.backg = Base(self.level).reduced_health(self.TH.hitpts,self.TH.orihitpts,self.TH.backg)
                self.king.is_attacking = True
            
            
            elif self.king.is_attacking!=True:
                for i in self.Cannons:
                    if i.hitpts>0 and self.king.dist_from_cannon(self.king.x,self.king.y,i.x,i.y) == 1 and self.king.is_attacking!=True:
                        i.hitpts = i.hitpts - self.king.damage
                        self.king.is_attacking = True
                        i.backg = Base(self.level).reduced_health(i.hitpts,i.orihitpts,i.backg)
                
                for i in self.witowers:
                    if i.hitpts>0 and self.king.dist_from_witower(self.king.x,self.king.y,i.x,i.y) == 1 and self.king.is_attacking!=True:
                        i.hitpts = i.hitpts - self.king.damage
                        self.king.is_attacking = True
                        i.backg = Base(self.level).reduced_health(i.hitpts,i.orihitpts,i.backg)
                
                for i in self.huts:
                    if i.hitpts>0 and self.king.dist_from_huts(self.king.x,self.king.y,i.x,i.y) == 1 and self.king.is_attacking!=True:
                        i.hitpts = i.hitpts - self.king.damage
                        self.king.is_attacking = True
                        i.backg = Base(self.level).reduced_health(i.hitpts,i.orihitpts,i.backg)
                
                for i in self.walls:
                    if i.hitpts>0 and self.king.dist_from_walls(self.king.x,self.king.y,i.x,i.y) == 1 and self.king.is_attacking!=True:
                        i.hitpts = i.hitpts - self.king.damage
                        self.king.is_attacking = True
            
            self.king.is_attacking = False    
            
            if self.rage == 0:
                sleep(0.25)
            else:
                sleep(0.5)        
        
        
        if key == ' ' and self.queen!= None and self.queen.is_alive == True:     
            
            
            if self.queen.prev_key == 'w':                
                Base(self.level).queen_attack(self.queen,self.TH,self.Cannons,self.witowers,self.huts,self.walls,self.queen.x,self.queen.y - 8,5)
            
            elif self.queen.prev_key == 's':
                Base(self.level).queen_attack(self.queen,self.TH,self.Cannons,self.witowers,self.huts,self.walls,self.queen.x,self.queen.y + 8,5)
            
            
            elif self.queen.prev_key == 'a':
                Base(self.level).queen_attack(self.queen,self.TH,self.Cannons,self.witowers,self.huts,self.walls,self.queen.x - 8,self.queen.y,5)
            
            elif self.queen.prev_key == 'd':
                Base(self.level).queen_attack(self.queen,self.TH,self.Cannons,self.witowers,self.huts,self.walls,self.queen.x + 8,self.queen.y,5)

            if self.rage == 0:
                sleep(0.25)
            else:
                sleep(0.5)        
        
        if key == '1' and self.queen!= None and self.queen.is_alive == True:        
           
            if self.queen.eagle == 0:
                self.queen.eagle = 1
                self.queen.eagletimer = time()
                 
                if self.queen.prev_key == 'w':   
                    self.queen.atck_x = self.queen.x
                    self.queen.atck_y = self.queen.y - 16         
                
                elif self.queen.prev_key == 's':
                        self.queen.atck_x = self.queen.x
                        self.queen.atck_y = self.queen.y + 16  
                
                elif self.queen.prev_key == 'a':
                        self.queen.atck_x = self.queen.x - 16
                        self.queen.atck_y = self.queen.y    
                
                elif self.queen.prev_key == 'd':
                        self.queen.atck_x = self.queen.x + 16
                        self.queen.atck_y = self.queen.y    
                        
                
                        
                
            

              
        
        if key == 'i' and self.total_barbs > 0:
            self.total_barbs -= 1
            self.barbarians.append(Barbarian(Spawn_pts().x1,Spawn_pts().y1))            
            self.barbarians[-1].is_alive = True
        
        if key == 'j' and self.total_barbs > 0:
            self.total_barbs -= 1
            self.barbarians.append(Barbarian(Spawn_pts().x2,Spawn_pts().y2))            
            self.barbarians[-1].is_alive = True
        
        if key == 'k' and self.total_barbs>0:
            self.total_barbs -= 1
            self.barbarians.append(Barbarian(Spawn_pts().x3,Spawn_pts().y3))            
            self.barbarians[-1].is_alive = True
        
        if key == 'x' and self.total_archs > 0:
            self.total_archs -= 1
            self.archers.append(Archer(Spawn_pts().x4,Spawn_pts().y4))            
            self.archers[-1].is_alive = True
       
        if key == 'y' and self.total_archs > 0:
            self.total_archs -= 1
            self.archers.append(Archer(Spawn_pts().x5,Spawn_pts().y5))            
            self.archers[-1].is_alive = True
        
        if key == 'z' and self.total_archs > 0:
            self.total_archs -= 1
            self.archers.append(Archer(Spawn_pts().x6,Spawn_pts().y6))            
            self.archers[-1].is_alive = True
        
        if key == 'm' and self.total_loons > 0:
            self.total_loons -= 1
            self.loons.append(Balloon(Spawn_pts().x7,Spawn_pts().y7))            
            self.loons[-1].is_alive = True
        
        if key == 'n' and self.total_loons > 0:
            self.total_loons -= 1
            self.loons.append(Balloon(Spawn_pts().x8,Spawn_pts().y8))            
            self.loons[-1].is_alive = True
        
        if key == 'o' and self.total_loons > 0:
            self.total_loons -= 1
            self.loons.append(Balloon(Spawn_pts().x9,Spawn_pts().y9))            
            self.loons[-1].is_alive = True
        
        
            
           
        if key == 'h':                        
            self.spell.heal(self.king,self.barbarians,self.loons,self.archers,self.queen)
            
        
        if time() -  self.spell.start_time >= 5 and self.rage == 0:            
              self.ragevalue = 1
              self.backg = Back.LIGHTGREEN_EX + ' ' + Style.RESET_ALL
              
                        
        if key == 'r' and self.rage == 1:
            self.backg = Back.LIGHTRED_EX + ' ' + Style.RESET_ALL
            self.rage = self.rage - 1
            self.spell.start_time = time()
            self.ragevalue = 0.5   
            
            
        if key == 'l' and self.king!=None and self.king.hitpts > 0:
            if self.king.dist_from_buildings_EU(self.king.x,self.king.y,self.TH.x,self.TH.y) <= 5:
                self.TH.hitpts = self.TH.hitpts - 300
                self.TH.backg = Base(self.level).reduced_health(self.TH.hitpts,self.TH.orihitpts,self.TH.backg)
            
            for i in self.Cannons:
                if self.king.dist_from_buildings_EU(self.king.x,self.king.y,i.x,i.y) <= 5:
                    i.hitpts = i.hitpts - 300
                    i.backg = Base(self.level).reduced_health(i.hitpts,i.orihitpts,i.backg)
                    
                    
            
            for i in self.huts:
                if self.king.dist_from_buildings_EU(self.king.x,self.king.y,i.x,i.y) <= 5:
                     i.hitpts = i.hitpts - 300
                     i.backg = Base(self.level).reduced_health(i.hitpts,i.orihitpts,i.backg)
                     
            
            for i in self.walls:
                if self.king.dist_from_buildings_EU(self.king.x,self.king.y,i.x,i.y) <= 5:
                     i.hitpts = i.hitpts - 300         
                
                
            
            
            
            
    def reduced_health_canwiz(self,hitpts,orihitpts,backg):
        self.hitpts = hitpts
        self.backg = backg
        self.orihitpts = orihitpts
        if (1.0*self.hitpts)/self.orihitpts >= 0.5:
            self.backg = Back.LIGHTBLACK_EX + ' ' + Style.RESET_ALL
        elif (1.0*self.hitpts)/self.orihitpts >= 0.2 and (1.0*self.hitpts)/self.orihitpts <= 0.5:
            self.backg = Back.LIGHTYELLOW_EX+ ' ' + Style.RESET_ALL
        elif (1.0*self.hitpts)/self.orihitpts <= 0.2 and (1.0*self.hitpts)/self.orihitpts >= 0.1:
            self.backg = Back.LIGHTRED_EX+ ' ' + Style.RESET_ALL 
        elif (1.0*self.hitpts)/self.orihitpts <= 0.1:
            self.backg = Back.RED + ' ' + Style.RESET_ALL
            
        return self.backg
    def reduced_health(self,hitpts,orihitpts,backg):
        self.hitpts = hitpts
        self.backg = backg
        self.orihitpts = orihitpts
        
        if (1.0*self.hitpts)/self.orihitpts >= 0.2 and (1.0*self.hitpts)/self.orihitpts <= 0.5:
            self.backg = Back.LIGHTYELLOW_EX+ ' ' + Style.RESET_ALL
        elif (1.0*self.hitpts)/self.orihitpts <= 0.2 and (1.0*self.hitpts)/self.orihitpts >= 0.1:
            self.backg = Back.LIGHTRED_EX+ ' ' + Style.RESET_ALL 
        elif (1.0*self.hitpts)/self.orihitpts <= 0.1:
            self.backg = Back.RED + ' ' + Style.RESET_ALL
            
        return self.backg
        
    
    def Cannon_attack(self,cannon,king,queen,barbarians,archers):
        self.king = king
        self.barbarians = barbarians 
        self.archers = archers
        self.queen = queen
        self.temp = 0
        if self.king!=None and self.king.is_alive == True and self.king.dist_from_buildings_EU(self.king.x,self.king.y,cannon.x,cannon.y) <= 10:
            for i in range(len(cannon.is_attacking)):
                if cannon.is_attacking[i] == True:
                    self.temp = 1
            
            if self.temp == 0 or cannon.is_attacking[0] == True:        
                cannon.is_attacking[0] = True
                self.king.hitpts = self.king.hitpts - cannon.damage
                
                if self.king.hitpts <= 0:
                    cannon.is_attacking[0] = False                    
                    self.king.is_alive = False
        elif self.king!=None and self.king.dist_from_buildings_EU(self.king.x,self.king.y,cannon.x,cannon.y) > 10 and cannon.is_attacking[0] == True:
            cannon.is_attacking[0] = False
        
        elif self.king!=None and self.king.is_alive == False:
            cannon.is_attacking[0] = False
        
        self.temp = 0
        
        if self.queen!=None and self.queen.is_alive == True and self.queen.dist_from_buildings_EU(self.queen.x,self.queen.y,cannon.x,cannon.y) <= 10:
            for i in range(len(cannon.is_attacking)):
                if cannon.is_attacking[i] == True:
                    self.temp = 1
            
            if self.temp == 0 or cannon.is_attacking[0] == True:        
                cannon.is_attacking[0] = True
                self.queen.hitpts = self.queen.hitpts - cannon.damage
                
                if self.queen.hitpts <= 0:
                    cannon.is_attacking[0] = False
                    
                    self.queen.is_alive = False
        elif self.queen!=None and self.queen.dist_from_buildings_EU(self.queen.x,self.queen.y,cannon.x,cannon.y) > 10 and cannon.is_attacking[0] == True:
            cannon.is_attacking[0] = False
        elif self.queen!=None and self.queen.is_alive == False:
            cannon.is_attacking[0] = False 
        
            
        
        self.temp = 0
        
        for i in range(len(self.barbarians)):
            if self.barbarians[i]!=None and self.barbarians[i].is_alive == True and self.barbarians[i].dist_from_buildings_EU(self.barbarians[i].x,self.barbarians[i].y,cannon.x,cannon.y) <= 10:
                for j in range(len(cannon.is_attacking)):
                    if cannon.is_attacking[j] == True:
                        self.temp = 1
                
                if self.temp == 0 or cannon.is_attacking[i+1] == True:
                    cannon.is_attacking[i+1] = True
                    self.barbarians[i].hitpts = self.barbarians[i].hitpts - cannon.damage
                    
                    
                    if self.barbarians[i].hitpts <= 0:
                        cannon.is_attacking[i+1] = False
                        
                        self.barbarians[i].is_alive = False
            elif self.barbarians[i] != None and self.barbarians[i].dist_from_buildings_EU(self.barbarians[i].x,self.barbarians[i].y,cannon.x,cannon.y) <= 10:
                cannon.is_attacking[i+1] = False
            elif self.barbarians[i] != None and self.barbarians[i].is_alive == False:
                cannon.is_attacking[i+1] = False
               
            self.temp = 0
        
        for i in range(len(self.archers)):
            if self.archers[i]!=None and self.archers[i].is_alive == True and self.archers[i].dist_from_buildings_EU(self.archers[i].x,self.archers[i].y,cannon.x,cannon.y) <= 10:
                for j in range(len(cannon.is_attacking)):
                    if cannon.is_attacking[j] == True:
                        self.temp = 1
                
                if self.temp == 0 or cannon.is_attacking[i+7] == True:
                    cannon.is_attacking[i+7] = True
                    self.archers[i].hitpts = self.archers[i].hitpts - cannon.damage
                    
                    
                    if self.archers[i].hitpts <= 0:
                        cannon.is_attacking[i+7] = False
                        
                        self.archers[i].is_alive = False
            elif self.archers[i] != None and self.archers[i].dist_from_buildings_EU(self.archers[i].x,self.archers[i].y,cannon.x,cannon.y) <= 10:
                cannon.is_attacking[i+7] = False
            elif self.archers[i] != None and self.archers[i].is_alive == False:
                cannon.is_attacking[i+7] = False
            
            self.temp = 0
        for i in range(len(cannon.is_attacking)):
            if cannon.is_attacking[i] == True:
                cannon.backg = Back.BLACK + ' ' +  Style.RESET_ALL
                self.temp = 1
                break
        if self.temp == 0:            
            cannon.backg = Base(self.level).reduced_health_canwiz(cannon.hitpts,cannon.orihitpts,cannon.backg)
            
        self.temp = 0
    
    
    
    def attack_group(self,witower,king,queen,barbarians,loons,archers,atckptx,atckpty):
        self.king = king 
        self.queen = queen
        self.barbarians = barbarians
        self.loons = loons 
        self.archers = archers 
        self.atckptx = atckptx 
        self.atckpty = atckpty
        self.witower = witower 
        
        if self.king!=None and self.king.is_alive == True and self.king.dist_from_buildings_EU(self.king.x,self.king.y,self.atckptx,self.atckpty) <= 3:
            self.king.hitpts = self.king.hitpts - self.witower.damage
       
        if self.queen!=None and self.queen.is_alive == True and self.queen.dist_from_buildings_EU(self.queen.x,self.queen.y,self.atckptx,self.atckpty) <= 3:
            self.queen.hitpts = self.queen.hitpts - self.witower.damage
        
        for i in range(len(self.barbarians)):
            if self.barbarians[i]!=None and self.barbarians[i].is_alive == True and self.barbarians[i].dist_from_buildings_EU(self.barbarians[i].x,self.barbarians[i].y,self.atckptx,self.atckpty) <= 3:
               self.barbarians[i].hitpts = self.barbarians[i].hitpts - self.witower.damage
        
        for i in range(len(self.archers)):
            if self.archers[i]!=None and self.archers[i].is_alive == True and self.archers[i].dist_from_buildings_EU(self.archers[i].x,self.archers[i].y,self.atckptx,self.atckpty) <= 3:
               self.archers[i].hitpts = self.archers[i].hitpts - self.witower.damage            
                    
        for i in range(len(self.loons)):
            if self.loons[i]!=None and self.loons[i].is_alive == True and self.loons[i].dist_from_buildings_EU(self.loons[i].x,self.loons[i].y,self.atckptx,self.atckpty) <= 3:
               self.loons[i].hitpts = self.loons[i].hitpts - self.witower.damage           
                        
              
            
    
    
    def Witower_attack(self,witower,king,queen,barbarians,loons,archers):
        self.king = king
        self.queen = queen
        self.barbarians = barbarians 
        self.loons = loons
        self.archers = archers
        self.witower = witower
        self.temp = 0
        if self.king!=None and self.king.is_alive == True and self.king.dist_from_buildings_EU(self.king.x,self.king.y,self.witower.x,self.witower.y) <= 10:
            for i in range(len(self.witower.is_attacking)):
                if self.witower.is_attacking[i] == True:
                    self.temp = 1
            
            if self.temp == 0 or self.witower.is_attacking[0] == True:        
                self.witower.is_attacking[0] = True
                Base(self.level).attack_group(self.witower,self.king,self.queen,self.barbarians,self.loons,self.archers,self.king.x,self.king.y)
                
                if self.king.hitpts <= 0:
                    self.witower.is_attacking[0] = False
                    
                    self.king.is_alive = False
        elif self.king!=None and self.king.dist_from_buildings_EU(self.king.x,self.king.y,self.witower.x,self.witower.y) > 10 and self.witower.is_attacking[0] == True:
            self.witower.is_attacking[0] = False
        
        elif self.king!=None and self.king.is_alive == False:
            self.witower.is_attacking[0] = False
        
            
        
        self.temp = 0
        
        if self.queen!=None and self.queen.is_alive == True and self.queen.dist_from_buildings_EU(self.queen.x,self.queen.y,self.witower.x,self.witower.y) <= 10:
            for i in range(len(self.witower.is_attacking)):
                if self.witower.is_attacking[i] == True:
                    self.temp = 1
            
            if self.temp == 0 or self.witower.is_attacking[0] == True:        
                self.witower.is_attacking[0] = True
                Base(self.level).attack_group(self.witower,self.king,self.queen,self.barbarians,self.loons,self.archers,self.queen.x,self.queen.y)
                
                if self.queen.hitpts <= 0:
                    self.witower.is_attacking[0] = False
                    
                    self.queen.is_alive = False
        elif self.queen!=None and self.queen.dist_from_buildings_EU(self.queen.x,self.queen.y,self.witower.x,self.witower.y) > 10 and self.witower.is_attacking[0] == True:
            self.witower.is_attacking[0] = False
        elif self.queen!=None and self.queen.is_alive == False:
            self.witower.is_attacking[0] = False
            
        
        self.temp = 0
        
        for i in range(len(self.barbarians)):
            if self.barbarians[i]!=None and self.barbarians[i].is_alive == True and self.barbarians[i].dist_from_buildings_EU(self.barbarians[i].x,self.barbarians[i].y,self.witower.x,self.witower.y) <= 10:
                for j in range(len(self.witower.is_attacking)):
                    if self.witower.is_attacking[j] == True:
                        self.temp = 1
                
                if self.temp == 0 or self.witower.is_attacking[i+1] == True:
                    self.witower.is_attacking[i+1] = True
                    Base(self.level).attack_group(self.witower,self.king,self.queen,self.barbarians,self.loons,self.archers,self.barbarians[i].x,self.barbarians[i].y)
                    
                    
                    
                    if self.barbarians[i].hitpts <= 0:
                        self.witower.is_attacking[i+1] = False
                        
                        self.barbarians[i].is_alive = False
            elif self.barbarians[i] != None and self.barbarians[i].dist_from_buildings_EU(self.barbarians[i].x,self.barbarians[i].y,self.witower.x,self.witower.y) <= 10:
                self.witower.is_attacking[i+1] = False
            elif self.barbarians[i]!=None and self.barbarians[i].is_alive == False:
                self.witower.is_attacking[i+1] = False
               
            self.temp = 0
            
        for i in range(len(self.archers)):
            if self.archers[i]!=None and self.archers[i].is_alive == True and self.archers[i].dist_from_buildings_EU(self.archers[i].x,self.archers[i].y,self.witower.x,self.witower.y) <= 10:
                for j in range(len(self.witower.is_attacking)):
                    if self.witower.is_attacking[j] == True:
                        self.temp = 1
                
                if self.temp == 0 or self.witower.is_attacking[i+7] == True:
                    self.witower.is_attacking[i+7] = True                    
                    Base(self.level).attack_group(self.witower,self.king,self.queen,self.barbarians,self.loons,self.archers,self.archers[i].x,self.archers[i].y)
                    
                    
                    
                    if self.archers[i].hitpts <= 0:
                        self.witower.is_attacking[i+7] = False
                        
                        self.archers[i].is_alive = False
            elif self.archers[i] != None and self.archers[i].dist_from_buildings_EU(self.archers[i].x,self.archers[i].y,self.witower.x,self.witower.y) <= 10:
                self.witower.is_attacking[i+7] = False
            elif self.archers[i]!=None and self.archers[i].is_alive == False:
                self.witower.is_attacking[i+7] = False
               
            self.temp = 0
        
        for i in range(len(self.loons)):
            if self.loons[i]!=None and self.loons[i].is_alive == True and self.loons[i].dist_from_buildings_EU(self.loons[i].x,self.loons[i].y,self.witower.x,self.witower.y) <= 10:
                for j in range(len(self.witower.is_attacking)):
                    if self.witower.is_attacking[j] == True:
                        self.temp = 1
                
                if self.temp == 0 or self.witower.is_attacking[i+13] == True:
                    self.witower.is_attacking[i+13] = True                    
                    Base(self.level).attack_group(self.witower,self.king,self.queen,self.barbarians,self.loons,self.archers,self.loons[i].x,self.loons[i].y)
                    
                    
                    
                    if self.loons[i].hitpts <= 0:
                        self.witower.is_attacking[i+13] = False
                        
                        self.loons[i].is_alive = False
            elif self.loons[i] != None and self.loons[i].dist_from_buildings_EU(self.loons[i].x,self.loons[i].y,self.witower.x,self.witower.y) <= 10:
                self.witower.is_attacking[i+13] = False
            elif self.loons[i]!=None and self.loons[i].is_alive == False:
                self.witower.is_attacking[i+13] = False
               
               
            self.temp = 0
               
        for i in range(len(self.witower.is_attacking)):
            if self.witower.is_attacking[i] == True:
                self.witower.backg = Back.BLACK + ' ' +  Style.RESET_ALL
                self.temp = 1
                break
        if self.temp == 0:
            
            self.witower.backg = Base(self.level).reduced_health_canwiz(self.witower.hitpts,self.witower.orihitpts,self.witower.backg)
            
        self.temp = 0
            
    
   
    
        
    def move_barbarians(self,barbarians,TH,cannons,huts,walls,witowers):
        self.barbarians = barbarians
        self.TH = TH
        self.cannons = cannons
        self.witowers = witowers
        self.huts = huts
        self.walls = walls
        self.min_dist = 100000    
        self.cords = [self.barbarians.x,self.barbarians.y]           
        for i in self.cannons:  
            if i.hitpts > 0:   
                if self.min_dist > self.barbarians.dist_from_buildings_EU(self.barbarians.x,self.barbarians.y,i.x,i.y):
                    self.min_dist = self.barbarians.dist_from_buildings_EU(self.barbarians.x,self.barbarians.y,i.x,i.y)
                    self.cords[0] = i.x
                    self.cords[1] = i.y
        
        if self.TH.is_walled == False and self.TH.hitpts > 0:
                if self.min_dist > self.barbarians.dist_from_buildings_EU(self.barbarians.x,self.barbarians.y,self.TH.x,self.TH.y):
                    self.min_dist = self.barbarians.dist_from_buildings_EU(self.barbarians.x,self.barbarians.y,self.TH.x,self.TH.y)
                    self.cords[0] = self.TH.x
                    self.cords[1] = self.TH.y
                    
        for i in self.witowers:
            if i.hitpts > 0:
                if self.min_dist > self.barbarians.dist_from_buildings_EU(self.barbarians.x,self.barbarians.y,i.x,i.y):
                    self.min_dist = self.barbarians.dist_from_buildings_EU(self.barbarians.x,self.barbarians.y,i.x,i.y)
                    self.cords[0] = i.x
                    self.cords[1] = i.y
                
        
        for i in self.huts:
            if i.hitpts > 0:   
                if self.min_dist > self.barbarians.dist_from_buildings_EU(self.barbarians.x,self.barbarians.y,i.x,i.y):
                    self.min_dist = self.barbarians.dist_from_buildings_EU(self.barbarians.x,self.barbarians.y,i.x,i.y)
                    self.cords[0] = i.x 
                    self.cords[1] = i.y
        
        return self.cords
    
    def move_loons(self,loons,TH,cannons,huts,walls,witowers):
        self.loons = loons
        self.TH = TH
        self.cannons = cannons
        self.witowers = witowers
        self.huts = huts
        self.walls = walls
        self.min_dist = 100000    
        self.cords = [self.loons.x,self.loons.y]      
        self.livedef = 0     
        for i in self.cannons:  
            if i.hitpts > 0:
                self.livedef = 1   
                if self.min_dist > self.loons.dist_from_buildings_EU(self.loons.x,self.loons.y,i.x,i.y):
                    self.min_dist = self.loons.dist_from_buildings_EU(self.loons.x,self.loons.y,i.x,i.y)
                    self.cords[0] = i.x
                    self.cords[1] = i.y
                    
                                   
        for i in self.witowers:
            if i.hitpts > 0:
                self.livedef = 1
                if self.min_dist > self.loons.dist_from_buildings_EU(self.loons.x,self.loons.y,i.x,i.y):
                    self.min_dist = self.loons.dist_from_buildings_EU(self.loons.x,self.loons.y,i.x,i.y)
                    self.cords[0] = i.x
                    self.cords[1] = i.y
        
        if self.livedef == 0:
            if  self.TH.hitpts > 0:
                if self.min_dist > self.loons.dist_from_buildings_EU(self.loons.x,self.loons.y,self.TH.x,self.TH.y):
                    self.min_dist = self.loons.dist_from_buildings_EU(self.loons.x,self.loons.y,self.TH.x,self.TH.y)
                    self.cords[0] = self.TH.x
                    self.cords[1] = self.TH.y        
        
            for i in self.huts:
                if i.hitpts > 0:   
                    if self.min_dist > self.loons.dist_from_buildings_EU(self.loons.x,self.loons.y,i.x,i.y):
                        self.min_dist = self.loons.dist_from_buildings_EU(self.loons.x,self.loons.y,i.x,i.y)
                        self.cords[0] = i.x 
                        self.cords[1] = i.y
            
               
        
        
        return self.cords
             
       
    def move_archers(self,archers,TH,cannons,huts,walls,witowers):
        self.archers = archers
        self.TH = TH
        self.cannons = cannons
        self.witowers = witowers
        self.huts = huts
        self.walls = walls
        self.min_dist = 100000    
        self.cords = [self.archers.x,self.archers.y]           
        for i in self.cannons:  
            if i.hitpts > 0:   
                if self.min_dist > self.archers.dist_from_buildings_EU(self.archers.x,self.archers.y,i.x,i.y):
                    self.min_dist = self.archers.dist_from_buildings_EU(self.archers.x,self.archers.y,i.x,i.y)
                    self.cords[0] = i.x
                    self.cords[1] = i.y
        
        if self.TH.hitpts > 0:
                if self.min_dist > self.archers.dist_from_buildings_EU(self.archers.x,self.archers.y,self.TH.x,self.TH.y):
                    self.min_dist = self.archers.dist_from_buildings_EU(self.archers.x,self.archers.y,self.TH.x,self.TH.y)
                    self.cords[0] = self.TH.x
                    self.cords[1] = self.TH.y
                    
        for i in self.witowers:
            if i.hitpts > 0:
                if self.min_dist > self.archers.dist_from_buildings_EU(self.archers.x,self.archers.y,i.x,i.y):
                    self.min_dist = self.archers.dist_from_buildings_EU(self.archers.x,self.archers.y,i.x,i.y)
                    self.cords[0] = i.x
                    self.cords[1] = i.y
                
        
        for i in self.huts:
            if i.hitpts > 0:   
                if self.min_dist > self.archers.dist_from_buildings_EU(self.archers.x,self.archers.y,i.x,i.y):
                    self.min_dist = self.archers.dist_from_buildings_EU(self.archers.x,self.archers.y,i.x,i.y)
                    self.cords[0] = i.x 
                    self.cords[1] = i.y
        
        return self.cords    
            
            
             
               
        
    def render(self):
        system('clear')
        self.base = [[self.backg for i in range(self.cols)] for j in range(self.rows)]
        
        self.Used = [[0 for i in range(self.cols)] for j in range(self.rows)]
        
        
       
        
        if self.TH.hitpts > 0:
            for i in range(self.TH.y,self.TH.y+self.TH.length):
               for j in range(self.TH.x,self.TH.x+self.TH.breadth):
                   self.base[i][j] = self.TH.backg
                   self.Used[i][j] = 1
        elif self.TH.hitpts <= 0:
            self.TH.is_alive = False
                    
        
        for i in range(len(self.Cannons)):
            if self.Cannons[i].hitpts > 0:
                for j in range(self.Cannons[i].y,self.Cannons[i].y+self.Cannons[i].length):
                    for k in range(self.Cannons[i].x,self.Cannons[i].x+self.Cannons[i].breadth):                    
                        self.base[j][k] = self.Cannons[i].backg
                        self.Used[j][k] = 1
            elif self.Cannons[i].hitpts <= 0:
                self.Cannons[i].is_alive = False
        
        for i in range(len(self.huts)):
            if self.huts[i].hitpts > 0:
                for j in range(self.huts[i].y,self.huts[i].y+self.huts[i].length):
                    for k in range(self.huts[i].x,self.huts[i].x+self.huts[i].breadth):                    
                        self.base[j][k] = self.huts[i].backg
                        self.Used[j][k] = 1
            elif self.huts[i].hitpts <= 0:
                self.huts[i].is_alive = False
                
        for i in range(len(self.witowers)):
                if self.witowers[i].hitpts > 0:
                    for j in range(self.witowers[i].y,self.witowers[i].y+self.witowers[i].length):
                        for k in range(self.witowers[i].x,self.witowers[i].x+self.witowers[i].breadth):                    
                            self.base[j][k] = self.witowers[i].backg
                            self.Used[j][k] = 1
                elif self.witowers[i].hitpts <= 0:
                    self.witowers[i].is_alive = False    
            
                    
                    
        for i in range(len(self.walls)):  
            if self.walls[i].hitpts > 0:
                for j in range(self.walls[i].y,self.walls[i].y+self.walls[i].length):
                    for k in range(self.walls[i].x,self.walls[i].x+self.walls[i].breadth):                                       
                        self.base[j][k] = self.walls[i].backg
                        self.Used[j][k] = 1
            elif self.walls[i].hitpts <= 0:
                self.walls[i].is_alive = False
                self.TH.is_walled = False  
            
        
        
        
        if self.king != None and self.king.hitpts > 0:             
            for i in range(self.king.y,self.king.y+self.king.length):
                for j in range(self.king.x,self.king.x+self.king.breadth):
                    self.base[i][j] = self.king.backg
        
        elif self.king!=None and self.king.hitpts <= 0:
            self.king.is_alive = False 
        
        
        if self.queen != None and self.queen.hitpts > 0:             
            for i in range(self.queen.y,self.queen.y+self.queen.length):
                for j in range(self.queen.x,self.queen.x+self.queen.breadth):
                    self.base[i][j] = self.queen.backg
        
        elif self.queen!=None and self.queen.hitpts <= 0:
            self.queen.is_alive = False 
            
        for i in range(len(self.barbarians)):
            if self.barbarians[i]!=None and self.barbarians[i].hitpts > 0:
                for j in range(self.barbarians[i].y , self.barbarians[i].y+self.barbarians[i].length):
                    for k in range(self.barbarians[i].x,self.barbarians[i].x+self.barbarians[i].breadth):
                        self.base[j][k] = self.barbarians[i].backg
            
            elif self.barbarians[i]!=None and self.barbarians[i].hitpts <= 0:
                self.barbarians[i].is_alive = False            
        
        for i in range(len(self.loons)):
            if self.loons[i]!=None and self.loons[i].hitpts > 0:
                for j in range(self.loons[i].y , self.loons[i].y+self.loons[i].length):
                    for k in range(self.loons[i].x,self.loons[i].x+self.loons[i].breadth):
                        self.base[j][k] = self.loons[i].backg
            
            elif self.loons[i]!=None and self.loons[i].hitpts <= 0:
                self.loons[i].is_alive = False   
        
        for i in range(len(self.archers)):
            if self.archers[i]!=None and self.archers[i].hitpts > 0:
                for j in range(self.archers[i].y , self.archers[i].y+self.archers[i].length):
                    for k in range(self.archers[i].x,self.archers[i].x+self.archers[i].breadth):
                        self.base[j][k] = self.archers[i].backg
            
            elif self.archers[i]!=None and self.archers[i].hitpts <= 0:
                self.archers[i].is_alive = False 
        
        
        for i in range(len(self.Cannons)):
            if self.Cannons[i].is_alive == True and time()-self.Cannons[i].start_time >= 1:
                Base(self.level).Cannon_attack(self.Cannons[i],self.king,self.queen,self.barbarians,self.archers)            
                self.Cannons[i].start_time = time()
        
        for i in range(len(self.witowers)):
            if self.witowers[i].is_alive == True and time()-self.witowers[i].start_time >= 1:
                Base(self.level).Witower_attack(self.witowers[i],self.king,self.queen,self.barbarians,self.loons,self.archers)            
                self.witowers[i].start_time = time()
        
        if self.queen!=None and self.queen.is_alive == True and self.queen.eagle == 1 and time() - self.queen.eagletimer >= 1:
            Base(self.level).queen_attack(self.queen,self.TH,self.Cannons,self.witowers,self.huts,self.walls,self.queen.atck_x,self.queen.atck_y,9)
            self.queen.eagle = 0
                
        
                
        for j in range(len(self.barbarians)):
            if self.barbarians[j]!=None and self.barbarians[j].hitpts > 0:
                if time() - self.barbarians[j].start_time >= 1*self.ragevalue :                    
                    self.barbarians[j].move_barb(self.Used,self.barbarians[j].x,self.barbarians[j].y,Base(self.level).move_barbarians(self.barbarians[j],self.TH,self.Cannons,self.huts,self.walls,self.witowers)[0],Base(self.level).move_barbarians(self.barbarians[j],self.TH,self.Cannons,self.huts,self.walls,self.witowers)[1])
                                                  
                    if  self.barbarians[j].is_alive == True and self.barbarians[j]!= None:
                        if self.barbarians[j]!=None and self.TH.hitpts > 0 and self.barbarians[j].dist_from_TH(self.barbarians[j].x,self.barbarians[j].y) == 1:                
                            self.TH.hitpts = self.TH.hitpts - self.barbarians[j].damage
                            self.TH.backg = Base(self.level).reduced_health(self.TH.hitpts,self.TH.orihitpts,self.TH.backg)
                            self.barbarians[j].is_attacking = True
                       
                       
                        
                        elif self.barbarians[j].is_attacking!=True:
                            
                            for i in self.Cannons:
                                if i.hitpts>0 and self.barbarians[j].dist_from_cannon(self.barbarians[j].x,self.barbarians[j].y,i.x,i.y) == 1 and self.barbarians[j].is_attacking!=True:
                                    i.hitpts = i.hitpts - self.barbarians[j].damage
                                    self.barbarians[j].is_attacking = True
                                    i.backg = Base(self.level).reduced_health(i.hitpts,i.orihitpts,i.backg)
                            for i in self.witowers:
                                if i.hitpts>0 and self.barbarians[j].dist_from_witower(self.barbarians[j].x,self.barbarians[j].y,i.x,i.y) == 1 and self.barbarians[j].is_attacking!=True:
                                    i.hitpts = i.hitpts - self.barbarians[j].damage
                                    self.barbarians[j].is_attacking = True
                                    i.backg = Base(self.level).reduced_health(i.hitpts,i.orihitpts,i.backg)
                                
                            for i in self.huts:
                                if i.hitpts>0 and self.barbarians[j].dist_from_huts(self.barbarians[j].x,self.barbarians[j].y,i.x,i.y) == 1 and self.barbarians[j].is_attacking!=True:
                                    i.hitpts = i.hitpts - self.barbarians[j].damage
                                    self.barbarians[j].is_attacking = True
                                    i.backg = Base(self.level).reduced_health(i.hitpts,i.orihitpts,i.backg)
                            
                            for i in self.walls:
                                if i.hitpts>0 and self.barbarians[j].dist_from_walls(self.barbarians[j].x,self.barbarians[j].y,i.x,i.y) == 1 and self.barbarians[j].is_attacking!=True:
                                    i.hitpts = i.hitpts - self.barbarians[j].damage
                                    self.barbarians[j].is_attacking = True
                        
                        self.barbarians[j].is_attacking = False  
        
        
        for j in range(len(self.archers)):
            if self.archers[j]!=None and self.archers[j].hitpts > 0:
                if time() - self.archers[j].start_time >= 1*self.ragevalue:
                    if self.archers[j].is_attacking != True:                                        
                        self.archers[j].move_arch(self.Used,self.archers[j].x,self.archers[j].y,Base(self.level).move_archers(self.archers[j],self.TH,self.Cannons,self.huts,self.walls,self.witowers)[0],Base(self.level).move_archers(self.archers[j],self.TH,self.Cannons,self.huts,self.walls,self.witowers)[1])
                
                    self.archers[j].is_attacking = False                                   
                    if  self.archers[j].is_alive == True and self.archers[j]!= None:
                        if self.archers[j]!=None and self.TH.hitpts > 0 and self.archers[j].dist_from_buildings_EU(self.archers[j].x,self.archers[j].y,self.TH.x,self.TH.y) <= 10:                
                            self.TH.hitpts = self.TH.hitpts - self.archers[j].damage
                            self.TH.backg = Base(self.level).reduced_health(self.TH.hitpts,self.TH.orihitpts,self.TH.backg)
                            self.archers[j].is_attacking = True
                       
                       
                        
                        elif self.archers[j].is_attacking!=True:
                            
                            for i in self.Cannons:
                                if i.hitpts>0 and self.archers[j].dist_from_buildings_EU(self.archers[j].x,self.archers[j].y,i.x,i.y) <= 10 and self.archers[j].is_attacking!=True:
                                    i.hitpts = i.hitpts - self.archers[j].damage
                                    self.archers[j].is_attacking = True
                                    i.backg = Base(self.level).reduced_health(i.hitpts,i.orihitpts,i.backg)
                            for i in self.witowers:
                                if i.hitpts>0 and self.archers[j].dist_from_buildings_EU(self.archers[j].x,self.archers[j].y,i.x,i.y) <= 10 and self.archers[j].is_attacking!=True:
                                    i.hitpts = i.hitpts - self.archers[j].damage
                                    self.archers[j].is_attacking = True
                                    i.backg = Base(self.level).reduced_health(i.hitpts,i.orihitpts,i.backg)
                                
                            for i in self.huts:
                                if i.hitpts>0 and self.archers[j].dist_from_buildings_EU(self.archers[j].x,self.archers[j].y,i.x,i.y) <= 10 and self.archers[j].is_attacking!=True:
                                    i.hitpts = i.hitpts - self.archers[j].damage
                                    self.archers[j].is_attacking = True
                                    i.backg = Base(self.level).reduced_health(i.hitpts,i.orihitpts,i.backg)
                            
                            for i in self.walls:
                                if i.hitpts>0 and self.archers[j].dist_from_walls(self.archers[j].x,self.archers[j].y,i.x,i.y) == 1 and self.archers[j].is_attacking!=True:
                                    i.hitpts = i.hitpts - self.archers[j].damage
                                    self.archers[j].is_attacking = True
                        
                         
        
        
        for j in range(len(self.loons)):
            if self.loons[j]!=None and self.loons[j].hitpts > 0:
                if time() - self.loons[j].start_time >= 1*self.ragevalue :                    
                    self.loons[j].move_balloon(self.Used,self.loons[j].x,self.loons[j].y,Base(self.level).move_loons(self.loons[j],self.TH,self.Cannons,self.huts,self.walls,self.witowers)[0],Base(self.level).move_loons(self.loons[j],self.TH,self.Cannons,self.huts,self.walls,self.witowers)[1])
                                                  
                    if  self.loons[j].is_alive == True and self.loons[j]!= None:                       
                        
                        if self.loons[j].is_attacking != True:                            
                            for i in self.witowers:
                                if i.hitpts>0 and self.loons[j].dist_from_witower(self.loons[j].x,self.loons[j].y,i.x,i.y) == 1 and self.loons[j].is_attacking!=True:
                                    self.livedefs = 1
                                    i.hitpts = i.hitpts - self.loons[j].damage
                                    self.loons[j].is_attacking = True
                                    i.backg = Base(self.level).reduced_health(i.hitpts,i.orihitpts,i.backg)
                    
                        if self.loons[j].is_attacking != True:                            
                            for i in self.Cannons:
                                if i.hitpts>0 and self.loons[j].dist_from_cannon(self.loons[j].x,self.loons[j].y,i.x,i.y) == 1 and self.loons[j].is_attacking!=True:
                                    self.livedefs = 1
                                    i.hitpts = i.hitpts - self.loons[j].damage
                                    self.loons[j].is_attacking = True
                                    i.backg = Base(self.level).reduced_health(i.hitpts,i.orihitpts,i.backg)
                                    
                            
                        
                        if self.livedefs == 0:                         
                        
                            if self.loons[j]!=None and self.loons[j].is_attacking != True and self.TH.hitpts > 0 and self.loons[j].dist_from_TH(self.loons[j].x,self.loons[j].y) == 1:                
                                self.TH.hitpts = self.TH.hitpts - self.loons[j].damage
                                self.TH.backg = Base(self.level).reduced_health(self.TH.hitpts,self.TH.orihitpts,self.TH.backg)
                                self.loons[j].is_attacking = True
                            
                            
                            if self.loons[j].is_attacking!=True:
                                for i in self.huts:
                                    if i.hitpts>0 and self.loons[j].dist_from_huts(self.loons[j].x,self.loons[j].y,i.x,i.y) == 1 and self.loons[j].is_attacking!=True:
                                        i.hitpts = i.hitpts - self.loons[j].damage
                                        self.loons[j].is_attacking = True
                                        i.backg = Base(self.level).reduced_health(i.hitpts,i.orihitpts,i.backg)
                                
                            
                        self.livedefs = 0    
                        
                        self.loons[j].is_attacking = False  
                    
        score_board_height = 8
        wall = 1
        border_pixel = Back.LIGHTBLACK_EX+' '+Style.RESET_ALL
        self.output = [[border_pixel for i in range(self.cols+2*wall)] for j in range(score_board_height+self.rows+2*wall)]
        title = "Clash Of Clans"
        title_offset = (self.cols+wall-len(title)) // 2
        for j in range(0, len(title)):
            self.output[1][title_offset+j] = Back.LIGHTYELLOW_EX+Fore.RED+title[j]+Style.RESET_ALL
        
        if self.king!=None:
            health_bar_len = 40
            text = "King: "
            offset = (self.cols+wall-health_bar_len) // 8
            for j in range(0, len(text)):
                self.output[7][offset+j] = Back.WHITE+Fore.RED+text[j]+Style.RESET_ALL
            for j in range(0, health_bar_len):
                self.output[7][len(text)+offset+j] = Back.BLACK+" "+Style.RESET_ALL
            boss_health = int(self.king.hitpts * health_bar_len / self.king.orihitpts)
            for j in range(0, boss_health):
                self.output[7][len(text)+offset+j] = Back.LIGHTYELLOW_EX+" "+Style.RESET_ALL
        
        if self.queen!=None:
            health_bar_len = 40
            text = "Queen: "
            offset = (self.cols+wall-health_bar_len) // 8
            for j in range(0, len(text)):
                self.output[7][offset+j] = Back.WHITE+Fore.RED+text[j]+Style.RESET_ALL
            for j in range(0, health_bar_len):
                self.output[7][len(text)+offset+j] = Back.BLACK+" "+Style.RESET_ALL
            boss_health = int(self.queen.hitpts * health_bar_len / self.queen.orihitpts)
            for j in range(0, boss_health):
                self.output[7][len(text)+offset+j] = Back.LIGHTYELLOW_EX+" "+Style.RESET_ALL
        
        for j in range(0, self.rows):
            for i in range(0, self.cols):
                self.output[j+score_board_height+wall][i+wall] = self.base[j][i]
        
        Base.Game_Over(self)
                
        if self.game_over == 0 or self.game_over == 1:
                
            game_over_screen_height = 7
            game_over_screen_width = self.cols//2
            self.game_over_screen = [[border_pixel for i in range(game_over_screen_width)] for j in range(game_over_screen_height)]
            if self.game_over == 0:                
              game_over = "Defeat!"
            else:
                game_over = "Victory!"
            game_over_offset = (game_over_screen_width-len(game_over)) // 2
            for j in range(0, len(game_over)):
                self.game_over_screen[1][game_over_offset+j] = Back.BLUE+Fore.RED+game_over[j]+Style.RESET_ALL
            
        
            height_offset = score_board_height+((self.rows//2)-(game_over_screen_height//2)+1)
            width_offset = 2*wall+((self.cols//2)-(game_over_screen_width//2)) 
            for row in range(0, game_over_screen_height):
                for col in range(0, game_over_screen_width):
                    self.output[height_offset+row][width_offset+col] = self.game_over_screen[row][col]

        
        
        print("\n".join(["".join(row) for row in self.output])) 
        
        
        
        text_file = open(self.f_path, 'a')
        if os.stat(self.f_path).st_size != 0:
            text_file.write("\n")
        text_file.write("\n".join(["".join(row) for row in self.output]))
        text_file.close()
        
        return self.game_over
        
      
       
    
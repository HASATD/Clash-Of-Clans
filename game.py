from src.base import Base
from src.input import *
from src.king import *

level = 1

base = Base(level)


status = 0

while level == 1:   
    game_end = base.render()
    char = take_input(Get())
    base.get_key(char)
    if(char == 'q' or game_end == 0):              
        break
    
    elif game_end == 1:
        level = 2
        break

print(game_end)
base = Base(level) 
       
while level == 2:
    game_end = base.render()
    char = take_input(Get())
    base.get_key(char)
    if(char == 'q' or game_end == 0):              
        break
    
    elif game_end == 1:
        level = 3
        break

base = Base(level) 
       
while level == 3:
    game_end = base.render()
    char = take_input(Get())
    base.get_key(char)
    if(char == 'q' or game_end == 0 or game_end == 1):              
        break
    
    
    
    
        
    
    
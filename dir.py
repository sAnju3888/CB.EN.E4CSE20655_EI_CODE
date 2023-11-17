
class Dir:
        #class Variables
        dire = ['N','E','S','W']
        movement:list = [[0,1],[1,0],[0,-1],[-1,0]]
        def __init__(self):
            # these variables are protected so that only sub class and package can access        
            self._current_position_x:int 
            self._current_position_y:int
            self._current_Direction:str 
    
    
d = Dir()
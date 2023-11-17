from dir import Dir

class InvalidValueError(Exception):
        pass

class Rover(Dir):
    
    def __init__(self,grid,start_pos,commands,obstacles):
        self.grid = grid
        self.start_pos = start_pos 
        self.__commands = commands 
        self.direction = self.dire.index((self.start_pos[2][0]).upper())
        self.obstacles = obstacles

    def get_commands(self):
        return self.__commands 
    

    def print_input(self):
        print("Terrain: \n")
        for each in self.grid:
            print(f'{each} \n')
        print("Start position:",self.start_pos)
        print("Commands:",self.__commands)
        print("Obstacles:",self.obstacles)
        

    
    def journey_started(self):
        
        self.current_position_x = int(self.start_pos[0])
        self.current_position_y = int(self.start_pos[1])
        self.current_Direction = self.start_pos[2][0].upper()
        
        for dir in self.__commands:
           

            if dir.upper() == 'M' :
                x = self.current_position_x + self.movement[self.direction][0]
                y = self.current_position_y + self.movement[self.direction][1]
                r = len(self.grid) 
                c = len(self.grid[0])

                if 0 <= x < r and 0 <= y <= c and  self.grid[x][y]!=1:
                    # if the  position at obstacles updating the position Before Obstacle
                    self.current_position_x = x 
                    self.current_position_y = y 
                
            elif dir.upper() == 'L':
                
                # changing Direction if L occurs
                self.direction = (self.direction-1)%4
                self.current_Direction = self.dire[self.direction]
    
            else:
                 
                # changing Direction if R occurs
                 self.direction = (self.direction+1)%4
                 self.current_Direction = self.dire[self.direction]
            print(self.direction)
            

        print(f'Final Position:({self.current_position_x},{self.current_position_y},{self.current_Direction[0]})')
        print(f'Status Report: "Rover is at ({self.current_position_x},{self.current_position_y}) facing {self.current_Direction}. No Obstacles detected.')







def check_range(x,y,rows,column):

    if  not( 0<= int(x) < rows) or not(0<= int(y) < column):
        return True 
    else:
        return False



def main():
    IP = True
    
    while(IP):
        try:
            # Dimensions of Grid Based Terrain
            rows,column = map(int,input("Enter Rows and Column: ").split())
            
            # Handling Negative dimensions
            if ((rows < 0 or column < 0)  or (rows == 0 and column == 0)):
                print(f'Error: Invalid Dimensions')
            
            
            else:
                grid =[[0 for _ in range(rows)] for j in range(column)]
                IP = False

        except ValueError as v:
                #handling value error instead of int other type(strings,float) are handled
                print(f"Error: {v}")
                
        except KeyboardInterrupt as ki:
            # to Exit the program pressing control + c
            IP = False 
            print(f'\n Error: Error: KeyboardInterrupt ')
            exit()



            


    
    IP = True 
    while(IP):
        try:
            # Starting Position of Mars Rover
            start_pos = list(input("Enter the Start (x,y,direction) Co-ordinates:").split())
            if len(start_pos) != 3:
                print(f'Error:Only Three Arguements are Allowed')
                

            #checking Direction legid or not
            elif (start_pos[2][0]).upper() not in ['N','E','W','S']:
                raise InvalidValueError(f"Invalid Direction use ['N' ,'E', 'W' ,'S']")
                


            # Check if the input is not an integer
            elif not start_pos[0].isdigit() or not start_pos[1].isdigit():  
                print(f'Co-ordinates must be an integer.')

            #checking start position Falls inside the range 
            elif (start_pos[0].isdigit() or  start_pos[1].isdigit()) and  check_range(start_pos[0],start_pos[1],rows,column):
                print(f'Error: Invalid Dimensions')

            else:
                IP = False
            
        except KeyboardInterrupt as ki:
            # to Exit the program pressing control + c
            IP = False 
            print(f' \n Error: KeyboardInterrupt')
            exit()

        except InvalidValueError as Iv:
            print(f"Caught exception: {Iv}")
            

    IP = True
    # sequence of Commands
    
    while IP:
        flag = 0
        try:
            commands = list(input("Enter the Commands to Move:").split())

            for each_com in commands:
                if each_com.upper() not in ['M','L','R']:
                    flag = 1
                    raise InvalidValueError(f"{each_com}Invalid Command \n use ['M','L','R']")
            if flag != 1:
                IP = False


        except InvalidValueError as Iv:
            print(f"Caught exception: {Iv}")

        except KeyboardInterrupt as ki:
            # to Exit the program pressing control + c
            IP = False 
            print(f' \n Error: KeyboardInterrupt')
            exit()
    
    IP = True 
    while IP:
        try:
            #obstacles in Grid Based Terrain
            num_of_tuples = int(input("Enter No of tuples for Abstacles:"))
            if int(num_of_tuples) >= 0 and int(num_of_tuples) < ((rows)*(column)):
                IP = False
            else:
                print(f"obstacles size should be lesser than grid size")

        except ValueError as v:
            print(f"Only Int should be use")

        except KeyboardInterrupt as ki:
            # to Exit the program pressing control + c
            IP = False 
            print(f' \n Error: KeyboardInterrupt')
            exit()



        obstacles = ["0"]*num_of_tuples
        for i in range(num_of_tuples):
            IP = True 
            while IP:
                try:
                    x,y = map(int,input(f"Enter {i} Obstacles Co-ordinates:").split())

                    if not check_range(x,y,rows,column):
                        obstacles[i] = (x,y)
                        # Converting 0 to 1 [1 are obstacles]
                        grid[x][y] = 1
                        IP = False 
                    else:
                        raise InvalidValueError(f"Obstacle position{i} is not in grid")


                except InvalidValueError as Iv:
                    print(f"Caught exception: {Iv}")
                except ValueError as v:
                        #handling value error instead of int other type(strings,float) are handled
                        obstacle = []
                        print(f"Error: {v}")


                except  KeyboardInterrupt as ki:
                    # to Exit the program pressing control + c
                    IP = False 
                    print(f' \n Error: KeyboardInterrupt')
                    exit()



    c1 = Rover(grid,start_pos,commands,obstacles)
    c1.print_input()
    c1.journey_started()
    # print(c1.get_commands())

if __name__=="__main__":
    main()
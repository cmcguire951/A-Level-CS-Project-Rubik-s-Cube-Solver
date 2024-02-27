from ursina import *
import time
from cube import *
import datetime
from database import *

DesiredState = np.zeros((6,3,3), dtype=str)

for i in range (0,6):
    for f in range (0,3):
        if i==0:
            DesiredState[i,0,f] = "White"
            DesiredState[i,1,f] = "White"
            DesiredState[i,2,f] = "White"                    
        if i==1:
            DesiredState[i,0,f] = "Green"
            DesiredState[i,1,f] = "Green"
            DesiredState[i,2,f] = "Green"                    
        if i==2:
            DesiredState[i,0,f] = "Red"
            DesiredState[i,1,f] = "Red"
            DesiredState[i,2,f] = "Red"                    
        if i==3:
            DesiredState[i,0,f] = "Blue"
            DesiredState[i,1,f] = "Blue"
            DesiredState[i,2,f] = "Blue"                    
        if i==4:
            DesiredState[i,0,f] = "Orange"
            DesiredState[i,1,f] = "Orange"
            DesiredState[i,2,f] = "Orange"                    
        if i==5:
            DesiredState[i,0,f] = "Yellow"
            DesiredState[i,1,f] = "Yellow"
            DesiredState[i,2,f] = "Yellow"

class Cube(Ursina):
    def __init__(self):
        super().__init__()
        #window.fullscreen = True
        EditorCamera()# Creates original scene
        camera.world_position = (0,0,-40)
        self.model, self.texture = 'models/cubelet','textures/cublet texture'  # Defines the model and texture to be used throughout
        self.load()

        self.moverecord = list()

        self.solvetime = 0.0
        self.timer = Text(text=self.solvetime,scale=2,y=0.4,x=-0.2) # Defining the timer

        self.moves = 0
        self.movecounter = Text(text=self.moves,scale=2,y=0.4,x=0.1)

    def move_counter(self):
        self.moves += 1
        self.movecounter.text = self.moves


    def load(self):
        self.cubelet_pos()
        self.parent = Entity(model='cube', texture = 'white_cube')
        self.cubes = [Entity(parent = self.parent, model=self.model, texture=self.texture, position=pos, rotation=(0,-90,0)) for pos in self.sidepos] # Sets the model, texture and position of cubelets to be created
        self.rotation_axes = {'L':'-x', 'R':'x','U':'y','D':'-y','F':'z','B':'-z','Lp':'x', 'Rp':'-x','Up':'-y','Dp':'y','Fp':'-z','Bp':'z'}
        self.cubelet_side_pos = {'L': self.L, 'D': self.D, 'B': self.B, 'F': self.F, 'R': self.R, 'U': self.U, 'Lp': self.L, 'Dp': self.D, 'Bp': self.B, 'Fp': self.F, 'Rp': self.R, 'Up': self.U}
        self.rot = 0

        self.animation_time = 0.5


    def rotate(self, sidename):
        cube_position = self.cubelet_side_pos[sidename]
        rotation_axis = self.rotation_axes[sidename]
        self.parent_to_scene()
        for cube in self.cubes:
            if cube.position in cube_position:
                cube.parent = self.parent
                if rotation_axis == 'x':
                    self.parent.animate_rotation_x(90, duration=self.animation_time)
                if rotation_axis == 'y':
                    self.parent.animate_rotation_y(90, duration=self.animation_time)
                if rotation_axis == 'z':
                    self.parent.animate_rotation_z(90, duration=self.animation_time)        # Checks what axis it wants and the corresponding direction to rotate in
                if rotation_axis == '-x':
                    self.parent.animate_rotation_x(-90, duration=self.animation_time)
                if rotation_axis == '-y':
                    self.parent.animate_rotation_y(-90, duration=self.animation_time)
                if rotation_axis == '-z':
                    self.parent.animate_rotation_z(-90, duration=self.animation_time)
        


    def parent_to_scene(self):
        for cube in self.cubes:
            if cube.parent == self.parent:
                world_pos, world_rot = round(cube.world_position, 1), cube.world_rotation  # Parents individual parts of the cube to the scene instead of the center so that the whole cube doesn't move but individual parts do
                cube.parent = scene
                cube.position, cube.rotation = world_pos, world_rot
        self.parent.rotation = 0
                

    def cubelet_pos(self):
        self.L = {Vec3(-2, y, z) for y in range(-2,4,2) for z in range(-2,4,2)}
        self.D = {Vec3(x, -2, z) for x in range(-2,4,2) for z in range(-2,4,2)}  # Creates the L and B sides
        self.B = {Vec3(x, y, 2) for x in range(-2,4,2) for y in range(-2,4,2)}
        self.F = {Vec3(x, y, -2) for x in range(-2,4,2) for y in range(-2,4,2)}
        self.R = {Vec3(2, y, z) for y in range(-2,4,2) for z in range(-2,4,2)}
        self.U = {Vec3(x, 2, z) for x in range(-2,4,2) for z in range(-2,4,2)}
        self.sidepos = self.L | self.D | self.B | self.F | self.R | self.U   # Stores the positions of the L and D sides

    def left(self):
        self.rotate('L')
        L()
        self.moverecord.append('L')
        print(CubeState)

    def lower(self):
        self.rotate('D')
        D()
        self.moverecord.append('D')
        print(CubeState)

    def back(self):
        self.rotate('B')
        B()
        self.moverecord.append('B')
        print(CubeState)

    def front(self):
        self.rotate('F')
        F()
        self.moverecord.append('F')         # Runs the moves and prints the array and adds the corresponding element to the moverecord list
        print(CubeState)

    def right(self):
        self.rotate('R')
        R()
        self.moverecord.append('R')
        print(CubeState)

    def upper(self):
        self.rotate('U')
        U()
        self.moverecord.append('U')
        print(CubeState)

        
    def left_prime(self):
        self.rotate('Lp')
        Lp()
        print(CubeState)

    def lower_prime(self):
        self.rotate('Dp')
        Dp()
        print(CubeState)

    def back_prime(self):
        self.rotate('Bp')
        Bp()
        print(CubeState)

    def front_prime(self):
        self.rotate('Fp')
        Fp()
        print(CubeState)

    def right_prime(self):
        self.rotate('Rp')
        Rp()
        print(CubeState)

    def upper_prime(self):
        self.rotate('Up')
        Up()
        print(CubeState)
        

    def input(self, key):        
        if key == 'l':
            self.left()
            self.move_counter()
        if key == 'd':
            self.lower()
            self.move_counter()
        if key == 'b':
            self.back()
            self.move_counter()     # Updates the move counter whenever a move is made
        if key == 'f':
            self.front()
            self.move_counter()
        if key == 'r':
            self.right()
            self.move_counter()
        if key == 'u':
            self.upper()
            self.move_counter()
        super().input(key)

        
    def move_display(self):
        print('here')
        print(scramble)
        for i in range(1,26):
            print(scramble[i-16])
            if scramble[i-1] == 'U':
                invoke(self.upper,delay=i)
            if scramble[i-1] == 'D':
                invoke(self.lower,delay=i)
            if scramble[i-1] == 'R':
                invoke(self.right,delay=i)
            if scramble[i-1] == 'L':
                invoke(self.left,delay=i)
            if scramble[i-1] == 'F':
                invoke(self.front,delay=i)      # Performs whatever move the corresponding item in the list is
            if scramble[i-1] == 'B':
                invoke(self.back,delay=i)
            if scramble[i-1] == 'Up':
                invoke(self.upper_prime,delay=i)
            if scramble[i-1] == 'Dp':
                invoke(self.lower_prime,delay=i)
            if scramble[i-1] == 'Rp':
                invoke(self.right_prime,delay=i)
            if scramble[i-1] == 'Lp':
                invoke(self.left_prime,delay=i)
            if scramble[i-1] == 'Fp':
                invoke(self.front_prime,delay=i)
            if scramble[i-1] == 'Bp':
                invoke(self.back_prime,delay=i)


#if __name__ == '__main__':
window = Cube()
window.btn = Button(scale_x=0.15, scale_y=0.1, x=-.5, color=color.gray, text='Scramble', text_size=.5, text_color=color.black, on_click=window.move_display) # Creates a scramble button
solved = False
finished = 0
print(solved)

def update():
    global solved
    global finished
    #print('here')
    if window.moves >= 1:
        solved = np.array_equal(CubeState, DesiredState)
        if solved == False:
            window.solvetime += time.dt
            window.timer.text = round(window.solvetime, 2)      # Displays the time taken
        if solved == True:
            finished += 1
            if finished == 1:
                print(scramble)
                scramble_str = ' '.join(scramble)       # Prints the attributes that will be stored in the db
                print(window.solvetime)
                print(window.moves)
                print(window.moverecord)
                moves_str = ' '.join(window.moverecord)
                date = datetime.date.today()
                print(date)
                currenttime = datetime.datetime.now()
                currenttime = currenttime.strftime("%H:%M:%S")
                print(currenttime)
                database_entry(scramble_str, window.solvetime, window.moves, moves_str, date, currenttime) # Adds these to the db

window.run()






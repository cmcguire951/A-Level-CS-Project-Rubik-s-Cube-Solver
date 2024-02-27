from ursina import *
import time
from cube import *


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
        EditorCamera()                      # Creates original scene
        camera.world_position = (0,0,-40)
        self.model, self.texture = 'models/cubelet','textures/cublet texture'  # Defines the model and texture to be used throughout
        self.load()

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

    def rotate_no_animation(self, sidename):
        cube_position = self.cubelet_side_pos[sidename]
        rotation_axis = self.rotation_axes[sidename]
        self.parent_to_scene()
        for cube in self.cubes:
            if cube.position in cube_position:
                cube.parent = self.parent
                if rotation_axis == 'x':
                    self.parent.rotation_x += 90
                if rotation_axis == 'y':
                    self.parent.rotation_y += 90
                if rotation_axis == 'z':
                    self.parent.rotation_z += 90        # Checks what axis it wants and the corresponding direction to rotate in
                if rotation_axis == '-x':
                    self.parent.rotation_x -= 90
                if rotation_axis == '-y':
                    self.parent.rotation_y -= 90
                if rotation_axis == '-z':
                    self.parent.rotation_z -= 90
        


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
        print(CubeState)
    def lower(self):
        self.rotate('D')
        D()
        print(CubeState)
    def back(self):
        self.rotate('B')
        B()
        print(CubeState)
    def front(self):
        self.rotate('F')
        F()                          # Runs the moves
        print(CubeState)
    def right(self):
        self.rotate('R')
        R()
        print(CubeState)
    def upper(self):
        self.rotate('U')
        U()
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


    def left_no_animation(self):
        self.rotate_no_animation('L')
        L()
        print(CubeState)
    def lower_no_animation(self):
        self.rotate_no_animation('D')
        D()
        print(CubeState)
    def back_no_animation(self):
        self.rotate_no_animation('B')
        B()
        print(CubeState)
    def front_no_animation(self):
        self.rotate_no_animation('F')
        F()                          # Runs the moves
        print(CubeState)
    def right_no_animation(self):
        self.rotate_no_animation('R')
        R()
        print(CubeState)
    def upper_no_animation(self):
        self.rotate_no_animation('U')
        U()
        print(CubeState)
        
    def left_prime_no_animation(self):
        self.rotate_no_animation('Lp')
        Lp()
        print(CubeState)
    def lower_prime_no_animation(self):
        self.rotate_no_animation('Dp')
        Dp()
        print(CubeState)
    def back_prime_no_animation(self):
        self.rotate_no_animation('Bp')
        Bp()
        print(CubeState)
    def front_prime_no_animation(self):
        self.rotate_no_animation('Fp')
        Fp()
        print(CubeState)
    def right_prime_no_animation(self):
        self.rotate_no_animation('Rp')
        Rp()
        print(CubeState)
    def upper_prime_no_animation(self):
        self.rotate_no_animation('Up')
        Up()
        print(CubeState)


    def move_display(self, solution):
        print('here')
        print(solution)
        for i in range(5,len(solution)+5):
            if solution[i-5] == 'U':
                invoke(self.upper,delay=i)
            if solution[i-5] == 'D':
                invoke(self.lower,delay=i)
            if solution[i-5] == 'R':
                invoke(self.right,delay=i)
            if solution[i-5] == 'L':
                invoke(self.left,delay=i)
            if solution[i-5] == 'F':
                invoke(self.front,delay=i)      # Performs whatever move the corresponding item in the list is
            if solution[i-5] == 'B':
                invoke(self.back,delay=i)
                
            if solution[i-5] == 'Up':
                invoke(self.upper_prime,delay=i)
            if solution[i-5] == 'Dp':
                invoke(self.lower_prime,delay=i)
            if solution[i-5] == 'Rp':
                invoke(self.right_prime,delay=i)
            if solution[i-5] == 'Lp':
                invoke(self.left_prime,delay=i)
            if solution[i-5] == 'Fp':
                invoke(self.front_prime,delay=i)
            if solution[i-5] == 'Bp':
                invoke(self.back_prime,delay=i)



    def move_display_no_animation(self, solution):
        print('here')
        print(solution)
        for i in range(1,len(solution)+1):
            if solution[i-1] == 'Up':
                self.upper_no_animation()
            if solution[i-1] == 'Dp':
                self.lower_no_animation()
            if solution[i-1] == 'Rp':
                self.right_no_animation()
            if solution[i-1] == 'Lp':
                self.left_no_animation()
            if solution[i-1] == 'Fp':
                self.front_no_animation()      # Performs the inverse move to whatever is in the list in order to reverse the solution and display the scrambled cube
            if solution[i-1] == 'Bp':
                self.back_no_animation()
                
            if solution[i-1] == 'U':
                self.upper_prime_no_animation()
            if solution[i-1] == 'D':
                self.lower_prime_no_animation()
            if solution[i-1] == 'R':
                self.right_prime_no_animation()
            if solution[i-1] == 'L':
                self.left_prime_no_animation()
            if solution[i-1] == 'F':
                self.front_prime_no_animation()
            if solution[i-1] == 'B':
                self.back_prime_no_animation()
                
            if solution[i-1] == 'U2':
                self.upper_prime_no_animation()
                self.upper_prime_no_animation()
            if solution[i-1] == 'D2':
                self.lower_prime_no_animation()
                self.lower_prime_no_animation()
            if solution[i-1] == 'R2':
                self.right_prime_no_animation()
                self.right_prime_no_animation()
            if solution[i-1] == 'L2':
                self.left_prime_no_animation()
                self.left_prime_no_animation()
            if solution[i-1] == 'F2':
                self.front_prime_no_animation()
                self.front_prime_no_animation()
            if solution[i-1] == 'B2':
                self.back_prime_no_animation()
                self.back_prime_no_animation()

        

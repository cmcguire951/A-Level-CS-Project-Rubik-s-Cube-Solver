import numpy as np
import random
CubeState = np.zeros((6,3,3), dtype=str)
moves = 0


def InitArray():
    for i in range (0,6):
        for f in range (0,3):
            if i==0:
                CubeState[i,0,f] = "White"
                CubeState[i,1,f] = "White"
                CubeState[i,2,f] = "White"                    
            if i==1:
                CubeState[i,0,f] = "Green"
                CubeState[i,1,f] = "Green"
                CubeState[i,2,f] = "Green"                    
            if i==2:
                CubeState[i,0,f] = "Red"
                CubeState[i,1,f] = "Red"
                CubeState[i,2,f] = "Red"                    
            if i==3:
                CubeState[i,0,f] = "Blue"
                CubeState[i,1,f] = "Blue"
                CubeState[i,2,f] = "Blue"                    
            if i==4:
                CubeState[i,0,f] = "Orange"
                CubeState[i,1,f] = "Orange"
                CubeState[i,2,f] = "Orange"                    
            if i==5:
                CubeState[i,0,f] = "Yellow"
                CubeState[i,1,f] = "Yellow"
                CubeState[i,2,f] = "Yellow"
                

InitArray()

#print(CubeState)

#print(CubeState[0])

def U():
    #print('u')
    C = 0
    UM = 0
    UL = 0
    UR = 0
    LM = 0     #Creates temp variables
    RM = 0
    BL = 0
    BM = 0
    BR = 0
    
    C = CubeState[0,1,1]
    UM = CubeState[0,0,1] 
    UL = CubeState[0,0,0] 
    UR = CubeState[0,0,2] 
    LM = CubeState[0,1,0]  #Sets the state of the face to temp variables
    RM = CubeState[0,1,2] 
    BL = CubeState[0,2,0] 
    BM = CubeState[0,2,1] 
    BR = CubeState[0,2,2]

    CubeState[0,1,1] = C
    CubeState[0,0,1] = LM
    CubeState[0,0,0] = BL
    CubeState[0,0,2] = UL
    CubeState[0,1,0] = BM         #Transposes the face
    CubeState[0,1,2] = UM
    CubeState[0,2,0] = BR
    CubeState[0,2,1] = RM
    CubeState[0,2,2] = UR

    GUL = CubeState[1,0,0]
    GUM = CubeState[1,0,1]  #sets 3 temp variables to the top 3 of the green side
    GUR = CubeState[1,0,2]

    RUL = CubeState[2,0,0]
    RUM = CubeState[2,0,1]  #sets 3 temp variables to the top 3 of the red side
    RUR = CubeState[2,0,2]

    BUL = CubeState[3,0,0]
    BUM = CubeState[3,0,1]  #sets 3 temp variables to the top 3 of the blue side
    BUR = CubeState[3,0,2]

    OUL = CubeState[4,0,0]
    OUM = CubeState[4,0,1]  #sets 3 temp variables to the top 3 of the orange side
    OUR = CubeState[4,0,2]

    CubeState[1,0,0] = RUL
    CubeState[1,0,1] = RUM  #sets the top row of the green side to the top 3 of the red side
    CubeState[1,0,2] = RUR

    CubeState[2,0,0] = BUL
    CubeState[2,0,1] = BUM  #sets the top row of the red side to the top 3 of the blue side
    CubeState[2,0,2] = BUR

    CubeState[3,0,0] = OUL
    CubeState[3,0,1] = OUM  #sets the top row of the blue side to the top 3 of the orange side
    CubeState[3,0,2] = OUR

    CubeState[4,0,0] = GUL
    CubeState[4,0,1] = GUM  #sets the top row of the orange side to the top 3 of the green side
    CubeState[4,0,2] = GUR

def D():
    #print('d')
    C = 0
    UM = 0
    UL = 0
    UR = 0
    LM = 0     #Creates temp variables
    RM = 0
    BL = 0
    BM = 0
    BR = 0
    
    C = CubeState[5,1,1]
    UM = CubeState[5,0,1] 
    UL = CubeState[5,0,0] 
    UR = CubeState[5,0,2] 
    LM = CubeState[5,1,0]  #Sets the state of the yellow face to temp variables
    RM = CubeState[5,1,2] 
    BL = CubeState[5,2,0] 
    BM = CubeState[5,2,1] 
    BR = CubeState[5,2,2]

    CubeState[5,1,1] = C
    CubeState[5,0,1] = LM
    CubeState[5,0,0] = BL
    CubeState[5,0,2] = UL
    CubeState[5,1,0] = BM         #Transposes the face
    CubeState[5,1,2] = UM
    CubeState[5,2,0] = BR
    CubeState[5,2,1] = RM
    CubeState[5,2,2] = UR

    GLL = CubeState[1,2,0]
    GLM = CubeState[1,2,1]  #sets 3 temp variables to the lower 3 of the green side
    GLR = CubeState[1,2,2]

    RLL = CubeState[2,2,0]
    RLM = CubeState[2,2,1]  #sets 3 temp variables to the lower 3 of the red side
    RLR = CubeState[2,2,2]

    BLL = CubeState[3,2,0]
    BLM = CubeState[3,2,1]  #sets 3 temp variables to the lower 3 of the blue side
    BLR = CubeState[3,2,2]

    OLL = CubeState[4,2,0]
    OLM = CubeState[4,2,1]  #sets 3 temp variables to the lower 3 of the orange side
    OLR = CubeState[4,2,2]

    CubeState[1,2,0] = OLL
    CubeState[1,2,1] = OLM  #sets the bottom row of the green side to the bottom 3 of the orange side
    CubeState[1,2,2] = OLR

    CubeState[2,2,0] = GLL
    CubeState[2,2,1] = GLM  #sets the bottom row of the red side to the bottom 3 of the green side
    CubeState[2,2,2] = GLR

    CubeState[3,2,0] = RLL
    CubeState[3,2,1] = RLM  #sets the bottom row of the blue side to the bottom 3 of the red side
    CubeState[3,2,2] = RLR

    CubeState[4,2,0] = BLL
    CubeState[4,2,1] = BLM  #sets the bottom row of the orange side to the bottom 3 of the green side
    CubeState[4,2,2] = BLR

def F():
    #print('f')
    C = 0
    UM = 0
    UL = 0
    UR = 0
    LM = 0     #Creates temp variables
    RM = 0
    BL = 0
    BM = 0
    BR = 0
    
    C = CubeState[2,1,1]
    UM = CubeState[2,0,1] 
    UL = CubeState[2,0,0] 
    UR = CubeState[2,0,2] 
    LM = CubeState[2,1,0]  #Sets the state of the red face to temp variables
    RM = CubeState[2,1,2] 
    BL = CubeState[2,2,0] 
    BM = CubeState[2,2,1] 
    BR = CubeState[2,2,2]

    CubeState[2,1,1] = C
    CubeState[2,0,1] = LM
    CubeState[2,0,0] = BL
    CubeState[2,0,2] = UL
    CubeState[2,1,0] = BM         #Transposes the face
    CubeState[2,1,2] = UM
    CubeState[2,2,0] = BR
    CubeState[2,2,1] = RM
    CubeState[2,2,2] = UR

    GUR = CubeState[1,0,2]
    GMR = CubeState[1,1,2]  #sets 3 temp variables to the right 3 of the green side
    GLR = CubeState[1,2,2]

    YUL = CubeState[5,0,0]
    YUM = CubeState[5,0,1]  #sets 3 temp variables to the upper 3 of the yellow side
    YUR = CubeState[5,0,2]

    BUL = CubeState[3,0,0]
    BML = CubeState[3,1,0]  #sets 3 temp variables to the left 3 of the blue side
    BLL = CubeState[3,2,0]

    WLL = CubeState[0,2,0]
    WLM = CubeState[0,2,1]  #sets 3 temp variables to the lower 3 of the white side
    WLR = CubeState[0,2,2]

    CubeState[1,0,2] = YUL
    CubeState[1,1,2] = YUM  #sets the right column of the green side to the top 3 of the yellow side
    CubeState[1,2,2] = YUR

    CubeState[0,2,0] = GLR
    CubeState[0,2,1] = GMR  #sets the bottom row of the white side to the right 3 of the green side
    CubeState[0,2,2] = GUR

    CubeState[3,0,0] = WLL
    CubeState[3,1,0] = WLM  #sets the left column of the blue side to the bottom 3 of the white side
    CubeState[3,2,0] = WLR

    CubeState[5,0,0] = BLL
    CubeState[5,0,1] = BML  #sets the top row of the yellow side to the left 3 of the blue side
    CubeState[5,0,2] = BUL

def B():
    #print('b')
    C = 0
    UM = 0
    UL = 0
    UR = 0
    LM = 0     #Creates temp variables
    RM = 0
    BL = 0
    BM = 0
    BR = 0
    
    C = CubeState[4,1,1]
    UM = CubeState[4,0,1] 
    UL = CubeState[4,0,0] 
    UR = CubeState[4,0,2] 
    LM = CubeState[4,1,0]  #Sets the state of the orange face to temp variables
    RM = CubeState[4,1,2] 
    BL = CubeState[4,2,0] 
    BM = CubeState[4,2,1] 
    BR = CubeState[4,2,2]

    CubeState[4,1,1] = C
    CubeState[4,0,1] = LM
    CubeState[4,0,0] = BL
    CubeState[4,0,2] = UL
    CubeState[4,1,0] = BM         #Transposes the face
    CubeState[4,1,2] = UM
    CubeState[4,2,0] = BR
    CubeState[4,2,1] = RM
    CubeState[4,2,2] = UR

    BUR = CubeState[3,0,2]
    BMR = CubeState[3,1,2]  #sets 3 temp variables to the right 3 of the blue side
    BLR = CubeState[3,2,2]

    YLL = CubeState[5,2,0]
    YLM = CubeState[5,2,1]  #sets 3 temp variables to the upper 3 of the yellow side
    YLR = CubeState[5,2,2]

    GUL = CubeState[1,0,0]
    GML = CubeState[1,1,0]  #sets 3 temp variables to the left 3 of the green side
    GLL = CubeState[1,2,0]

    WUL = CubeState[0,0,0]
    WUM = CubeState[0,0,1]  #sets 3 temp variables to the upper 3 of the white side
    WUR = CubeState[0,0,2]

    CubeState[0,0,0] = BUR
    CubeState[0,0,1] = BMR  #sets the top 3 of the white side to the left 3 of the green side
    CubeState[0,0,2] = BLR

    CubeState[1,0,0] = WUR
    CubeState[1,1,0] = WUM  #sets the left column of the green side to the top 3 of the white side
    CubeState[1,2,0] = WUL

    CubeState[5,2,0] = GUL
    CubeState[5,2,1] = GML  #sets the bottom row of the yellow side to the left 3 of the green side
    CubeState[5,2,2] = GLL

    CubeState[3,0,2] = YLR
    CubeState[3,1,2] = YLM  #sets the right column of the blue side to the bottom 3 of the yellow side
    CubeState[3,2,2] = YLL

def R():
    #print('r')
    C = 0
    UM = 0
    UL = 0
    UR = 0
    LM = 0     #Creates temp variables
    RM = 0
    BL = 0
    BM = 0
    BR = 0
    
    C = CubeState[3,1,1]
    UM = CubeState[3,0,1] 
    UL = CubeState[3,0,0] 
    UR = CubeState[3,0,2] 
    LM = CubeState[3,1,0]  #Sets the state of the orange face to temp variables
    RM = CubeState[3,1,2] 
    BL = CubeState[3,2,0] 
    BM = CubeState[3,2,1] 
    BR = CubeState[3,2,2]

    CubeState[3,1,1] = C
    CubeState[3,0,1] = LM
    CubeState[3,0,0] = BL
    CubeState[3,0,2] = UL
    CubeState[3,1,0] = BM         #Transposes the face
    CubeState[3,1,2] = UM
    CubeState[3,2,0] = BR
    CubeState[3,2,1] = RM
    CubeState[3,2,2] = UR

    YUR = CubeState[5,0,2]
    YMR = CubeState[5,1,2]  #sets 3 temp variables to the right 3 of the yellow side
    YLR = CubeState[5,2,2]

    OUL = CubeState[4,0,0]
    OML = CubeState[4,1,0]  #sets 3 temp variables to the left 3 of the orange side
    OLL = CubeState[4,2,0]

    WUR = CubeState[0,0,2]
    WMR = CubeState[0,1,2]  #sets 3 temp variables to the right 3 of the white side
    WLR = CubeState[0,2,2]

    RUR = CubeState[2,0,2]
    RMR = CubeState[2,1,2]  #sets 3 temp variables to the right 3 of the white side
    RLR = CubeState[2,2,2]

    CubeState[4,0,0] = WLR
    CubeState[4,1,0] = WMR  #sets the right 3 of the white side to the left 3 of the orange side
    CubeState[4,2,0] = WUR

    CubeState[0,0,2] = RUR
    CubeState[0,1,2] = RMR  #sets the right column of the white side to the right 3 of the red side
    CubeState[0,2,2] = RLR

    CubeState[2,0,2] = YUR
    CubeState[2,1,2] = YMR  #sets the right column of the red side to the right 3 of the yellow side
    CubeState[2,2,2] = YLR

    CubeState[5,0,2] = OLL
    CubeState[5,1,2] = OML  #sets the right column of the blue side to the bottom 3 of the yellow side
    CubeState[5,2,2] = OUL

def L():
    #print('L')
    C = 0
    UM = 0
    UL = 0
    UR = 0
    LM = 0     #Creates temp variables
    RM = 0
    BL = 0
    BM = 0
    BR = 0
    
    C = CubeState[1,1,1]
    UM = CubeState[1,0,1] 
    UL = CubeState[1,0,0] 
    UR = CubeState[1,0,2] 
    LM = CubeState[1,1,0]  #Sets the state of the orange face to temp variables
    RM = CubeState[1,1,2] 
    BL = CubeState[1,2,0] 
    BM = CubeState[1,2,1] 
    BR = CubeState[1,2,2]

    CubeState[1,1,1] = C
    CubeState[1,0,1] = LM
    CubeState[1,0,0] = BL
    CubeState[1,0,2] = UL
    CubeState[1,1,0] = BM         #Transposes the face
    CubeState[1,1,2] = UM
    CubeState[1,2,0] = BR
    CubeState[1,2,1] = RM
    CubeState[1,2,2] = UR

    WUL = CubeState[0,0,0]
    WML = CubeState[0,1,0]  #sets 3 temp variables to the left 3 of the yellow side
    WLL = CubeState[0,2,0]

    RUL = CubeState[2,0,0]
    RML = CubeState[2,1,0]  #sets 3 temp variables to the left 3 of the red side
    RLL = CubeState[2,2,0]

    YUL = CubeState[5,0,0]
    YML = CubeState[5,1,0]  #sets 3 temp variables to the left 3 of the yellow side
    YLL = CubeState[5,2,0]

    OUR = CubeState[4,0,2]
    OMR = CubeState[4,1,2]  #sets 3 temp variables to the right 3 of the orange side
    OLR = CubeState[4,2,2]

    CubeState[2,0,0] = WUL
    CubeState[2,1,0] = WML  #sets the left 3 of the red side to the left 3 of the white side
    CubeState[2,2,0] = WLL

    CubeState[5,0,0] = RUL
    CubeState[5,1,0] = RML  #sets the left column of the yellow side to the left 3 of the red side
    CubeState[5,2,0] = RLL

    CubeState[4,0,2] = YLL
    CubeState[4,1,2] = YML  #sets the left column of the orange side to the left 3 of the yellow side
    CubeState[4,2,2] = YUL

    CubeState[0,0,0] = OLR
    CubeState[0,1,0] = OMR  #sets the right column of the blue side to the bottom 3 of the yellow side
    CubeState[0,2,0] = OUR

def Up():
    U()
    U()
    U()

def Dp():
    D()
    D()
    D()

def Rp():
    R()
    R()
    R()

def Lp():
    L()
    L()
    L()

def Fp():
    F()
    F()
    F()

def Bp():
    B()
    B()
    B()

def scrambler():
    #global move
    global scramble
    scramble = [None]*25
    for i in range(0,25):
        move = random.randint(1,12)
        if move == 1:
            scramble[i] = 'U'
        if move == 2:
            scramble[i] = 'D'
        if move == 3:
            scramble[i] = 'R'
        if move == 4:
            scramble[i] = 'L'
        if move == 5:
            scramble[i] = 'F'
        if move == 6:
            scramble[i] = 'B'
        if move == 7:
            scramble[i] = 'Up'
        if move == 8:
            scramble[i] = 'Dp'
        if move == 9:
            scramble[i] = 'Rp'
        if move == 10:
            scramble[i] = 'Lp'
        if move == 11:
            scramble[i] = 'Fp'
        if move == 12:
            scramble[i] = 'Bp'

scrambler()
#print(scramble)

    #print(scramble)

##print(scramble)
	
#print("")
#print("")

#R()
#print(CubeState)

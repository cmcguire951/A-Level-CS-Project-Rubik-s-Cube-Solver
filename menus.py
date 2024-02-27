from tkinter import *
from tkinter import ttk
import tkinter as tk
from cube import *
import ctypes
from database import *
import time
import os
from Cube_Display_Model import *
from twophase import solve



ctypes.windll.shcore.SetProcessDpiAwareness(1)


def main():
    global MainMenu
    global style
    MainMenu = Tk()
    MainMenu.title('Rubiks Cube Sim')  # Creates a window with the title 'Rubiks Cube Solver' that is 1280x960 and with a gray background
    MainMenu.geometry('1280x960')
    MainMenu.config(bg='gray')

    #MainMenu.tk.call('tk','scaling',2.0)

    style = ttk.Style()
    style.configure('W.TButton', font=('Verdana', 25), foreground = 'black')  # Style for the buttons
    
    Label(MainMenu, text='Rubiks Cube Sim', font=('Verdana', 40, 'bold'), bg='gray').pack()  # Shows a title 'Rubiks Cube Solver'
    
    timerbtn = ttk.Button(MainMenu, text='Timer/Interactive', style='W.TButton', command=timer_window)
    timerbtn.place(relx=0.5, rely=0.7, anchor=CENTER)   # Creates a button and anchors it to the center
    
    solverbtn = ttk.Button(MainMenu, text='Solver', style='W.TButton', command=solverinput)
    solverbtn.place(relx=0.5, rely=0.5, anchor=CENTER)  
    
    databasebtn = ttk.Button(MainMenu, text='Database', style='W.TButton', command=maindatabase)
    databasebtn.place(relx=0.5, rely=0.3, anchor=CENTER)

    style = ttk.Style()
    style.configure('W.TLabel', font=('Verdana', 15), foreground = 'black', background = 'gray')

def timer_window():
    os.system('Cube_Timer_Model.py')

def maindatabase():
    global DataMenu
    MainMenu.withdraw()
    DataMenu = Toplevel(MainMenu)
    DataMenu.title('Database Viewer')  # Creates a window with the title 'Database Viewer' that is 1280x960 and with a gray background
    DataMenu.geometry('1280x960')
    DataMenu.config(bg='gray')

    Label(DataMenu, text='Database Viewer', font=('Verdana', 40, 'bold'), bg='gray').pack()  # Shows a title 'Database Viewer'
    
    searchbtn = ttk.Button(DataMenu, text='Search', style='W.TButton', command=databasesearch)
    searchbtn.place(relx=0.5, rely=0.3, anchor=CENTER)   # Creates a button and anchors it to the center
    
    fullbtn = ttk.Button(DataMenu, text='Full View', style='W.TButton', command=database_full_display)
    fullbtn.place(relx=0.5, rely=0.5, anchor=CENTER)  
    
    backbtn = ttk.Button(DataMenu, text='Back', command=lambda:[DataMenu.destroy(), MainMenu.deiconify()])
    backbtn.place(relx=0.1, rely=0.9, anchor=CENTER)

def databasesearch():
    global DataSearch
    global day
    global month
    global year
    DataMenu.withdraw()
    DataSearch = Toplevel(DataMenu)
    DataSearch.title('Database Search')  # Creates a window with the title 'Database Search' that is 1280x960 and with a gray background
    DataSearch.geometry('1280x960')
    DataSearch.config(bg='gray')
    
    Label(DataSearch, text='Database Search', font=('Verdana', 40, 'bold'), bg='gray').pack()  # Shows a title 'Database Search'

    day = ttk.Label(DataSearch, text='Enter Day as any 2 digit number between 01-31', style='W.TLabel') # Creates a label explaining how to enter the day
    day.place(relx=0.5, rely=0.17, anchor=CENTER)
    month = ttk.Label(DataSearch, text='Enter Month as 2 digit number between 01-12', style='W.TLabel') # Creates a label explaining how to enter the month
    month.place(relx=0.5, rely=0.22, anchor=CENTER)
    year = ttk.Label(DataSearch, text='Enter Year as any 4-digit integer', style='W.TLabel') # Creates a label explaining how to enter the year
    year.place(relx=0.5, rely=0.27, anchor=CENTER)
    
    backbtn = ttk.Button(DataSearch, text='Back', command=lambda:[DataSearch.destroy(), DataMenu.deiconify()])
    backbtn.place(relx=0.1, rely=0.9, anchor=CENTER)

    style = ttk.Style()
    style.configure('W.TLabel', font=('Verdana', 15), foreground = 'black', background = 'gray')    # Style for the labels
    style.configure('Custom.TButton', font=('Verdana', 15), foreground = 'green') # style for the search button

    day = ttk.Label(DataSearch, text='Day', style='W.TLabel') # Creates a label next to the day entry saying 'day'
    day.place(relx=0.4, rely=0.4, anchor=CENTER)
    day = ttk.Entry(DataSearch, width = 12)             # creates the day text entry
    day.place(relx=0.5, rely=0.4, anchor=CENTER)

    month = ttk.Label(DataSearch, text='Month', style='W.TLabel') # Creates a label next to the month entry saying 'month'
    month.place(relx=0.38, rely=0.5, anchor=CENTER)
    month = ttk.Entry(DataSearch, width = 12)             # creates the month text entry
    month.place(relx=0.5, rely=0.5, anchor=CENTER)

    year = ttk.Label(DataSearch, text='Year', style='W.TLabel') # Creates a label next to the year entry saying 'year'
    year.place(relx=0.39, rely=0.6, anchor=CENTER)
    year = ttk.Entry(DataSearch, width = 12)             # creates the year text entry
    year.place(relx=0.5, rely=0.6, anchor=CENTER)

    search = ttk.Button(DataSearch, text='Go', style='Custom.TButton', command=database_search_results)  # creates a search button
    search.place(relx=0.8, rely=0.5, anchor=CENTER)

def database_search_results():
    day_val = str(day.get())
    month_val = str(month.get())        # Stores the inputs from the previous window
    year_val = str(year.get())
    print(day_val)
    print(month_val)
    print(year_val)

    output_from_db(day_val,month_val,year_val)
     # Calls the function from database.py
    
    global DataSearchResults
    DataSearch.withdraw()
    DataSearchResults = Toplevel(DataSearch)
    DataSearchResults.title('Database Search Results')  # Creates a window with the title 'Database Search Results' that is 1280x960 and with a gray background
    DataSearchResults.geometry('1280x960')
    DataSearchResults.config(bg='gray')

    backbtn = ttk.Button(DataSearchResults, text='Back', command=lambda:[DataSearchResults.destroy(), DataSearch.deiconify()])
    backbtn.place(relx=0.1, rely=0.9, anchor=CENTER)

    Label(DataSearchResults, text='Database Search Results', font=('Verdana', 40, 'bold'), bg='gray').pack()

    now_showing = ttk.Label(DataSearchResults, text='Now Showing Results From: ' + output_from_db.date_input, style='W.TLabel') # Creates a label next to the day entry saying 'Now showing: date'
    now_showing.place(relx=0.5, rely=0.1, anchor=CENTER)

    body = tk.Text(DataSearchResults, width = 120, height = 35)
    body.place(relx=0.5,rely=0.5,anchor=CENTER)
    body.insert(tk.END, '\n' + 'SolveID, Scramble, Solve Time, Number of Moves Taken, Moves Taken' + '\n')# Displays the contents of the DB on a text widget
    for i in range(1,output_from_db.number_of_results+1): 
        body.insert(tk.END, '\n' + str(output_from_db.Results[i-1]) + '\n')

    y_scroll = Scrollbar(DataSearchResults, command=body.yview)
    y_scroll.pack(side=RIGHT, fill=Y)       # Creates a scroll bar that can be used if there is too much data
    body['yscrollcommand'] = y_scroll.set

def database_full_display():
    output_all()

    global DataFullView
    DataMenu.withdraw()
    DataFullView = Toplevel(DataMenu)
    DataFullView.title('Database Search Results')  # Creates a window with the title 'Database Full View' that is 1280x960 and with a gray background
    DataFullView.geometry('1280x960')
    DataFullView.config(bg='gray')

    backbtn = ttk.Button(DataFullView, text='Back', command=lambda:[DataFullView.destroy(), DataMenu.deiconify()])
    backbtn.place(relx=0.1, rely=0.9, anchor=CENTER)

    Label(DataFullView, text='Database Full View', font=('Verdana', 40, 'bold'), bg='gray').pack()

    now_showing = ttk.Label(DataFullView, text='Now Showing All Results', style='W.TLabel') # Creates a label next to the entry saying 'Now showing all results'
    now_showing.place(relx=0.5, rely=0.1, anchor=CENTER)

    body = tk.Text(DataFullView, width = 120, height = 35)
    body.place(relx=0.5,rely=0.5,anchor=CENTER)
    body.insert(tk.END, '\n' + 'SolveID, Scramble, Solve Time, Number of Moves Taken, Moves Taken, Date of Solve, Time of Solve' + '\n')# Displays the contents of the DB on a text widget
    for i in range(1,output_all.number_of_results+1): 
        body.insert(tk.END, '\n' + str(output_all.outputs[i-1]) + '\n')

    y_scroll = Scrollbar(DataFullView, command=body.yview)
    y_scroll.pack(side=RIGHT, fill=Y)       # Creates a scroll bar that can be used if there is too much data
    body['yscrollcommand'] = y_scroll.set

def solverinput():
    global InputMenu
    MainMenu.withdraw()
    InputMenu = Toplevel(MainMenu)
    InputMenu.title('Cube Input')  # Creates a window with the title 'Cube Input' that is 1280x960 and with a gray background
    InputMenu.geometry('1280x960')
    InputMenu.config(bg='gray')

    Label(InputMenu, text='Cube Input', font=('Verdana', 40, 'bold'), bg='gray').pack()  # Shows a title 'Cube Input'

    backbtn = ttk.Button(InputMenu, text='Back', command=lambda:[InputMenu.destroy(), MainMenu.deiconify()]) 
    backbtn.place(relx=0.1, rely=0.9, anchor=CENTER)

    global ColourNum     # creates lists for the Colour and ColourNumber
    global Colour

    style.configure('Custom.TButton', font=('Verdana', 15), foreground = 'green') # style for the solve button
    solve = ttk.Button(InputMenu, text='Solve', style='Custom.TButton', command=lambda:[ArrayInput(), display_solution()]) # creates a solve button
    solve.place(relx=0.8, rely=0.7, anchor=CENTER)

    RedCenter = tk.Button(InputMenu, width=4, height=1, bg='Red')
    RedCenter.place(relx=0.4 ,rely=0.5, anchor=CENTER)
    WhiteCenter = tk.Button(InputMenu, width=4, height=1, bg='White')
    WhiteCenter.place(relx=0.4 ,rely=0.3, anchor=CENTER)
    YellowCenter = tk.Button(InputMenu, width=4, height=1, bg='Yellow')    # creates 6 actionless buttons to act as the face centers
    YellowCenter.place(relx=0.4 ,rely=0.7, anchor=CENTER)
    GreenCenter = tk.Button(InputMenu, width=4, height=1, bg='Green')
    GreenCenter.place(relx=0.2 ,rely=0.5, anchor=CENTER)
    BlueCenter = tk.Button(InputMenu, width=4, height=1, bg='Blue')
    BlueCenter.place(relx=0.6 ,rely=0.5, anchor=CENTER)
    OrangeCenter = tk.Button(InputMenu, width=4, height=1, bg='Orange')
    OrangeCenter.place(relx=0.8 ,rely=0.5, anchor=CENTER)

    Colour = []
    ColourNum = []

    global z
    z=0

    for i in range(0,48):
        Colour.append('white')  # adds 48 elements to each list
        ColourNum.append(0)   

    def ColourChange(x,y,z):
        global ColourNum
        if ColourNum[z] == 0:
            Colour[z] = 'Lightgray'
        if ColourNum[z] == 7:
            ColourNum[z] = 1
        if ColourNum[z] == 1:
            Colour[z] = 'Red'
        if ColourNum[z] == 2:
            Colour[z] = 'White'      # cycles through each colour + colour number each time a button is pressed
        if ColourNum[z] == 3:
            Colour[z] = 'Blue'
        if ColourNum[z] == 4:
            Colour[z] = 'Yellow'
        if ColourNum[z] == 5:
            Colour[z] = 'Orange'
        if ColourNum[z] == 6:
            Colour[z] = 'Green'
        tk.Button(InputMenu, width=4, height=1, bg=Colour[z], command=lambda:[ColourChange(x,y,z)], activebackground=Colour[z]).place(relx=x ,rely=y, anchor=CENTER)
        ColourNum[z] = ColourNum[z] + 1
        
    def InputButtons(center_x,center_y, number):
        ColourChange(center_x-0.06,center_y-0.06,number)
        ColourChange(center_x,center_y-0.06,number+1)
        ColourChange(center_x+0.06,center_y-0.06,number+2)
        ColourChange(center_x-0.06,center_y,number+3)     # Creates a function that creates 8 buttons relative to the center button
        ColourChange(center_x+0.06,center_y,number+4)
        ColourChange(center_x-0.06,center_y+0.06,number+5)
        ColourChange(center_x,center_y+0.06,number+6)
        ColourChange(center_x+0.06,center_y+0.06,number+7)

    InputButtons(0.4,0.3,0) # Creates buttons for white side
    InputButtons(0.2,0.5,8) # Creates buttons for green side
    InputButtons(0.4,0.5,16) # Creates buttons for red side
    InputButtons(0.4,0.7,24) # Creates buttons for yellow side
    InputButtons(0.6,0.5,32) # Creates buttons for blue side
    InputButtons(0.8,0.5,40) # Creates buttons for orange side

    def ArrayInput():
        def ArrayState(piece):
            CubeState[face,0,0] = Colour[piece]    
            CubeState[face,0,1] = Colour[piece+1]
            CubeState[face,0,2] = Colour[piece+2]
            CubeState[face,1,0] = Colour[piece+3]
            CubeState[face,1,2] = Colour[piece+4]   # Defines a function that takes the starting piece as a
            CubeState[face,2,0] = Colour[piece+5]   # prameter and sets the value of those from the list to
            CubeState[face,2,1] = Colour[piece+6]   # corresponding values in  the array
            CubeState[face,2,2] = Colour[piece+7]
        for face in range(0,6):
            if face == 0:
                ArrayState(0)  # Cycles through the 6 faces, each with the corresponding starting piece.
            if face == 1:
                ArrayState(8)
            if face == 2:
                ArrayState(16)
            if face == 3:
                ArrayState(32)
            if face == 4:
                ArrayState(40)
            if face == 5:
                ArrayState(24)
        #print(CubeState)

def display_solution():
    game = Cube() # Creates an instance of the class
    
    CubeStateStr = list()   
    temp = CubeState[0].tolist()
    CubeStateStr.append(''.join(temp[0]) + ''.join(temp[1]) + ''.join(temp[2]))
    temp = CubeState[3].tolist()
    CubeStateStr.append(''.join(temp[0]) + ''.join(temp[1]) + ''.join(temp[2]))
    temp = CubeState[2].tolist()
    CubeStateStr.append(''.join(temp[0]) + ''.join(temp[1]) + ''.join(temp[2]))     # Converts the CubeState array into a list
    temp = CubeState[5].tolist()
    CubeStateStr.append(''.join(temp[0]) + ''.join(temp[1]) + ''.join(temp[2]))
    temp = CubeState[1].tolist()
    CubeStateStr.append(''.join(temp[0]) + ''.join(temp[1]) + ''.join(temp[2]))
    temp = CubeState[4].tolist()
    CubeStateStr.append(''.join(temp[0]) + ''.join(temp[1]) + ''.join(temp[2]))

    CubeStateStr = ''.join(CubeStateStr)    #Changes the list into a long string

    #CubeStateStr = 'BWYGWYWYRWGGGBROOORRBRRWGYGROWRYWBBBYOGOGBOWYOBRGOBYYW' #<---- Example solve

    CubeStateStr = CubeStateStr.replace('W','U')
    CubeStateStr = CubeStateStr.replace('R','F')
    CubeStateStr = CubeStateStr.replace('B','R')        # Puts the string in a form that can be solved by the module
    CubeStateStr = CubeStateStr.replace('Y','D')
    CubeStateStr = CubeStateStr.replace('G','L')
    CubeStateStr = CubeStateStr.replace('O','B')
    
    #print(CubeStateStr)

    solution = solve(CubeStateStr)      # Solves the cube
    solution = solution.replace("'",'p')
    solution_list = solution.split()
    solution_list_full = list()

    for i in range(0,len(solution_list)):
        if solution_list[i] == 'U2':
            solution_list_full.append('U')
            solution_list_full.append('U')
        if solution_list[i] == 'D2':
            solution_list_full.append('D')
            solution_list_full.append('D')
        if solution_list[i] == 'F2':
            solution_list_full.append('F')
            solution_list_full.append('F')      # Changes all the double moves separate so they can be displayed properly
        if solution_list[i] == 'B2':
            solution_list_full.append('B')
            solution_list_full.append('B')
        if solution_list[i] == 'R2':
            solution_list_full.append('R')
            solution_list_full.append('R')
        if solution_list[i] == 'L2':
            solution_list_full.append('L')
            solution_list_full.append('L')
            
        if '2' not in solution_list[i]:
            solution_list_full.append(solution_list[i])


    print(solution_list) # Prints the solution in the commandline
    initial_scramble = solution_list
    initial_scramble.reverse()

    print(initial_scramble)

    def showsolve():
        game.move_display(solution_list_full)

    game.btn = Button(scale_x=0.15, scale_y=0.1, x=-.5, color=color.gray, text='Solve', text_size=.5, text_color=color.black, on_click=showsolve) # Creates a scramble button

    game.move_display_no_animation(initial_scramble)        # Displays the users scrambled cube
    game.run()
        
main()

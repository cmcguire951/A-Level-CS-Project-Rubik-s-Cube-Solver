import sqlite3

conn = sqlite3.connect('solves.db')     # Establishes an initial connection
cur = conn.cursor()

sql = """
    CREATE TABLE IF NOT EXISTS Solves (
        SolveID INTEGER PRIMARY KEY AUTOINCREMENT,
        Scramble TEXT,
        Solve_Time FLOAT,
        Number_of_Moves INTEGER,      
        Moves_Completed INTEGER
        )"""

        # Creates the Solves table
        
cur.execute(sql) # Runs the creating command

sql = """
    CREATE TABLE IF NOT EXISTS Datetime (
        Date TEXT,
        Time TEXT,
        SolveID INTEGER PRIMARY KEY AUTOINCREMENT,
        FOREIGN KEY(SolveID) REFERENCES Solves(SolveID)
        )"""

        # Creates the Datetime table

cur.execute(sql)

conn.commit()
conn.close()


def database_entry(scramble, solvetime, number_of_moves, moves_taken, date_of_solve, time_of_solve):
    entry = [scramble, solvetime, number_of_moves, moves_taken]   # Takes the parameters into separate lists for each table
    entry2 = [date_of_solve, time_of_solve]

    query = """INSERT INTO Solves(Scramble,Solve_Time, Number_of_Moves, Moves_Completed) VALUES(?,?,?,?)"""   # Inserts data into the Solves table

    conn = sqlite3.connect('solves.db')
    cur = conn.cursor()

    cur.execute(query, entry)

    query = """INSERT INTO Datetime(Date, Time) VALUES(?,?)"""   # Inserts data into the Datetime table

    cur.execute(query, entry2)

    conn.commit()
    conn.close()

def output_from_db(day, month, year):
    output_from_db.date_input = year + '-' + month + '-' + day  # Concatenates into one string that can be used to search the database
    print(output_from_db.date_input)
   

    conn = sqlite3.connect('solves.db')
    cur = conn.cursor()

    query = """SELECT SolveID FROM Datetime WHERE Date=?"""  # Gets the SolveIDs from the Datetime table
    cur.execute(query,(output_from_db.date_input,))

    IDs = cur.fetchall()
    print(IDs)
    output_from_db.number_of_results = len(IDs)

    query = """SELECT *  FROM Solves WHERE SolveID=?"""   # Uses these SolveIDs to search the Solves table

    output_from_db.Results = list() # List to store the results

    for i in range(1,output_from_db.number_of_results+1):
        cur.execute(query, IDs[i-1])
        output_from_db.Results.append(cur.fetchone())      # Prints the results of the search
        #print(output_from_db.Results[i-1])
    
    conn.close()

def output_all():
    conn = sqlite3.connect('solves.db')
    cur = conn.cursor()

    query = """SELECT SolveID FROM Datetime"""
    cur.execute(query)
    
    output_all.outputs = list()
    all_IDs = cur.fetchall()
    output_all.number_of_results = len(all_IDs)

    query = """SELECT * FROM Solves WHERE SolveID=?"""
    query2 = """SELECT Date,Time FROM Datetime WHERE SolveID=?"""

    for i in range(1,output_all.number_of_results+1):
        cur.execute(query, all_IDs[i-1])        # Adds the required fields to the list
        output_all.outputs.append(cur.fetchone())
        
        cur.execute(query2, all_IDs[i-1])       # Adds on the date and time to the correct elements in the list
        output_all.outputs[i-1]+=cur.fetchone()

        #print(output_all.outputs[i-1])

    conn.close()


        
    


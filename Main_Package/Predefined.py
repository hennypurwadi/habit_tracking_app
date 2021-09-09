#create table habit_db file using sqlite3

def tablecreation():
    #print("Table Creation")
        
    try:
        import sqlite3
        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()
        #print("Connected to SQLite")

        command = """CREATE TABLE IF NOT EXISTS 'habit_db'(
            'Id' integer NOT NULL,
            'Title' text NOT NULL,
            'Period' text NOT NULL,
            'Born' integer,
            'Start_Date' integer NOT NULL,
            'Due_Date' integer,
            'Streak' integer,
            'Max_Streak' integer,
            'Break' integer,
            PRIMARY KEY("Id" AUTOINCREMENT)
        )"""

        conn.execute(command)

        # len records of Habits exists
        records = conn.fetchall()
        #print("Total habits are:  ", len(records))
        #print("Succeed to create table")

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            #print("\n")
            #print('SQLite connection is closed')

#Insert 5 predefined habits into habit_db.sqlite3

def predefinedhabits():
    import sqlite3
    import datetime
    import time
    from datetime import datetime, timedelta

    sqliteConnection = sqlite3.connect('habit_db.sqlite3')
    conn = sqliteConnection.cursor()

    habits = [('No Sugar', 'Daily', '2021-07-01', '2021-08-27', '2021-08-28', 2, 10, 5),
              ('Do Sport', 'Daily', '2021-07-01', '2021-08-27', '2021-08-28', 7, 8, 9),
              ('Clean House', 'Weekly', '2021-08-01', '2021-08-22', '2021-08-29', 1, 1, 1),
              ('Eat Fruit', 'Daily', '2021-07-15', '2021-08-25', '2021-08-26', 4, 4, 2),
              ('Help others ', 'Weekly', '2021-08-01', '2021-08-24', '2021-08-31', 0, 0, 2)
              ]

    conn.executemany(
        "INSERT OR REPLACE INTO habit_db ('Title','Period','Born','Start_Date','Due_Date','Streak','Max_Streak','Break') VALUES (?,?,?,?,?,?,?,?)",
        habits)

    sqliteConnection.commit()
    #print("Succeed to create 5 Predefined Habits")




import pytest
from Main_Package.Predefined import tablecreation,predefinedhabits
from Main_Package.AutoResetOverDue import autoresetoverdue
from Main_Package.CreateNew import newhabits
from Main_Package.Delete import deletehabits
from Main_Package.Task import completetask
from Main_Package.Edit import edittitle,edittodaily,edittoweekly
from Main_Package.Analyze import allhabitlist,dailyhabitlist,weeklyhabitlist
from Main_Package.Analyze import longstreakhabits,longstreakdailyhabits,longstreakweeklyhabits
from Main_Package.Analyze import longstreakgivenhabit,shortstreakhabits

import sqlite3
import datetime
import time
from datetime import datetime, timedelta

sqliteConnection = sqlite3.connect('habit_db.sqlite3')
conn = sqliteConnection.cursor()
records = conn.fetchall()
lenrecords = len(records)

def test_tablecreation():
    """test if no row in database"""
    tablecreation()
    assert lenrecords == 0

def test_predefinedhabits():
    predefinedhabits()
    c = conn.execute('SELECT * FROM habit_db')

    assert list(c) == [(1,'No Sugar', 'Daily', '2021-07-01', '2021-08-27', '2021-08-28', 2, 10, 5),
              (2,'Do Sport', 'Daily', '2021-07-01', '2021-08-27', '2021-08-28', 7, 8, 9),
              (3,'Clean House', 'Weekly', '2021-08-01', '2021-08-22', '2021-08-29', 1, 1, 1),
              (4,'Eat Fruit', 'Daily', '2021-07-15', '2021-08-25', '2021-08-26', 4, 4, 2),
              (5,'Help others ', 'Weekly', '2021-08-01', '2021-08-24', '2021-08-31', 0, 0, 2),
              ]

def test_autoresetoverdue():
    autoresetoverdue()

    assert list() == [(1, 'No Sugar', 'Daily', '2021-07-01', '2021-09-12', '2021-09-13', 0, 10, 6),
                            (2, 'Do Sport', 'Daily', '2021-07-01', '2021-09-12', '2021-09-13', 0, 8, 10),
                            (3, 'Clean House', 'Weekly', '2021-08-01', '2021-09-12', '2021-09-19', 0, 1, 2),
                            (4, 'Eat Fruit', 'Daily', '2021-07-15', '2021-09-12', '2021-09-13', 0, 4, 3),
                            (5, 'Help others ', 'Weekly', '2021-08-01', '2021-09-12', '2021-09-19', 0, 0, 3)
                            ]

def test_deletehabits():
    deletehabits()
    # input_delete = '3'
    # inp_delete = 3
    assert list() == [(1, 'No Sugar', 'Daily', '2021-07-01', '2021-09-12', '2021-09-13', 0, 10, 6),
                            (2, 'Do Sport', 'Daily', '2021-07-01', '2021-09-12', '2021-09-13', 0, 8, 10),
                            (3, 'Eat Fruit', 'Daily', '2021-07-15', '2021-09-12', '2021-09-13', 0, 4, 3),
                            (4, 'Help others ', 'Weekly', '2021-08-01', '2021-09-12', '2021-09-19', 0, 0, 3)
                            ]
def test_newhabits():
    newhabits()
    assert list() == [(1, 'No Sugar', 'Daily', '2021-07-01', '2021-09-12', '2021-09-13', 0, 10, 6),
                              (2, 'Do Sport', 'Daily', '2021-07-01', '2021-09-12', '2021-09-13', 0, 8, 10),
                              (3, 'Eat Fruit', 'Daily', '2021-07-15', '2021-09-12', '2021-09-13', 0, 4, 3),
                              (4, 'Help others ', 'Weekly', '2021-08-01', '2021-09-12', '2021-09-19', 0, 0, 3),
                              (5, 'Eat Vegetable', 'Daily', '2021-09-12', '2021-09-12', '2021-09-19', 0, 0, 0)
                             ]

def test_edittitle():
    edittitle()
    #inp_Id = 5
    #Inp_Title = 'Eat Veggie'
    assert list() == [(1, 'No Sugar', 'Daily', '2021-07-01', '2021-09-12', '2021-09-13', 0, 10, 6),
                              (2, 'Do Sport', 'Daily', '2021-07-01', '2021-09-12', '2021-09-13', 0, 8, 10),
                              (3, 'Eat Fruit', 'Daily', '2021-07-15', '2021-09-12', '2021-09-13', 0, 4, 3),
                              (4, 'Help others ', 'Weekly', '2021-08-01', '2021-09-12', '2021-09-19', 0, 0, 3),
                              (5, 'Eat Veggie', 'Daily', '2021-09-12', '2021-09-12', '2021-09-19', 0, 0, 0)
                              ]

def test_edittodaily():
    edittodaily()
    # inp_Id = 4
    assert list() == [(1, 'No Sugar', 'Daily', '2021-07-01', '2021-09-12', '2021-09-13', 0, 10, 6),
                              (2, 'Do Sport', 'Daily', '2021-07-01', '2021-09-12', '2021-09-13', 0, 8, 10),
                              (3, 'Eat Fruit', 'Daily', '2021-07-15', '2021-09-12', '2021-09-13', 0, 4, 3),
                              (4, 'Help others ', 'Daily', '2021-08-01', '2021-09-12', '2021-09-13', 0, 0, 3),
                              (5, 'Eat Veggie', 'Daily', '2021-09-12', '2021-09-12', '2021-09-19', 0, 0, 0)
                              ]

def test_edittoweekly():
    edittoweekly()
    # inp_Id = 1
    assert list() == [(1, 'No Sugar', 'Weekly', '2021-07-01', '2021-09-12', '2021-09-19', 0, 10, 6),
                              (2, 'Do Sport', 'Daily', '2021-07-01', '2021-09-12', '2021-09-13', 0, 8, 10),
                              (3, 'Eat Fruit', 'Daily', '2021-07-15', '2021-09-12', '2021-09-13', 0, 4, 3),
                              (4, 'Help others ', 'Daily', '2021-08-01', '2021-09-12', '2021-09-13', 0, 0, 3),
                              (5, 'Eat Veggie', 'Daily', '2021-09-12', '2021-09-12', '2021-09-19', 0, 0, 0)
                              ]

def test_completetask():
    completetask()
    #inp_Id = 5
    assert list() == [(1, 'No Sugar', 'Weekly', '2021-07-01', '2021-09-12', '2021-09-19', 0, 10, 6),
                              (2, 'Do Sport', 'Daily', '2021-07-01', '2021-09-12', '2021-09-13', 0, 8, 10),
                              (3, 'Eat Fruit', 'Daily', '2021-07-15', '2021-09-12', '2021-09-13', 0, 4, 3),
                              (4, 'Help others ', 'daily', '2021-08-01', '2021-09-12', '2021-09-13', 0, 0, 3),
                              (5, 'Eat Veggie', 'Daily', '2021-09-12', '2021-09-19', '2021-09-26', 1, 1, 0)
                              ]

def test_allhabitlist():
    """Display all habits"""
    allhabitlist()
    assert list() == [(1, 'No Sugar', 'Weekly', '2021-07-01', '2021-09-12', '2021-09-19', 0, 10, 6),
                              (2, 'Do Sport', 'Daily', '2021-07-01', '2021-09-12', '2021-09-13', 0, 8, 10),
                              (3, 'Eat Fruit', 'Daily', '2021-07-15', '2021-09-12', '2021-09-13', 0, 4, 3),
                              (4, 'Help others ', 'daily', '2021-08-01', '2021-09-12', '2021-09-13', 0, 0, 3),
                              (5, 'Eat Veggie', 'Daily', '2021-09-12', '2021-09-19', '2021-09-26', 1, 1, 0)
                              ]

def test_dailyhabitlist():
    """Display all daily habits"""
    dailyhabitlist()
    assert list() == [(2, 'Do Sport', 'Daily', '2021-07-01', '2021-09-12', '2021-09-13', 0, 8, 10),
                              (3, 'Eat Fruit', 'Daily', '2021-07-15', '2021-09-12', '2021-09-13', 0, 4, 3),
                              (4, 'Help others ', 'Daily', '2021-08-01', '2021-09-12', '2021-09-13', 0, 0, 3),
                              (5, 'Eat Veggie', 'Daily', '2021-09-12', '2021-09-19', '2021-09-26', 1, 1, 0)
                              ]

def test_weeklyhabitlist():
    """Display all weekly habits"""
    weeklyhabitlist()
    assert list() == [(1, 'No Sugar', 'Weekly', '2021-07-01', '2021-09-12', '2021-09-19', 0, 10, 6)]

def test_longstreakhabits():
    """Display longest streak habits"""
    longstreakhabits()
    assert list() == [(1, 'No Sugar', 'Weekly', '2021-07-01', '2021-09-12', '2021-09-19', 0, 10, 6)]

def test_longstreakdailyhabits():
    """Display longest streak Daily habits"""
    longstreakdailyhabits()
    assert list() == [(2, 'Do Sport', 'Daily', '2021-07-01', '2021-09-12', '2021-09-13', 0, 8, 10)]

def test_longstreakweeklyhabits():
    """Display longest streak Weekly habits"""
    longstreakweeklyhabits()
    assert list() == [(1, 'No Sugar', 'Weekly', '2021-07-01', '2021-09-12', '2021-09-19', 0, 10, 6)]

def test_longstreakgivenhabit():
    """Display longest streak of given habit"""
    longstreakgivenhabit()
    inp_Id = 2
    assert list() == [(2, 'Do Sport', 'Daily', '2021-07-01', '2021-09-12', '2021-09-13', 0, 8, 10)]

def test_shortstreakhabits():
    """Display shortest streak from all habits"""
    shortstreakhabits()
    assert list() == [(4, 'Help others ', 'daily', '2021-08-01', '2021-09-12', '2021-09-13', 0, 0, 3)]

#python -m pytest test_children.py
#python -k pytest test_children.py
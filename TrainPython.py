"""
This script asks the user if they practiced programming today,
and adds their response to a .csv.

The script checks a .csv for entries for the given day
If there is an entry, returns the total time entered today
Then, asks respondent if they want to make an entry and writes
it in a new cell of the .csv

Last updated: 5 Aug 20
"""
import os
import pandas as pd
import numpy as np
import datetime as dt
path = 'C:/Users/gabee/OneDrive/Documents/TrainPython.xlsx'
df = pd.DataFrame(pd.read_excel(path))

def entry():
    """
    (series of entries -> minutes entry in .csv) 

    Function that creates timestamp on start and writes difference
    between start and stop of function in a .csv file

    """
    
    resp = input("Are you starting to code? Enter 'y' to enter time data: ")
    if resp.lower() == 'y':
        x = dt.datetime.now()
        print("Timer started at " + str(x) + ". To shut off the timer and create entry, press enter again.")
        resp = input("If you want to stop the timer without a creating an entry, type 'stop': ")
        resp = input(" ")
        if not resp.lower() == 'stop':
            y = dt.datetime.now()
            time_min = (y-x)/60
            print(time_min + " minutes spent coding. Adding entry.")
            try:
                pd.DataFrame.to_csv
                # Write code
            except:
                return time_min
                # Failed to write, return minutes
#pd.DataFrame.to_excel(f, [1, 1, 1, 1, 1,])
#type(x)




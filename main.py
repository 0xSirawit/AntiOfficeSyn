from tkinter import *
import datetime
import pandas as pd 
from pathlib import Path  
from IPython.display import display
import os
from numpy import nan 
import notify
import atexit

#get the startup time
opentime = datetime.datetime.now()
DateNow = opentime.strftime('%d/%m/%Y')
StartTime = opentime.strftime('%X')

#create and add info into dataframe
#static-spendtime
path = './AntiOfficeSyn/spendtime.csv' 
isFile = os.path.isfile(path) #checking that is there spendtime.csv in folder
if isFile == False:
    spendtime = pd.DataFrame([[nan, nan, nan, nan]],
                            columns=['Dates', 'StartTime', 'EndTime', 'Duration'])
    filepath = Path('./AntiOfficeSyn/spendtime.csv')  
    filepath.parent.mkdir(parents=True, exist_ok=True)  
    spendtime.to_csv(filepath) 
notify.notify()

#time to seconds
def timetosecond(time):
    time = time.split(':')
    sumsecounds = int(time[0])*3600 + int(time[1])*60 + int(time[2])
    return sumsecounds
#before close the program
def exit_handler():
    EndTime = datetime.datetime.now().strftime('%X')
    spendtime = pd.read_csv('./AntiOfficeSyn/spendtime.csv',index_col=0)
    Duration = datetime.timedelta(seconds=timetosecond(EndTime) - timetosecond(StartTime))
    infotime = pd.DataFrame([[DateNow, StartTime, EndTime, Duration]],
                            columns=['Dates', 'StartTime', 'EndTime', 'Duration'])
    donetime = pd.concat([spendtime,infotime,], ignore_index = True)
    filepath = Path('./AntiOfficeSyn/spendtime.csv')  
    filepath.parent.mkdir(parents=True, exist_ok=True)  
    donetime.to_csv(filepath) 
    display(donetime)
atexit.register(exit_handler)

#setup
root = Tk()
root.title('Anti Office Syndrome')
root.geometry('800x400+0+0')

mylabel = Label(root,text='Anti Office Syndrome', font=18, fg='#fff', bg='#2e2e2e').pack()
def changebtn(): 
    Label(root,text='btnfunction', font=18, fg='#fff', bg='#2e2e2e').pack()
btn = Button(root, text='btn', font=20, fg='#fff', bg='#2e2e2e', command=changebtn).pack()
root.mainloop()
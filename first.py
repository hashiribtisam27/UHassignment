import pandas as pd
import matplotlib.pyplot as plt
#import folium
import html
from IPython.display import display 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# explorng the data
df = pd.read_csv(r"C:\Users\DELL\Desktop\ny.csv")
'''data read from csv'''
df.shape
df.head(5)
dmy = df.copy()
dmy['Date/Time'] = dmy['Date/Time'].map(pd.to_datetime) 
print(dmy.tail())

def getDateOfMonth(dt):
    '''function to get day of the month'''
    return dt.day
dmy['day'] = dmy['Date/Time'].map(getDateOfMonth)

def getWeekDay(dt):
    '''function to get day of the week'''
    return dt.weekday()
dmy['weekday'] = dmy['Date/Time'].map(getWeekDay)  

def getHour(dt):
    '''function to get hour of the day'''
    return dt.hour
dmy['hour'] = dmy['Date/Time'].map(getHour)  

print(dmy.tail())
def histogram():
    '''function to create histogram'''

plt.hist(dmy.day,bins=30,range=(0.5,30.5) ,rwidth=.9)
plt.xlabel('Date of the month')
plt.ylabel('Frequency')
plt.title('Frequency by Date of Month');


def countRow(row):
    '''function for the lineplot 
    it takes row as the argument and prints the lines consisting of 
    '''
    return len(row)
orderByDate = dmy.groupby('day').apply(countRow)  
# print(orderByDate)
plt.plot(orderByDate)


plt.hist(dmy.hour,bins=24,range=(0.5,24) ,rwidth=.9)
plt.xlabel('Hour')
plt.ylabel('Frequency')
plt.title('Frequency by hour');


plt.hist(dmy.weekday,bins=7,range=(-0.5,6),rwidth=.8 ,color="#AA6112")
plt.xticks(range(7),'Mon Tue Wed Thu Fri Sat Sun'.split())
plt.xlabel('Week')
plt.ylabel('Frequency')
plt.title('Frequency by Day')

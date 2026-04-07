
from pathlib import Path 
import csv 

import matplotlib.pyplot as plt

from datetime import datetime

#importing data from csv file
path = Path('project_2.py/grouse_climate_data.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

for index, column_header in enumerate(header_row):
    print(index, column_header)

dates, highs, lows = [], [], []

for row in reader:
    current_date = datetime.strptime(row[4], '%Y-%m-%d')
    

    # if high_raw == '':
    #     print(f'Missing data for {current_date}, skipping...')
    #     continue
    try:
        high = float(row[9])
        low = float(row[11])
        
    except ValueError:
        print(f"Error parsing data at {current_date}")
        continue

    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    print(highs)


#plot max temps
plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots(figsize = (10, 6))
ax.plot(dates, highs, color ='red', alpha = 0.5, label = 'High Temperatures')
ax.plot(dates, lows, color = 'blue', alpha = 0.5, label = 'Low Temperatures')
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1, label = 'Daily Range')

#fomratting
ax.set_title("Daily High and Low Temperatures on Grouse Mountain 2026", fontsize = 20)
ax.set_xlabel('Date in 2026', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (C)",fontsize=16)
ax.tick_params(labelsize=12)

ax.legend(loc = 'upper right', bbox_to_anchor = (0.9, 1.0), fontsize = 12, shadow = True )

#Create grid in background 
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_axisbelow(True)


max_temp = max(highs)
max_date = dates[highs.index(max_temp)]
max = ((max_date, max_temp), colour = 'black')

fig.autofmt_xdate()
plt.show()




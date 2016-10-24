import pandas as pd
import numpy as np

import sys

sys.path.append('../../utility')
import pocket as pk


occupancy_data = pd.read_csv('datatraining.txt', header=0)
occupancy_data = occupancy_data.rename(columns = {'Occupancy':'Classification'})
del occupancy_data['date']
# we need to convert these digits 1 and 5 into a binary signal [1,-1]
occupancy_data['Classification'] = occupancy_data['Classification'].apply(lambda value: value if value==1 else -1)

print pk.pocket(occupancy_data)

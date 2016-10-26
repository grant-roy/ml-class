import pandas as pd


def load_data(name=''):
    data = pd.read_csv(name, header=0)
    data = data.rename(columns = {'Occupancy':'Classification'})
    del data['date']
    data['Classification'] = data['Classification'].apply(lambda value: value if value==1 else -1)
    return data

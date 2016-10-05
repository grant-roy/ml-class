import pandas as pd

# we'll read in a data file for AAPL histroical pricing
df = pd.read_fwf('ABT.txt', colspecs='infer', widths=None, header=0,
                 names=['optionid','issuer','date','cp_flap','exercise_style','index_flag','exdate','root','suffix',
                        'last_date','open_interest','ss_flag','div_convention','flag','ticker','best_bid','best_offer',
                        'volume','strike_price','cfadj','impl_volatility','delta','gamma','theta','vega'])

print(df.tail())

print(df.columns)
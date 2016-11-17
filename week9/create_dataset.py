import pandas as pd


def logistic_function(x=None):
    return


def create_dataset():

    d = pd.DataFrame(columns=['scalar','x1','x2','x3','y'])

    # create samples where each x1=0,x2=0,x3=0
    d = d.append(create_rows(N=2160, numYisZero=2007))

    # create samples where each x1=0,x2=0,x3=1
    d = d.append(create_rows(N=1363, numYisZero=1216, x3=1))

    # create samples where each x1=0,x2=1,x3=0
    d = d.append(create_rows(N=1137, numYisZero=911,x2=1))

    # create samples where each x1=0,x2=1,x3=1
    d = d.append(create_rows(N=547, numYisZero=408, x2=1, x3=1))

    # create samples where each x1=1,x2=0,x3=0
    d = d.append(create_rows(N=886, numYisZero=825, x1=1))

    # create samples where each x1=1,x2=1,x3=0
    d = d.append(create_rows(N=1091, numYisZero=858, x1=1, x2=1, x3=0))

    # create samples where each x1=1,x2=0,x3=1
    d = d.append(create_rows(N=1925, numYisZero=1638, x1=1, x3=1))

    # create samples where each x1=1,x2=1,x3=1
    d = d.append(create_rows(N=1415, numYisZero=1033, x1=1, x2=1, x3=1))

    d['scalar'] = 1
    d.to_csv('datatraining.csv', index=False)


def create_rows(N=0,numYisZero=0,x1=0,x2=0,x3=0):
    ds = pd.DataFrame()
    for n in range(N):
        # set the correct percentage to adopters
        if n >= numYisZero:
            y=1
        else:
            y=0

        ds = ds.append( pd.DataFrame.from_records([{ 'y':y,'x1':x1,'x2':x2,'x3':x3 }]))

    return ds

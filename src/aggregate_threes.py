import pandas as pd
import numpy as np


def fp_concat(df, fp_cols):
    full_fp = []
    for index, row in df.iterrows():
        big_fp = []
        for col in fp_cols:
            for x in row[col]:
                big_fp.append(x)
        full_fp.append(big_fp)
    return full_fp

def abg_aggregate(df, agg = 'concat'):
    methods = ['rdkit']
    cols = df.columns
    fp_cols = {}
    fp_aggr = {}
    
    for method in methods:
        a = [s for s in cols if method in s]
        assert len(a) == 3
        assert a[0][1:].strip('_') == a[1][1:].strip('_') == a[2][1:].strip('_')
        fp_cols[a[0][1:].strip('_')] = a

    if agg == 'concat':
        for key in fp_cols.keys():
            fp_aggr[key] = fp_concat(df, fp_cols[key])
    else: 
        print(f'{agg} aggregation method does not exist')
    return fp_aggr


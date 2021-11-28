#https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_function
#https://stackoverflow.com/questions/6933784/is-there-a-way-to-calculate-correlation-in-tsql-using-over-clauses-instead-of-ct
from scipy.stats import pearsonr
import numpy as np

class corr:
    def __init__(self):
        self.xsum = []
        self.ysum = []

    def step(self,x,y):
        self.xsum.append(x if x is not None else 0)
        self.ysum.append(y if y is not None else 0)
        
    def finalize(self):
        return pearsonr(self.xsum,self.ysum)[0]

class MySum:
    def __init__(self):
        self.count = 0

    def step(self,x):
        if x is not None:
            self.count += x

    def finalize(self):
        return self.count


#STDEV(X)

#SQRT(X)
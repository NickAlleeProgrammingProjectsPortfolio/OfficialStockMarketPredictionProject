from sklearn.base import BaseEstimator, TransformerMixin

class stockAttributeAdder(BaseEstimator, TransformerMixin):
    def __init__(self):
        None
    def fit(self, X, y=None):
        return self
    def transform(self, X, y=None):
        ## logic goes here
        
        #1 day before
        newCols = ["high1DayBefore", "low1DayBefore", "open1DayBefore","close1DayBefore","volume1DayBefore"]
        oldCols = ["High", "Low", "Open", "Close", "Volume"]
        zippedCols = zip(newCols,oldCols)
        for colname, oldcol in zippedCols:
            thisCol = X[oldcol]
            #make it a list
            thisCol = list(thisCol)
            #insert a 0 for 1 day in the begining
            thisCol.insert(0,0)
            #pop the last day off
            thisCol.pop()
            #set the new column to that data
            X[colname] = thisCol
        
        #2 days before
        newCols = ["high2DaysBefore", "low2DaysBefore", "open2DaysBefore","close2DaysBefore","volume2DaysBefore"]
        oldCols = ["High", "Low", "Open", "Close", "Volume"]
        zippedCols = zip(newCols,oldCols)
        for colname, oldcol in zippedCols:
            thisCol = X[oldcol]
            #make it a list
            thisCol = list(thisCol)
            #insert a 0 for 1 day in the begining
            thisCol.insert(0,0)
            #insert a 0 for 2 day in the begining
            thisCol.insert(0,0)
            #pop the last day off
            thisCol.pop()
            #pop the next day off
            thisCol.pop()
            #set the new column to that data
            X[colname] = thisCol
        
        #3 days before
        newCols = ["high3DaysBefore", "low3DaysBefore", "open3DaysBefore","close3DaysBefore","volume3DaysBefore"]
        oldCols = ["High", "Low", "Open", "Close", "Volume"]
        zippedCols = zip(newCols,oldCols)
        for colname, oldcol in zippedCols:
            thisCol = X[oldcol]
            #make it a list
            thisCol = list(thisCol)
            #insert a 0 for 1 day in the begining
            thisCol.insert(0,0)
            #insert a 0 for 2 day in the begining
            thisCol.insert(0,0)
            thisCol.insert(0,0)
            #pop the last day off
            thisCol.pop()
            #pop the next day off
            thisCol.pop()
            thisCol.pop()
            #set the new column to that data
            X[colname] = thisCol
        
        #4 days before
        newCols = ["high4DaysBefore", "low4DaysBefore", "open4DaysBefore","close4DaysBefore","volume4DaysBefore"]
        oldCols = ["High", "Low", "Open", "Close", "Volume"]
        zippedCols = zip(newCols,oldCols)
        for colname, oldcol in zippedCols:
            thisCol = X[oldcol]
            #make it a list
            thisCol = list(thisCol)
            #insert a 0 for 1 day in the begining
            thisCol.insert(0,0)
            #insert a 0 for 2 day in the begining
            thisCol.insert(0,0)
            thisCol.insert(0,0)
            thisCol.insert(0,0)

            #pop the last day off
            thisCol.pop()
            #pop the next day off
            thisCol.pop()
            thisCol.pop()
            thisCol.pop()
            #set the new column to that data
            X[colname] = thisCol
        
        #5 days before
        newCols = ["high5DaysBefore", "low5DaysBefore", "open5DaysBefore","close5DaysBefore","volume5DaysBefore"]
        oldCols = ["High", "Low", "Open", "Close", "Volume"]
        zippedCols = zip(newCols,oldCols)
        for colname, oldcol in zippedCols:
            thisCol = X[oldcol]
            #make it a list
            thisCol = list(thisCol)
            #insert a 0 for 1 day in the begining
            thisCol.insert(0,0)
            #insert a 0 for 2 day in the begining
            thisCol.insert(0,0)
            thisCol.insert(0,0)
            thisCol.insert(0,0)
            thisCol.insert(0,0)

            #pop the last day off
            thisCol.pop()
            #pop the next day off
            thisCol.pop()
            thisCol.pop()
            thisCol.pop()
            thisCol.pop()
            #set the new column to that data
            X[colname] = thisCol
        X = X.iloc[5:]
        X.drop("Dividends", axis = 1, inplace = True)
        X.drop("Stock Splits", axis = 1, inplace = True)
        return X
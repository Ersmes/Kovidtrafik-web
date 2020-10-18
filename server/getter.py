import pandas as pd
import numpy as np
import datetime as dt

def get(date, time):
    hours = (date.month * 30 + date.day - 1) * 24 + time + 1

    total_data = pd.read_csv("total_data.csv")
    average = total_data.mean()
    target = total_data[hours - 1]
    percent = 100 * (target / average)

    upper = np.percentile(total_data, 65)
    lower = np.percentile(total_data, 35)

    if target < lower:
        return "Traffic levels in Atlanta will be low, about %d percent of the average" % percent
    elif target > upper:
        return "Traffic levels in Atlanta will be high, about %d percent of the average" % percent
    else:
        return "Traffic levels in Atlanta will be moderate, about %d percent of the average" % percent
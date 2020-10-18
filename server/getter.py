import pandas as pd
import numpy as np
import datetime as dt

def get(date, time):
    start = dt.date(2020, 8, 30)
    delta = date - start
    hours = delta.days * 24 + time.hour + 1

    total_data = pd.read_csv("predictions.csv")
    predicted_series = pd.Series(total_data.iloc[:,0])
    average = total_data.iloc[:,0].mean()
    target = predicted_series[hours - 1]
    percent = 100 * (target / average)

    upper = np.percentile(total_data, 65)
    lower = np.percentile(total_data, 35)

    if target < lower:
        return "The predicted traffic level is %d, about %d percent of the average traffic level of %d. \n" \
              "Traffic levels in Atlanta will be low." % (target, percent, average)
    elif target > upper:
        return "The predicted traffic level is %d, about %d percent of the average traffic level of %d. \n" \
              "Traffic levels in Atlanta will be high." % (target, percent, average)
    else:
        return "The predicted traffic level is %d, about %d percent of the average traffic level of %d. \n" \
              "Traffic levels in Atlanta will be moderate." % (target, percent, average)
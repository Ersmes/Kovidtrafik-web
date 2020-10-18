from statsmodels.tsa.arima_model import ARIMA

import server.helpers.preprocessing as pp
from server.helpers.arima import difference, inverse_difference

series = pp.get_data()
X = series.values

hours_in_week = 168
diff = difference(X, hours_in_week)

model = ARIMA(diff, order=(3, 1, 1))
model_fit = model.fit(trend='nc', disp=0)

model_fit.save('model.pkl')

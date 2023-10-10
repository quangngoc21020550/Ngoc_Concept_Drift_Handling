from statsforecast.models import AutoARIMA,AutoETS,ARIMA
import pandas as pd
import numpy as np
from statsforecast import StatsForecast
from sklearn.metrics import mean_squared_error,mean_absolute_error
from base_line_model import series_reader,base_line_model

sudden_df=pd.read_csv('../../data/simulated_data/sudden_cd_3000.csv')
sudden_df=sudden_df.drop_duplicates(subset=['drift_point'])
sudden_df=sudden_df.sort_values('drift_point',ascending=True)
sudden_df.reset_index(drop=True, inplace=True)

auto_arima=AutoARIMA(seasonal=False)
auto_ets=AutoETS()
ar_3=ARIMA(order=[3,0,0])
ar_5=ARIMA(order=[5,0,0])

pred_df,error_df=base_line_model(sudden_df,ar_5,100)

pred_df.to_csv('../../result/sudden/ar5_sudden_window_100_prediction.csv',index=False)
error_df.to_csv('../../result/sudden/ar5_sudden_window_100_error.csv',index=False)
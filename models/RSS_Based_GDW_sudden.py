import pandas as pd
import itertools
import numpy as np
import random
from random import choices
from pandas.plotting import autocorrelation_plot
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import pyplot
import lightgbm as lgb
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_absolute_error
import warnings

from config import LOCAL_ABSOLUTE_PATH

window_size_list=[1, 2, 3, 5, 10, 15]
warnings.simplefilter(action='ignore', category=FutureWarning)
from itertools import combinations

# Load three types concept drift df

sudden_df = pd.read_csv(LOCAL_ABSOLUTE_PATH + 'Series_generation/simulated_data/sudden_df.csv')
sudden_df = sudden_df.drop_duplicates(subset=['drift_point'])
sudden_df = sudden_df.sort_values('drift_point', ascending=True)
sudden_df.reset_index(drop=True, inplace=True)

gradual_df=pd.read_csv(LOCAL_ABSOLUTE_PATH + 'Series_generation/simulated_data/gradual_df.csv')
incremental_df=pd.read_csv(LOCAL_ABSOLUTE_PATH + 'Series_generation/simulated_data/incremental_cd.csv')
# Load prediction and RMSE

## Plain

# sudden
Plain_sudden_w200_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Plain_LGBM/sudden/window_200/Plain_LGBM_sudden_cd_cv8_window200.csv')
Plain_sudden_w200_predict_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Plain_LGBM/sudden/window_200/Plain_GBMprediction_cv8_window200.csv')
Plain_sudden_wAll_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Plain_LGBM/sudden/window_all/Plain_LGBM_sudden_cd_cv8_window_All.csv')
Plain_sudden_wAll_predict_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Plain_LGBM/sudden/window_all/Plain_LGBM_prediction_cv8_window_All.csv')

# incremental
Plain_incremental_w200_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Plain_LGBM/incremental/window_200/Plain_LGBM_Incremental_cd_cv8_window200.csv')
Plain_incremental_w200_predict_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Plain_LGBM/incremental/window_200/Plain_LGBM_Incremental_prediction_cv8_window200.csv')
Plain_incremental_wAll_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Plain_LGBM/incremental/window_All/Plain_LGBM_Incremental_cd_cv8_window_All.csv')
Plain_incremental_wAll_predict_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Plain_LGBM/incremental/window_All/Plain_LGBM_Incremental_prediction_cv8_window_All.csv')

# gradual
Plain_gradual_w200_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Plain_LGBM/gradual/window_200/Plain_LGBM_gradual_cd_cv8_window200.csv')
Plain_gradual_w200_predict_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Plain_LGBM/gradual/window_200/plain_LGBM_gradual_prediction_cv8_window200.csv')
Plain_gradual_wAll_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Plain_LGBM/gradual/window_All/Plain_LGBM_gradual_cd_cv8_window_All.csv')
Plain_gradual_wAll_predict_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Plain_LGBM/gradual/window_All/Plain_LGBM_gradual_prediction_cv8_window_All.csv')

## EXP

# sudden
EXP_sudden_w200_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/EXP_LGBM/sudden/window_200/sudden_cd_weighted_cv8_window200.csv')
EXP_sudden_w200_predict_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/EXP_LGBM/sudden/window_200/sudden_prediction_weighted_cv8_window200.csv')
EXP_sudden_wAll_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/EXP_LGBM/sudden/window_all/sudden_cd_weighted_cv8_window_All.csv')
EXP_sudden_wAll_predict_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/EXP_LGBM/sudden/window_all/prediction_weighted_cv8_window_All.csv')

# incremental
EXP_incremental_w200_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/EXP_LGBM/incremental/window_200/Incremental_cd_weighted_cv8_window200.csv')
EXP_incremental_w200_predict_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/EXP_LGBM/incremental/window_200/Incremental_prediction_weighted_cv8_window200.csv')
EXP_incremental_wAll_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/EXP_LGBM/incremental/window_All/Incremental_cd_weighted_cv8_window_All.csv')
EXP_incremental_wAll_predict_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/EXP_LGBM/incremental/window_All/Incremental_prediction_weighted_cv8_window_All.csv')

# gradual
EXP_gradual_w200_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/EXP_LGBM/gradual/window_200/gradual_cd_weighted_cv8_window200.csv')
EXP_gradual_w200_predict_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/EXP_LGBM/gradual/window_200/gradual_prediction_weighted_cv8_window200.csv')
EXP_gradual_wAll_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/EXP_LGBM/gradual/window_All/gradual_cd_weighted_cv8_window_All.csv')
EXP_gradual_wAll_predict_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/EXP_LGBM/gradual/window_All/gradual_prediction_weighted_cv8_window_All.csv')

## Linear

# sudden
Linear_sudden_w200_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Linear_LGBM/sudden/window_200/Linear_sudden_cd_weighted_cv8_window200.csv')
Linear_sudden_w200_predict_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Linear_LGBM/sudden/window_200/Linear_sudden_prediction_weighted_cv8_window200.csv')
Linear_sudden_wAll_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Linear_LGBM/sudden/window_all/Linear_sudden_cd_weighted_cv8_window_All.csv')
Linear_sudden_wAll_predict_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Linear_LGBM/sudden/window_all/Linear_sudden_prediction_weighted_cv8_window_All.csv')

# incremental
Linear_incremental_w200_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Linear_LGBM/incremental/window_200/Linear_Incremental_cd_weighted_cv8_window200.csv')
Linear_incremental_w200_predict_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Linear_LGBM/incremental/window_200/Linear_Incremental_prediction_weighted_cv8_window200.csv')
Linear_incremental_wAll_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Linear_LGBM/incremental/window_All/Linear_Incremental_cd_weighted_cv8_window_All.csv')
Linear_incremental_wAll_predict_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Linear_LGBM/incremental/window_All/Linear_Incremental_prediction_weighted_cv8_window_All.csv')

# gradual
Linear_gradual_w200_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Linear_LGBM/gradual/window_200/Linear_gradual_cd_weighted_cv8_window200.csv')
Linear_gradual_w200_predict_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Linear_LGBM/gradual/window_200/Linear_gradual_prediction_weighted_cv8_window200.csv')
Linear_gradual_wAll_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Linear_LGBM/gradual/window_All/Linear_gradual_cd_weighted_cv8_window_All.csv')
Linear_gradual_wAll_predict_df = pd.read_csv(
    LOCAL_ABSOLUTE_PATH + 'models/Light_GBM_gross_bootstraping/Linear_LGBM/gradual/window_All/Linear_gradual_prediction_weighted_cv8_window_All.csv')


# Function define

def RSS_calculator(y, y_hat):
    RSS = np.sum((y - y_hat) ** 2)
    return RSS


def string_to_list(string_org):
    string = string_org.split(',')
    string_list = []
    for i in range(len(string)):
        if i == 0:
            data = float(string[i][1:])

        elif i == len(string) - 1:
            data = float(string[i][:-1])
        else:
            data = float(string[i])
        string_list.append(data)
    return string_list


def RSS_Based_Gradient(y, y_hat1, y_hat2, weight_1, weight_2):
    error = (y - weight_1 * y_hat1 - weight_2 * y_hat2)
    grad1 = -2 * y_hat1 * error
    grad2 = -2 * y_hat2 * error

    return grad1, grad2


def df_pair(temp_list, n):
    temp_list2 = []
    for c in combinations(temp_list, n):
        temp_list2.append(c)
    return temp_list2


# Build dict

Sudden_dict = {
    'Plain_w200': Plain_sudden_w200_predict_df,
    'Plain_wAll': Plain_sudden_wAll_predict_df,
    'Exp_w200': EXP_sudden_w200_predict_df,
    'Exp_wAll': EXP_sudden_wAll_predict_df,
    'Linear_w200': Linear_sudden_w200_predict_df,
    'Linear_wAll': Linear_sudden_wAll_predict_df
}

Sudden_LGBM_RMSE_dict = {
    'Plain_w200': Plain_sudden_w200_df['testing_RMSE'],
    'Plain_wAll': Plain_sudden_wAll_df['testing_RMSE'],
    'Exp_w200': EXP_sudden_w200_df['testing_RMSE'],
    'Exp_wAll': EXP_sudden_wAll_df['testing_RMSE'],
    'Linear_w200': Linear_sudden_w200_df['testing_RMSE'],
    'Linear_wAll': Linear_sudden_wAll_df['testing_RMSE']
}

Incremetnal_dict = {
    'Plain_w200': Plain_incremental_w200_predict_df,
    'Plain_wAll': Plain_incremental_wAll_predict_df,
    'Exp_w200': EXP_incremental_w200_predict_df,
    'Exp_wAll': EXP_incremental_wAll_predict_df,
    'Linear_w200': Linear_incremental_w200_predict_df,
    'Linear_wAll': Linear_incremental_wAll_predict_df
}

Incremetnal_LGBM_RMSE_dict = {
    'Plain_w200': Plain_incremental_w200_df['testing_RMSE'],
    'Plain_wAll': Plain_incremental_wAll_df['testing_RMSE'],
    'Exp_w200': EXP_incremental_w200_df['testing_RMSE'],
    'Exp_wAll': EXP_incremental_wAll_df['testing_RMSE'],
    'Linear_w200': Linear_incremental_w200_df['testing_RMSE'],
    'Linear_wAll': Linear_incremental_wAll_df['testing_RMSE']
}

Gradual_dict = {
    'Plain_w200': Plain_gradual_w200_predict_df,
    'Plain_wAll': Plain_gradual_wAll_predict_df,
    'Exp_w200': EXP_gradual_w200_predict_df,
    'Exp_wAll': EXP_gradual_wAll_predict_df,
    'Linear_w200': Linear_gradual_w200_predict_df,
    'Linear_wAll': Linear_gradual_wAll_predict_df
}

Gradual_LGBM_RMSE_dict = {
    'Plain_w200': Plain_gradual_w200_df['testing_RMSE'],
    'Plain_wAll': Plain_gradual_wAll_df['testing_RMSE'],
    'Exp_w200': EXP_gradual_w200_df['testing_RMSE'],
    'Exp_wAll': EXP_gradual_wAll_df['testing_RMSE'],
    'Linear_w200': Linear_gradual_w200_df['testing_RMSE'],
    'Linear_wAll': Linear_gradual_wAll_df['testing_RMSE']
}


def GDW_method(error_function,
               window_size_list,
               drfit_type_df,
               df1,
               df2,
               learning_rate=0.01):
    """
    error_functio: RSS,...

    drfit_type_df: sudden_df,gradual_df,incremental_df

    """

    window_size_df_RMSE = pd.DataFrame({
        'window_size_1_RMSE': [],
        'window_size_2_RMSE': [],
        'window_size_3_RMSE': [],
        'window_size_5_RMSE': [],
        'window_size_10_RMSE': [],
        'window_size_15_RMSE': []
    })

    for row in range(len(drfit_type_df)):

        series_row = drfit_type_df.loc[row]
        series = series_row['series']
        series_list = string_to_list(series)

        df1_predic_df_perdiction = df1.iloc[:, row]
        df2__predic_df_perdiction = df2.iloc[:, row]

        weighted_df = pd.DataFrame({
            'df1_predic': df1_predic_df_perdiction,
            'df2_predic': df2__predic_df_perdiction,
            'label': series_list[-len(df1):]
        })
        weighted_df['weighted_perdiction'] = np.NaN
        RMSE_list = []
        weight_1 = 0.5
        weight_2 = 0.5
        for x in range(len(window_size_list)):
            for i in range(len(weighted_df)):
                if i < window_size_list[x]:
                    weighted_df.iloc[i, 3] = 0.5 * weighted_df.iloc[
                        i, 0] + 0.5 * weighted_df.iloc[i, 1]

                else:
                    y = weighted_df.iloc[i - window_size_list[x]:i,
                        2].mean(axis=0)
                    y_hat1 = weighted_df.iloc[i - window_size_list[x]:i,
                             0].mean(axis=0)
                    y_hat2 = weighted_df.iloc[i - window_size_list[x]:i,
                             1].mean(axis=0)

                    grad_1, grad_2 = error_function(y=y,
                                                    y_hat1=y_hat1,
                                                    y_hat2=y_hat2,
                                                    weight_1=weight_1,
                                                    weight_2=weight_2)

                    weight_1_update = weight_1 - grad_1 * learning_rate
                    weight_2_update = weight_2 - grad_2 * learning_rate
                    weighted_df.iloc[
                        i, 3] = weight_1_update * weighted_df.iloc[
                        i, 0] + weight_2_update * weighted_df.iloc[i, 1]
                    weight_1 = weight_1_update
                    weight_2 = weight_2_update

            window_weighted_RMSE = np.sqrt(
                ((weighted_df['weighted_perdiction'] -
                  weighted_df['label']) ** 2).mean())

            RMSE_list.append(window_weighted_RMSE)

        window_size_df_RMSE.loc[row] = RMSE_list

    return window_size_df_RMSE


sudden_GDW__mean_df = pd.DataFrame({
    'info': [],
    'window_size_1_RMSE': [],
    'window_size_2_RMSE': [],
    'window_size_3_RMSE': [],
    'window_size_5_RMSE': [],
    'window_size_10_RMSE': [],
    'window_size_15_RMSE': [],
    'No_weighted_LGBM_1_RMSE': [],
    'No_weighted_LGBM_2_RMSE': []})

sudden_pair_list = []
Sudden_list = list(Sudden_dict.keys())
sudden_pair_list.extend(df_pair(Sudden_list, 2))

for df_pairs in sudden_pair_list:
    df1 = Sudden_dict[df_pairs[0]]
    df2 = Sudden_dict[df_pairs[1]]
    window_size_df_RMSE = GDW_method(error_function=RSS_Based_Gradient,
                                     window_size_list=window_size_list,
                                     drfit_type_df=sudden_df,
                                     df1=df1,
                                     df2=df2)

    window_size_df_RMSE[df_pairs[0]] = Sudden_LGBM_RMSE_dict[df_pairs[0]]
    window_size_df_RMSE[df_pairs[1]] = Sudden_LGBM_RMSE_dict[df_pairs[1]]

    file_name = df_pairs[0] + '_' + df_pairs[1]
    infor = 'Sudden_RSS_based_GDW_'
    path = 'Plain_EXP_Linear_RSS_RMSE_Result_Summary/'
    window_size_df_RMSE.to_csv(path + infor + file_name + '.csv')

    # get mean
    window_size_df_RMSE.rename(columns={df_pairs[0]: 'No_weighted_LGBM_1_RMSE',
                                        df_pairs[1]: 'No_weighted_LGBM_2_RMSE'}, inplace=True)

    window_size_RMSE_mean_dict = dict(np.mean(window_size_df_RMSE, axis=0))
    window_size_RMSE_mean_dict['info'] = file_name

    sudden_GDW__mean_df = sudden_GDW__mean_df.append(window_size_RMSE_mean_dict, ignore_index=True)

sudden_GDW__mean_df.to_csv(path + infor + 'mean_adjusted.csv')
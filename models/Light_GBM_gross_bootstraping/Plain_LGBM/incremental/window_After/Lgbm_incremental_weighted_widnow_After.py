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

warnings.simplefilter(action='ignore', category=FutureWarning)

incremental_df = pd.read_csv('../incremental_cd_2000.csv')
incremental_df = incremental_df.sort_values('start_point', ascending=True)
incremental_df.reset_index(drop=True, inplace=True)


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


def para_num(num_lr, num_sub_feature, Num_leaves, num_min_data, num_max_depth):
    LR_list = [np.random.uniform(0, 1) for i in range(num_lr)]
    LR_list.sort()

    sub_feature_list = [np.random.uniform(0, 1) for i in range(num_sub_feature)]
    sub_feature_list.sort()

    num_leaves_list = [np.random.randint(20, 300) for i in range(Num_leaves)]
    num_leaves_list.sort()

    min_data_list = [np.random.randint(10, 100) for i in range(num_min_data)]
    min_data_list.sort()

    max_depth_list = [np.random.randint(50, 300) for i in range(num_max_depth)]
    max_depth_list.sort()
    boost_type_list = ['goss']
    return LR_list, sub_feature_list, num_leaves_list, min_data_list, max_depth_list, boost_type_list


# define a prequential method
def prequential_CV(K, training_set):
    ave_trainig_RMSE = 0
    ave_training_MAE = float('inf')
    for learning_rate in LR_list:
        for boosting_type in boost_type_list:
            for sub_feature in sub_feature_list:
                for num_leaves in num_leaves_list:
                    for min_data in min_data_list:
                        for max_depth in max_depth_list:
                            params = {'learning_rate': learning_rate,
                                      'boosting_type': boosting_type,
                                      'sub_feature': sub_feature,
                                      'num_leaves': num_leaves,
                                      'min_data': min_data,
                                      'max_depth': max_depth,
                                      'verbosity': -1, 'feature_pre_filter': False}

                            valid_pre_list = list()
                            rows = training_set.count()[0]
                            sum_metric = 0
                            for k in range(K):
                                if k == K - 1:
                                    break
                                train = training_set.iloc[:round((k + 1) * rows / K)]
                                valid = training_set.iloc[round((k + 1) * rows / K):round((k + 2) * rows / K)]
                                train_x = train.drop(columns=['drift_point', 'value'], axis=1)
                                train_y = train['value']

                                valid_lable = valid['value']
                                valid_x = valid.drop(columns=['drift_point', 'value'], axis=1)


                                train_set = lgb.Dataset(train_x, label=train_y)

                                model_gbm = lgb.train(params,
                                                      train_set)

                                valid_pre = model_gbm.predict(valid_x)
                                valid_pre_list.append(valid_pre)

                            all_predic = np.array(list(itertools.chain.from_iterable(valid_pre_list)))
                            valid_label = training_set.iloc[round((1) * rows / K):]['value']
                            RMSE = np.sqrt(((all_predic - valid_label) ** 2).mean())
                            MAE = mean_absolute_error(all_predic, valid_label)

                            if MAE < ave_training_MAE:
                                best_params_dic = {
                                    'learning_rate': learning_rate,
                                    'boosting_type': boosting_type,
                                    'sub_feature': sub_feature,
                                    'num_leaves': num_leaves,
                                    'min_data': min_data,
                                    'max_depth': max_depth
                                }
                                ave_trainig_RMSE = RMSE
                                ave_training_MAE = MAE

    return ave_trainig_RMSE, ave_training_MAE, best_params_dic


test_rmse_df = pd.DataFrame()
test_mae_df = pd.DataFrame()
training_rmse_df = pd.DataFrame()
training_mae_df = pd.DataFrame()
for times in range(100):
    LR_list, sub_feature_list, num_leaves_list, min_data_list, max_depth_list, boost_type_list = para_num(1, 1, 1, 1, 1)
    # training start at drift point
    rmse_list = []
    MAE_list = []
    training_rmse_list = []
    training_mae_list = []
    for row in range(len(incremental_df)):
        incremental_series_row = incremental_df.loc[row]
        incremental_series = incremental_series_row[2]
        incremental_series_list = string_to_list(incremental_series)
        incremental_series_df = pd.DataFrame({})
        incremental_series_df = pd.DataFrame({
            'drift_point': incremental_series_row.start_point,
            'value': incremental_series_list})
        for lags in range(1, 11):
            incremental_series_df['lag' + str(lags)] = incremental_series_df['value'].shift(lags).fillna(0)

        # sudden_series_df['window_std']=np.std(sudden_series_df.loc[:,
        #                       (sudden_series_df.columns!='value')&(sudden_series_df.columns!='drift_point')],
        #                                ddof=1,axis=1)

        drift_point = incremental_series_df.iloc[0, 0]

        meaningful_set = incremental_series_df.iloc[drift_point:]

        training_set = meaningful_set.iloc[:round(0.8 * len(meaningful_set))]
        test_set = meaningful_set.iloc[round(0.8 * len(meaningful_set)):]

        train_x = training_set.drop(columns=['drift_point', 'value'], axis=1)
        train_y = training_set['value']


        train_set = lgb.Dataset(train_x, label=train_y)

        test_x = test_set.drop(columns=['drift_point', 'value'], axis=1)
        test_y = test_set['value']

        ave_trainig_RMSE, ave_training_MAE, best_params_dic = prequential_CV(8, training_set=training_set)

        training_rmse_list.append(ave_trainig_RMSE)
        training_mae_list.append(ave_training_MAE)

        params = {'learning_rate': best_params_dic['learning_rate'],
                  'boosting_type': best_params_dic['boosting_type'],
                  'sub_feature': best_params_dic['sub_feature'],
                  'num_leaves': best_params_dic['num_leaves'],
                  'min_data': best_params_dic['min_data'],
                  'max_depth': best_params_dic['max_depth'],
                  'verbosity': -1}

        best_model = lgb.train(params, train_set)
        test_predict = best_model.predict(test_x)

        testing_RMSE = np.sqrt(((test_predict - test_y) ** 2).mean())
        testing_MAE = mean_absolute_error(test_predict, test_y)

        rmse_list.append(testing_RMSE)
        MAE_list.append(testing_MAE)
    test_rmse_df['times' + str(times)] = rmse_list
    test_mae_df['times' + str(times)] = MAE_list
    training_rmse_df['times' + str(times)] = training_rmse_list
    training_mae_df['times' + str(times)] = training_mae_list

incremental_df['testing_RMSE']=np.mean(test_rmse_df,axis=1)
incremental_df['testing_MAE']=np.mean(test_mae_df,axis=1)
incremental_df['training_RMSE']=np.mean(training_rmse_df,axis=1)
incremental_df['training_MAE']=np.mean(training_mae_df,axis=1)

incremental_df.to_csv('Plain_LGBM_Incremental_cd_cv8_window_After.csv',index=False)

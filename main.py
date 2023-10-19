import time

from config import LOCAL_ABSOLUTE_PATH
import os

RUN_CMD = 'python  ' + LOCAL_ABSOLUTE_PATH

# RUN LGBM MODEL

# EXP_LGBM
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/EXP_LGBM/gradual/window_100/Lgbm_gradual_weighted_widnow100.py") already run
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/EXP_LGBM/gradual/window_200/Lgbm_gradual_weighted_widnow200.py")
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/EXP_LGBM/gradual/window_All/Lgbm_gradual_weighted_widnow_all.py")
# time.sleep(10)
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/EXP_LGBM/incremental/window_100/Lgbm_incremental_weighted_widnow100.py")
# time.sleep(10)
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/EXP_LGBM/incremental/window_200/Lgbm_incremental_weighted_widnow200.py")
# time.sleep(10)
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/EXP_LGBM/incremental/window_After/Lgbm_incremental_weighted_widnow_After.py")
# time.sleep(10)
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/EXP_LGBM/incremental/window_All/Lgbm_incremental_weighted_widnow_All.py")
# time.sleep(10)
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/EXP_LGBM/sudden/window_100/Lgbm_sudden_weighted_widnow100.py")
# time.sleep(10)
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/EXP_LGBM/sudden/window_200/Lgbm_sudden_weighted_widnow200.py")
# time.sleep(10)
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/EXP_LGBM/sudden/window_After/Lgbm_sudden_weighted_widnow_After.py")
# time.sleep(10)
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/EXP_LGBM/sudden/window_all/Lgbm_sudden_weighted_widnowAll.py")
# time.sleep(10)

# # Linear_LGBM
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Linear_LGBM/gradual/window_100/Linear_Lgbm_gradual_weighted_widnow100.py")
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Linear_LGBM/gradual/window_200/Linear_Lgbm_gradual_weighted_widnow200.py")
# time.sleep(10)n
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Linear_LGBM/gradual/window_All/Linear_Lgbm_gradual_weighted_widnow_all.py")
# time.sleep(10)
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Linear_LGBM/incremental/window_100/Linear_Lgbm_incremental_weighted_widnow100.py")
# time.sleep(10)
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Linear_LGBM/incremental/window_200/Linear_Lgbm_incremental_weighted_widnow200.py")
# time.sleep(10)
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Linear_LGBM/incremental/window_After/Linear_Lgbm_incremental_weighted_widnow_After.py")
# time.sleep(10)
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Linear_LGBM/incremental/window_All/Linear_Lgbm_incremental_weighted_widnow_All.py")
# time.sleep(10)
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Linear_LGBM/sudden/window_100/Linear_Lgbm_sudden_weighted_widnow_100.py")
# time.sleep(10)
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Linear_LGBM/sudden/window_200/Linear_Lgbm_sudden_weighted_widnow200.py")
# time.sleep(10)
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Linear_LGBM/sudden/window_After/Linear_Lgbm_sudden_weighted_widnow_After.py")
# time.sleep(10)
# os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Linear_LGBM/sudden/window_all/Linear_Lgbm_sudden_weighted_widnowAll.py")
#

# Plain_LGBM
os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Plain_LGBM/gradual/window_100/Lgbm_gradual_weighted_widnow100.py")
time.sleep(10)
os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Plain_LGBM/gradual/window_200/Lgbm_gradual_weighted_widnow200.py")
time.sleep(10)
os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Plain_LGBM/gradual/window_All/Lgbm_gradual_weighted_widnow_all.py")
time.sleep(10)
os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Plain_LGBM/incremental/window_100/Lgbm_incremental_weighted_widnow100.py")
time.sleep(10)
os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Plain_LGBM/incremental/window_200/Lgbm_incremental_weighted_widnow200.py")
time.sleep(10)
os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Plain_LGBM/incremental/window_After/Lgbm_incremental_weighted_widnow_After.py")
time.sleep(10)
os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Plain_LGBM/incremental/window_All/Lgbm_incremental_weighted_widnow_All.py")
time.sleep(10)
os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Plain_LGBM/sudden/window_100/Lgbm_sudden_weighted_widnow100.py")
time.sleep(10)
os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Plain_LGBM/sudden/window_200/Lgbm_sudden_weighted_widnow200.py")
time.sleep(10)
os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Plain_LGBM/sudden/window_After/Lgbm_sudden_weighted_widnow_After.py")
time.sleep(10)
os.system(RUN_CMD + "models/Light_GBM_gross_bootstraping/Plain_LGBM/sudden/window_all/Lgbm_sudden_weighted_widnowAll.py")

# RUN GDW_ECW
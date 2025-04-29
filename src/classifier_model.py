from optuna.integration import OptunaSearchCV
from optuna import distributions
from sklearn.utils.class_weight import compute_sample_weight
import xgboost
import numpy as np
import pickle

def train_optuna_XGB(X, y, feature_name = ''):
    num_zeros = (y == 0).sum()
    num_ones = (y == 1).sum()
    scw = num_zeros/num_ones
    xgb = xgboost.XGBClassifier()
    
    params = {
        "n_estimators": distributions.IntDistribution(100,1000),
        'scale_pos_weight' : distributions.FloatDistribution(scw/2, 2*scw), #sometimes custom sample weights might be better
        'max_depth': distributions.IntDistribution(1, 20, log=False, step=1),
        "learning_rate": distributions.FloatDistribution(1e-3, 0.1, log=True),
        "subsample": distributions.FloatDistribution(0.05, 1.0),
        "colsample_bytree": distributions.FloatDistribution(0.05, 1.0),
        "min_child_weight": distributions.IntDistribution(1, 20)
    }
    optuna_search = OptunaSearchCV(xgb, params, scoring='roc_auc', 
                                   cv=5,
                                   n_jobs = -1)
    optuna_search.fit(X, y)
    
    model_pkl_file = f'saved_models/{feature_name}_xgb_model.pkl'  
    with open(model_pkl_file, 'wb') as handle:  
        pickle.dump(optuna_search, handle)
    print(optuna_search.best_score_)
    return


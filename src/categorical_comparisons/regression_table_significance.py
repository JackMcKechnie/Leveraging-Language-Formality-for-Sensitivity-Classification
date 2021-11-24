import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.model_selection import cross_validate
from sklearn.preprocessing import scale
from make_scores import make_scores

def regression_table(data,feature_names,type):
    features = data[feature_names]
    target = data["Formality"]

    # Regression setup
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=5)
    cv = KFold(n_splits=10, random_state=1, shuffle=True)
    scoring = ["r2","neg_mean_squared_error","neg_mean_absolute_error","max_error"]

    # Run regressions 

    # Linear regression
    lin_reg = linear_model.LinearRegression()
    lin_reg_scores = cross_validate(lin_reg, X_train, y_train, cv=cv,scoring=scoring)
    

    # Ridge regression
    ridge_reg = linear_model.Ridge()
    ridge_reg_scores = cross_validate(ridge_reg, X_train, y_train, cv=cv,scoring=scoring)

    # Lasso regression
    lasso_reg = linear_model.Lasso()
    lasso_reg_scores = cross_validate(lasso_reg, X_train, y_train, cv=cv,scoring=scoring)

    # LARS Lasso
    lars_lasso_reg = linear_model.LassoLars(normalize=False)
    lars_lasso_reg_scores = cross_validate(lars_lasso_reg, X_train, y_train, cv=cv,scoring=scoring)

    # Bayesian Ridge Regression
    bayesian_ridge_reg = linear_model.BayesianRidge()
    bayesian_ridge_reg_scores = cross_validate(bayesian_ridge_reg, X_train, y_train, cv=cv,scoring=scoring)

    # Stochastic Gradient Descent Regression
    sgd_reg = linear_model.SGDRegressor()
    sgd_reg_scores = cross_validate(sgd_reg, scale(X_train), scale(y_train), cv=cv,scoring=scoring)

    # Generate table

    table = pd.DataFrame()

    table["Linear Regression + " + type + ": MSE"] = lin_reg_scores["test_neg_mean_squared_error"]
    table["Linear Regression + " + type + ": MAE"] = lin_reg_scores["test_neg_mean_absolute_error"]
    
    table["Ridge Regression + " + type + ": MSE"] = ridge_reg_scores["test_neg_mean_squared_error"]
    table["Ridge Regression + " + type + ": MAE"] = ridge_reg_scores["test_neg_mean_absolute_error"]

    table["Lasso Regression + " + type + ": MSE"] = lasso_reg_scores["test_neg_mean_squared_error"]
    table["Lasso Regression + " + type + ": MAE"] = lasso_reg_scores["test_neg_mean_absolute_error"]

    table["LARS Lasso Regression + " + type + ": MSE"] = lars_lasso_reg_scores["test_neg_mean_squared_error"]
    table["LARS Lasso Regression + " + type + ": MAE"] = lars_lasso_reg_scores["test_neg_mean_absolute_error"]

    table["Bayesian Ridge Regression + " + type + ": MSE"] = bayesian_ridge_reg_scores["test_neg_mean_squared_error"]
    table["Bayesian Ridge Regression + " + type + ": MAE"] = bayesian_ridge_reg_scores["test_neg_mean_absolute_error"]

    table["SGD Regression + " + type + ": MSE"] = sgd_reg_scores["test_neg_mean_squared_error"]
    table["SGD Regression + " + type + ": MAE"] = sgd_reg_scores["test_neg_mean_absolute_error"]

    #table["Test"] = test
    
    return table
# Imports
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.model_selection import cross_validate
from sklearn.preprocessing import scale
from make_scores import make_scores
from sklearn.model_selection import GridSearchCV
import numpy as np


def regression_table_tuned(data, feature_names, type):
    features = data[feature_names]
    target = data["Formality"]

    # Regression setup
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=1)
    cv = KFold(n_splits=10, random_state=1, shuffle=True)
    scoring = ["r2", "neg_mean_squared_error",
               "neg_median_absolute_error", "max_error"]

    # Linear regression
    print("Linear regression...")
    lin_reg = linear_model.LinearRegression()
    lin_reg_scores = cross_validate(
        lin_reg, X_train, y_train, cv=cv, scoring=scoring)
    print("Done")

    # Ridge regression
    print("Ridge regression...")
    ridge_reg = linear_model.Ridge()
    ridge_params = {'alpha': [1, 0.1, 0.01, 0.001, 0.0001, 0], "fit_intercept": [
        True, False], "solver": ['svd', 'cholesky', 'lsqr', 'sparse_cg', 'sag', 'saga']}
    ridge_tuned = GridSearchCV(
        estimator=ridge_reg, param_grid=ridge_params, n_jobs=-1)
    ridge_reg_scores = cross_validate(
        ridge_tuned, X_train, y_train, cv=cv, scoring=scoring, n_jobs=-1)
    print("Done")

    # Lasso regression
    print("Lasso regression...")
    lasso_reg = linear_model.Lasso()

    lasso_params = {'alpha': list(np.linspace(0.1, 1, 10)),
                    'fit_intercept': [True, False],
                    'selection': ['cyclic', 'random'],
                    'warm_start': [False, True]}

    lasso_reg_tuned = GridSearchCV(
        estimator=lasso_reg, param_grid=lasso_params, n_jobs=-1)
    lasso_reg_scores = cross_validate(
        lasso_reg_tuned, X_train, y_train, cv=cv, scoring=scoring, n_jobs=-1)
    print("Done")

    # LARS Lasso
    print("LARS Lasso regression...")
    lars_lasso_reg = linear_model.LassoLars(normalize=False)

    lars_lasso_params = {'alpha': list(np.linspace(0.1, 5, 10)),
                         'fit_intercept': [True, False]}

    lars_lasso_reg_tuned = GridSearchCV(
        estimator=lars_lasso_reg, param_grid=lars_lasso_params, n_jobs=-1)
    lars_lasso_reg_scores = cross_validate(
        lars_lasso_reg_tuned, X_train, y_train, cv=cv, scoring=scoring, n_jobs=-1)
    print("Done")

    # Bayesian Ridge Regression
    print("Bayesian Ridge regression...")
    bayesian_ridge_reg = linear_model.BayesianRidge()

    bayesian_ridge_params = {
        'alpha_1': list(np.linspace(1e-7, 2, 10)),
        # 'alpha_2' : list(np.linspace(1e-7,2,10)),
        'lambda_1': list(np.linspace(1e-7, 2, 10)),
        # 'lambda_2' : list(np.linspace(1e-7,2,10))
    }

    bayesian_ridge_reg_tuned = GridSearchCV(
        estimator=bayesian_ridge_reg, param_grid=bayesian_ridge_params, n_jobs=-1)

    bayesian_ridge_reg_scores = cross_validate(
        bayesian_ridge_reg_tuned, X_train, y_train, cv=cv, scoring=scoring)

    print("Done")

    # Stochastic Gradient Descent Regression
    print("Stochastic Gradient Descent regression...")
    sgd_reg = linear_model.SGDRegressor()

    sgd_params = {
        'loss': ['squared_error', 'huber', 'epsilon_insensitive', 'squared_epsilon_insensitive'],
        'penalty': ['l2', 'l1', 'elasticnet'],
        'alpha': [0.000001, 0.00001, 0.0001, 0.001, 0.01, 0.1],
        'fit_intercept': [True, False],
        'learning_rate': ['constant', 'optimal', 'invscaling', 'adaptive']
    }

    sgd_reg_tuned = GridSearchCV(
        estimator=sgd_reg, param_grid=sgd_params, n_jobs=-1)
    sgd_reg_scores = cross_validate(sgd_reg_tuned, scale(
        X_train), scale(y_train), cv=cv, scoring=scoring, n_jobs=-1)
    print("Done")

    # Generate table

    table = pd.DataFrame()

    type = "Nothing"

    table["Linear Regression Tuned + " + type] = make_scores(lin_reg_scores)
    table["Ridge Regression Tuned + " + type] = make_scores(ridge_reg_scores)
    table["Lasso Regression Tuned + " + type] = make_scores(lasso_reg_scores)
    table["LARS Lasso Regression Tuned + " +
          type] = make_scores(lars_lasso_reg_scores)
    table["Bayesian Ridge Regression Tuned + " +
          type] = make_scores(bayesian_ridge_reg_scores)
    table["Stochastic Gradient Descent Regression Tuned + " +
          type] = make_scores(sgd_reg_scores)

    table = table.T
    column_names = ["R Squared", "Negative Mean Squared Error",
                    "Negative Mean Absolute Error", "Max Error"]
    table.columns = column_names

    return table

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
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=1)
    cv = KFold(n_splits=10, random_state=1, shuffle=True)
    scoring = ["r2","neg_mean_squared_error","neg_median_absolute_error","max_error"]

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

    table["Linear Regression + " + type] = make_scores(lin_reg_scores)
    table["Ridge Regression + " + type] = make_scores(ridge_reg_scores)
    table["Lasso Regression + " + type] = make_scores(lasso_reg_scores)
    table["LARS Lasso Regression + " + type] = make_scores(lars_lasso_reg_scores)
    table["Bayesian Ridge Regression + " + type] = make_scores(bayesian_ridge_reg_scores)
    table["Stochastic Gradient Descent Regression + " + type] = make_scores(sgd_reg_scores)


    table = table.T
    column_names = ["R Squared","Negative Mean Squared Error","Negative Mean Absolute Error","Max Error"]
    table.columns = column_names

    return table
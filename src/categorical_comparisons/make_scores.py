import pandas as pd

# Table maker helper function
def make_scores(scores):
    temp = pd.DataFrame()
    out = pd.DataFrame()
    temp["R Squared"] = scores["test_r2"]
    temp["Negative Mean Squared Error"] = scores["test_neg_mean_squared_error"]
    temp["Negative Mean Absolute Error"] = scores["test_neg_median_absolute_error"]
    temp["Max Error"] = scores["test_max_error"]
    r2 = (temp["R Squared"].sum()/10)
    neg_mse = (temp["Negative Mean Squared Error"].sum()/10)
    neg_mae = (temp["Negative Mean Absolute Error"].sum()/10)
    max_err = (temp["Max Error"].sum()/10)
    out = [r2,neg_mse,neg_mae,max_err]
    return out
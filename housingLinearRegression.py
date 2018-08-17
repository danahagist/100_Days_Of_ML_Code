# This file represents a very simple implementation of an sklearn Linear Regression in Python.
# This is from Dataquest's "Linear Regression for Machine Learning" course.
# Very simple, but powerful for certain types of problems.  

# Dropping NA values and one of the features (feature with very low variance in the dataset)
clean_test = test[final_corr_cols.index].dropna()
features = features.drop('Open Porch SF')

# Creating Linear Regression model and training on training data
lr = LinearRegression()
lr.fit(train[features], train['SalePrice'])

# Making predictions on train and test set based on the model
train_predictions = lr.predict(train[features])
test_predictions = lr.predict(clean_test[features])

# Calculating the mean squared error on train and test set
train_mse = mean_squared_error(train_predictions, train['SalePrice'])
test_mse = mean_squared_error(test_predictions, clean_test['SalePrice'])

# Calculating root mean squared error (RMSE) based on the above
# RMSE used due to being in same units as the target column
train_rmse_2 = np.sqrt(train_mse)
test_rmse_2 = np.sqrt(test_mse)

# Printing our root mean squared error
print(train_rmse_2)
print(test_rmse_2)

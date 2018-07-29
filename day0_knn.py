# Here is an exmple code file for using KNN with holdout validation

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

train_one = split_one
test_one = split_two
train_two = split_two
test_two = split_one

knn = KNeighborsRegressor()
knn.fit(train_one[['accommodates']], train_one['price'])
predictions = knn.predict(test_one[['accommodates']])
iteration_one_rmse = mean_squared_error(test_one['price'], predictions)**(1/2)

knn2 = KNeighborsRegressor()
knn2.fit(train_two[['accommodates']], train_two['price'])
predictions2 = knn2.predict(test_two[['accommodates']])
iteration_two_rmse = mean_squared_error(test_two['price'], predictions2)**(1/2)

avg_rmse = np.mean([iteration_one_rmse, iteration_two_rmse])

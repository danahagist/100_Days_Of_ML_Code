# Below is an example of training, predicting, and determining model accuracy for Decision Tree Classifer
# and a RandomForest model, each with different parameters


#Decision Tree Model
clf = DecisionTreeClassifier(random_state=1, min_samples_leaf=5)

clf.fit(train[columns], train["high_income"])

predictions = clf.predict(train[columns])
print(roc_auc_score(train["high_income"], predictions))

predictionsDT = clf.predict(test[columns])
print(roc_auc_score(test["high_income"], predictionsDT))


# Random Forest Model
clf = RandomForestClassifier(n_estimators=150, random_state=1, min_samples_leaf=5)
clf.fit(train[columns], train['high_income'])

predictionsRFTr = clf.predict(train[columns])
print(roc_auc_score(train["high_income"], predictionsRFTr))

predictionsRFTe = clf.predict(test[columns])
print(roc_auc_score(test['high_income'], predictionsRFTe))
